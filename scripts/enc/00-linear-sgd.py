"""
The purpose of this script is to implement a linear regression model using SGD with CKKS encryption
"""
import numpy as np
from src.palisade_container.build.PALISADEContainer import *

from src.components.initialization_functions.xavier_init import XavierInit
from src.components.initialization_functions.zeros_init import ZerosInit
from src.components.layers.linear_layer import LinearLayer
from src.components.loss_functions.lse_loss import LSELoss
from src.components.optimization_functions.nesterov_accelerated_gd import NAG
from src.loader import load_sklearn_data
from src.components.model import Model
from src.palisade.ops import create_enc_row_matrix


class LinearSGD(Model):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def init_layers(self, X):
        self.layers.append(
            LinearLayer(
                input_dim=X.shape[1],
                output_dim=1,
                optimization_fn=NAG,
                weight_init_fn=XavierInit,
                bias_init_fn=ZerosInit,
                lr=self.lr,
                mu=self.mu,
            )
        )
        self.loss_fn = LSELoss()




class_params = {
    "n_samples": 1000,
    "n_features": 20,
    "n_classes": 2,
    "class_sep": 8,
    "random_state": 88,
}
training_params = {
    "lr": 0.00001,
    "mu": 0.00001,
    "batch_size": 64,
    "n_epochs": 5,
    "plot_losses": True,
}


linear_sgd = LinearSGD(**training_params)


(
    X_train,
    X_valid,
    X_test,
    y_train,
    y_valid,
    y_test,
) = load_sklearn_data("classification", valid=True, split=[70, 10, 20], **class_params)

palisade = PALISADE()
Xrm = create_enc_row_matrix(X_train, palisade)

W = np.ones(shape=(X_train.shape[1]))
Wenc = palisade.encrypt_vector(W)



linear_sgd.fit(X_train, y_train)

print("Hello World")