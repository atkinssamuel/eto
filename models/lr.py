import math

import numpy as np

from layers.activation_functions.sigmoid_layer import SigmoidLayer
from layers.linear_layer import LinearLayer
from layers.loss_functions.bce_loss import BCELoss
from models.model import Model


class LR(Model):
    def __init__(self, lr=0.001, batch_size=64, n_epochs=50):
        super().__init__(lr, batch_size, n_epochs)

    def init_layers(self, X):
        self.layers.append(LinearLayer(input_dim=X.shape[1], output_dim=1))
        self.layers.append(SigmoidLayer())
        self.loss_fn = BCELoss()






