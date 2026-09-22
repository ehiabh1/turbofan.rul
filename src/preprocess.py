# Constant across all FD001 units - no information for the model.
DEAD_COLS = ["op3", "s1", "s5", "s10", "s16", "s18", "s19"]
# Two distinct values, no degradation trend. Judgement call, not constant.
NEAR_DEAD_COLS = ["s6"]
# Operating settings: jitter around a single setpoint in FD001.
OP_COLS = ["op1", "op2"]

RUL_CAP = 125


def drop_dead(df, drop_near_dead=True, drop_ops=True):
    cols = DEAD_COLS
    if drop_near_dead:
        cols = cols + NEAR_DEAD_COLS
    if drop_ops:
        cols = cols + OP_COLS
    return df.drop(columns=[c for c in cols if c in df.columns])


def clip_rul(df, cap=RUL_CAP):
    # YOUR CODE: return a copy of df with RUL capped at `cap`
    pass
