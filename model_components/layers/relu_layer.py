import numpy as np

from model_components.layers.layer_prototype import Layer


class ReLULayer(Layer):
    def __init__(self):
        self.X = None

    def forward(self, X):
        """
        max(0, X)
        """
        self.X = X
        return np.clip(X, a_min=0, a_max=None)

    def backward(self, E, lr=0.001):
        """
        grad = 0 if X < 0 else 1

        E_hat = E * grad
        """
        return np.multiply((self.X > 0).astype(int), E)
