import numpy as np

from src.components.layers.layer_prototype import Layer


class SquaredLayer(Layer):
    def forward(self, X):
        """

        Parameters
        ----------
        X: np.array of floats
            The input data to be forward propagated

        Returns
        -------
        out: np.array
            A numpy array of shape [X.shape[1], output_dim] computed by executing X * W + b
        """
        self.X = X
        return np.multiply(X, X)

    def backward(self, E):
        """
        Parameters
        ----------
        E: np.array of floats
            Error signal that is a np.array of shape N x output_dim

        Returns
        -------
        E_hat: np.array of floats
            The updated error signal (dL/dX) passed on to the next layer
        """
        return 2 * self.X * E
