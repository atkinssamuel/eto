import math

import numpy as np


def xavier_init(r, c=None):
    """
    Returns numpy array of weights initialized with shape [r, c] using Xavier initialization. If c is not provided,
    returns a numpy array of shape [r,] initialized using Xavier initialization.

    Parameters
    ----------
    r: int
        Number of rows
    c: int
        Number of columns

    Returns
    -------
    initialized weight matrix: np.array
        A numpy array of weights initialized using Xavier initialization
    """
    if c is None:
        return np.random.randn(r) * math.sqrt(r)
    return np.random.randn(r, c) * math.sqrt(r)
