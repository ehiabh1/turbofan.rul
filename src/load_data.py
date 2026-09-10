import pandas as pd
from pathlib import Path

COLS = ["unit", "cycle", "op1", "op2", "op3"] + [f"s{i}" for i in range(1, 22)]
DATA_DIR = Path(__file__).resolve().parents[1] / "data"

def load_fd(subset="FD001"):
    def read(name):
        return pd.read_csv(DATA_DIR / f"{name}_{subset}.txt",
                           sep=r"\s+", header=None, names=COLS)
    train, test = read("train"), read("test")
    rul = pd.read_csv(DATA_DIR / f"RUL_{subset}.txt", header=None, names=["RUL"])
    # Train engines run to failure, so RUL = last cycle - current cycle
    train["RUL"] = train.groupby("unit")["cycle"].transform("max") - train["cycle"]
    return train, test, rul
