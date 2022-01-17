import numpy as np

from autograd.components.initialization_functions.zeros_init import ZerosInit
from autograd.components.layers.layer_prototype import Layer
from autograd.components.optimization_functions.gradient_descent import GradientDescent
from autograd.components.initialization_functions.xavier_init import XavierInit


class LinearLayer(Layer):
    def __init__(
        self,
        input_dim,
        output_dim,
        lr=0.01,
        mu=0.01,
        optimization_fn=GradientDescent,
        weight_init_fn=XavierInit,
        bias_init_fn=ZerosInit
    ):
        self.X = None
        self.input_dim = input_dim
        self.output_dim = output_dim

        self.W = weight_init_fn().init(input_dim, output_dim)
        self.W_opt = optimization_fn(lr, mu)

        self.b = bias_init_fn().init(output_dim)
        self.b_opt = optimization_fn(lr, mu)

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
        if type(X):
            pass
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
        self.W = self.W_opt.update(self.W, np.matmul(np.transpose(self.X), E))
        self.b = self.b_opt.update(self.b, np.sum(E))
        return np.matmul(E, np.transpose(self.W))

    def stack_bias(self, height):
        stacked_bias = []
        for i in range(height):
            stacked_bias.append(self.b)
        return np.array(stacked_bias)
