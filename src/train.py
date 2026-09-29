"""Train and evaluate the random-forest baseline on FD001."""

import numpy as np
from sklearn.ensemble import RandomForestRegressor

from src.load_data import load_fd
from src.preprocess import drop_dead, clip_rul
from src.evaluate import rmse, nasa_score


def build_xy(df):
    features = [c for c in df.columns if c not in ("unit", "cycle", "RUL")]
    return df[features], df["RUL"], features


def main():
    train, test, _ = load_fd("FD001")
    tr = clip_rul(drop_dead(train))
    te = clip_rul(drop_dead(test))

    X_train, y_train, features = build_xy(tr)
    # Test engines are scored at their last recorded cycle only.
    X_test, y_test, _ = build_xy(te.groupby("unit").tail(1))

    rf = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    rf.fit(X_train, y_train)
    preds = rf.predict(X_test)

    naive = np.full(len(y_test), y_train.mean())

    print(f"features: {len(features)}")
    print(f"naive (mean) RMSE: {rmse(y_test, naive):.2f}")
    print(f"RF RMSE:           {rmse(y_test, preds):.2f}")
    print(f"RF NASA score:     {nasa_score(y_test, preds):.1f}")


if __name__ == "__main__":
    main()
