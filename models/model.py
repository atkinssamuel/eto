import math
from abc import abstractmethod

import numpy as np
from matplotlib import pyplot as plt

from model_components.loss_functions.bce_loss import BCELoss
from model_components.optimization_functions.gradient_descent import GradientDescent
from shared.helpers import xavier_init


class Model:
    """
    This is the over-arching "Model" class that all subsequent models must inherit from to ensure that the model
    functionality is consistent
    """
    def __init__(self, batch_size=256, n_epochs=50, lr=0.01, momentum=0.01, plot_losses=False, loss_fn=BCELoss,
                 optimization_fn=GradientDescent, weight_init_fn=xavier_init):
        # hyperparameters:
        self.batch_size = batch_size
        self.n_epochs = n_epochs
        self.lr = lr
        self.momentum = momentum
        self.plot_losses = plot_losses
        self.loss_fn = loss_fn
        self.optimization_fn = optimization_fn
        self.weight_init_fn = weight_init_fn

        self.layers = []
        self.losses = []

    def fit(self, X, y):
        """
        Updates the state of self.model by fitting this model to the X and y data.

        Parameters
        ----------
        X: np.array
            A numpy array of input data. This array has shape [N, M] where N is the number of data points and M is the
            number of data features
        y: np.array
            A numpy array of target data. This array has shape [N,] where N is the number of data points and each data
            entry is an integer that represents the class that this data entry belongs to. For binary classification,
            the y numpy array has only 0's and 1's
        """
        self.init_layers(X)

        X_batches, y_batches = self.create_batches(X, y)

        for epoch in range(self.n_epochs):
            for X_batch, y_batch in zip(X_batches, y_batches):
                out = self.forward(X_batch)
                loss, loss_signal = self.loss_fn.compute_loss(y_batch, out)
                self.losses.append(np.average(loss))
                self.backward(loss_signal)

        if self.plot_losses:
            self.plot_loss_curve()

    def predict(self, X):
        """
        Predicts on the supplied X data using self.model

        Parameters
        ----------
        X: np.array
            A numpy array of input data. This array has shape [N, M] where N is the number of data points and M is the
            number of data features

        Returns
        -------
        preds: np.array
            Returns a numpy array of predictions of shape [N,]. Each entry in the array must be an integer that
            represents the class that this data entry belongs to. For binary classification, the preds numpy array
            has only 0's and 1's.
        """
        return np.round(self.forward(X))

    def forward(self, X):
        """
        Computes the forward pass for all of the model_components in self.model_components

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
        out = X
        for layer in self.layers:
            out = layer.forward(out)
        return out

    def backward(self, y):
        """
        Computes the backward pass for all model_components in self.model_components

        Parameters
        ----------
        y: np.array
            A numpy array of labels
        """
        E = y
        for i in range(len(self.layers)-1, -1, -1):
            E = self.layers[i].backward(E)

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

    def plot_loss_curve(self):
        plt.plot(self.losses)
        plt.show()

    @abstractmethod
    def init_layers(self, X):
        """
        This method initializes the model_components to be used in the model

        Parameters
        ----------
        X: np.array
            A numpy array of input data
        """
        pass
