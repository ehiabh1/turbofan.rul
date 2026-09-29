import numpy as np


def rmse(y_true, y_pred):
    return np.sqrt(np.mean((np.asarray(y_true) - np.asarray(y_pred)) ** 2))


def nasa_score(y_true, y_pred):
    """NASA PHM08 asymmetric score. Lower is better; 0 is perfect.

    Late predictions (saying an engine has more life left than it does)
    are penalised harder than early ones, because a missed failure costs
    far more than an unnecessary early inspection.
    """
    d = np.asarray(y_pred) - np.asarray(y_true)
    penalties = np.where(d < 0, np.exp(-d/13) - 1 , np.exp(d/10) - 1)
    return(np.sum(penalties))
    
