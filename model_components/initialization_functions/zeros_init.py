import numpy as np

from model_components.initialization_functions.initialization_function_prototype import Initializer


class ZerosInit(Initializer):
    def init(self, r, c=None):
        """
        Zeros Init:

        zero array of shape r x c

        Parameters
        ----------
        r: int
            Number of rows
        c: int
            Number of columns

        Returns
        -------
        initialized weight matrix: np.array
            A numpy array of weights initialized using the specified initialization function
        """
        return np.zeros(shape=(r,) if c is None else (r, c))
