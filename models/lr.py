import math

import numpy as np

from models.model import Model

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


class LinearLayer:
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
        self.W = self.W - lr * np.matmul(np.transpose(self.X), E)
        self.b = self.b - lr * np.sum(E)
        return np.matmul(E, np.transpose(self.W))

    def stack_bias(self, height):
        stacked_bias = []
        for i in range(height):
            stacked_bias.append(self.b)
        return np.array(stacked_bias)


class LR(Model):
    def __init__(self, lr=0.001, batch_size=64):
        super().__init__()
        self.lr = lr
        self.batch_size = batch_size
        self.layers = []
        self.losses = []

    def init_layers(self, X):
        self.layers.append(LinearLayer(input_dim=X.shape[1], output_dim=1))

    def forward(self, X):
        """
        Need to compute sigmoid(XW + b)

        Parameters
        ----------
        X: np.array
            A numpy array of input data. This array has shape [N, M] where N is the number of data points and M is the
            number of data features

        Returns
        -------
        out: np.array of floats
            A numpy array of shape [N,]. Each value is between 0 and 1 and represents the model's prediction on that
            particular X element.
        """
        layer_out = None
        layer_in = X
        for layer in self.layers:
            layer_out = layer.forward(layer_in)
            layer_in = layer_out
        return layer_out

    def fit(self, X, y):
        self.init_layers(X)

        X_batches, y_batches = self.create_batches(X, y)

        for X_batch, y_batch in zip(X_batches, y_batches):
            out = self.forward(X_batch)
            self.losses.append(self.compute_loss(y_batch, out, loss_fn="bce"))

    def compute_loss(self, y_true, y_pred, loss_fn="bce"):
        if loss_fn == "bce":
            return -(np.matmul(y_true, np.log(y_pred)) + np.matmul((1. - y_true), np.log(1. - y_pred)))

    def predict(self, X):
        pass

    def create_batches(self, X, y):
        X_batches = []
        y_batches = []
        n_batches = math.ceil(X.shape[0]/self.batch_size)

        start_ind = 0
        end_ind = self.batch_size
        for batch_ind in range(n_batches-1):
            start_ind += self.batch_size
            end_ind = min(end_ind + self.batch_size, X.shape[0])
            X_batches.append(X[start_ind:end_ind])
            y_batches.append(y[start_ind:end_ind])
        return np.array(X_batches), np.array(y_batches)
