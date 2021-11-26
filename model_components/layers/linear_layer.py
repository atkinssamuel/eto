import numpy as np

from model_components.layers.layer_prototype import Layer
from model_components.optimization_functions.gradient_descent import GradientDescent
from shared.helpers import xavier_init


class LinearLayer(Layer):
    def __init__(self, input_dim, output_dim, lr=0.01, momentum=0.01, optimization_fn=GradientDescent,
                 weight_init_fn=xavier_init):
        self.X = None
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.W = weight_init_fn(input_dim, output_dim)
        self.b = weight_init_fn(output_dim)

        self.lr = lr
        self.momentum = momentum
        self.optimization_fn = optimization_fn(self.lr, self.momentum)

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

    def backward(self, E):
        """
        Updates the weights and biases using the error signal and returns a new error signal.

        W = W - lr * X^T * E
        b = b - lr * sum(E)

        E_hat = E * W^T

        Parameters
        ----------
        E: np.array of floats
            Error signal that is a np.array of shape N x output_dim

        Returns
        -------
        E_hat: np.array of floats
            The updated error signal (dL/dX) passed on to the next layer
        """
        self.W = self.optimization_fn.update(self.W, np.matmul(np.transpose(self.X), E))
        self.b = self.optimization_fn.update(self.b, np.sum(E))
        return np.matmul(E, np.transpose(self.W))

    def stack_bias(self, height):
        stacked_bias = []
        for i in range(height):
            stacked_bias.append(self.b)
        return np.array(stacked_bias)
