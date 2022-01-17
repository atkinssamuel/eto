import numpy as np

from autograd.components.layers.layer_prototype import Layer


class SigmoidLayer(Layer):
    def __init__(self):
        self.X = None

    @staticmethod
    def sigmoid(X):
        """
        1 / (1 + exp(X))
        """
        return 1 / (1 + np.exp(X))

    def forward(self, X):
        """
        1 / (1 + exp(X))
        """
        self.X = X
        return self.sigmoid(X)

    def backward(self, E, lr=0.001):
        """
        E_hat = sigmoid(X) * (1 - sigmoid(X))
        """
        t1 = np.multiply(
            self.sigmoid(self.X), np.ones(shape=self.X.shape) - self.sigmoid(self.X)
        )
        return np.multiply(E, t1)
