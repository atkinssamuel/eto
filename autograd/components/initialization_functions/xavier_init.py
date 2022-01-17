import numpy as np

from autograd.components.initialization_functions.initialization_function_prototype import Initializer


class XavierInit(Initializer):
    def init(self, r, c=None):
        """
        Xavier Init:

        normal(u, sigma)

        u = 0
        sigma = sqrt(2/(a + b))

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
        mu = 0
        sigma = np.sqrt(2 / (r + (c if c is not None else 0)))
        return np.random.normal(loc=mu, scale=sigma, size=(r,) if c is None else (r, c))
