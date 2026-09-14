DEAD_COLS = ["op3", "s1", "s5", "s10", "s16", "s18", "s19"]
# Two distinct values, no degradation trend. Judgement call, not constant.
NEAR_DEAD_COLS = ["s6"]

def drop_dead(df, drop_near_dead=True):
    cols = DEAD_COLS + (NEAR_DEAD_COLS if drop_near_dead else [])
    return df.drop(columns=[c for c in cols if c in df.columns])
