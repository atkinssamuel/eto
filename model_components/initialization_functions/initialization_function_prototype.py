from abc import abstractmethod


class Initializer:
    def __init__(self):
        pass

    @abstractmethod
    def init(self, r, c=None):
        """
        Returns numpy array of weights initialized with shape [r, c] using the defined weight initialization technique.
        If c is not provided, returns a numpy array of shape [r,] initialized using the defined weight initialization
        technique.

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
        pass
