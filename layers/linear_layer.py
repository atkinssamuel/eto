import numpy as np

from layers.layer_prototype import Layer
from shared.helpers import xavier_init


class LinearLayer(Layer):
    def __init__(self, input_dim, output_dim):
        self.X = None
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.W = xavier_init(input_dim, output_dim)
        self.b = xavier_init(output_dim)

    def forward(self, X):
        """

        Parameters
        ----------
        X

        Returns
        -------
        out: np.array
            A numpy array of shape [X.shape[1], output_dim] computed by executing X * W + b
        """
        stacked_bias = self.stack_bias(X.shape[0])
        self.X = X
        return np.matmul(X, self.W) + stacked_bias

    def backward(self, E, lr=0.001):
        """
        Updates the weights and biases using the error signal and returns a new error signal.

        W = W - lr * X^T * E
        b = b - lr * sum(E)

        E_hat = E * W^T

        Parameters
        ----------
        E: np.array of floats
            Error signal that is a np.array of shape N x output_dim
        lr: float
            The learning rate

        Returns
        -------
        E_hat: np.array of floats
            The updated error signal (dL/dX) passed on to the next layer
        """
        self.W = self.W - lr * np.matmul(np.transpose(self.X), E)
        self.b = self.b - lr * np.sum(E)
        return np.matmul(E, np.transpose(self.W))

    def stack_bias(self, height):
        stacked_bias = []
        for i in range(height):
            stacked_bias.append(self.b)
        return np.array(stacked_bias)
