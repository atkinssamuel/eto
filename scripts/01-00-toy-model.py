import math

from model_components.initialization_functions.xavier_init import XavierInit
from model_components.initialization_functions.zeros_init import ZerosInit
from model_components.layers.relu_layer import ReLULayer
from model_components.layers.sigmoid_approx_layer import SigmoidApprox
from model_components.loss_functions.lse_loss import LSELoss
from model_components.optimization_functions.gradient_descent import GradientDescent
from shared.eval import test_model_implementation
from model_components.layers.rescaling_layer import RescalingLayer
from model_components.layers.linear_layer import LinearLayer
from model_components.layers.sigmoid_layer import SigmoidLayer
from model_components.layers.squared_layer import SquaredLayer
from model_components.loss_functions.bce_loss import BCELoss
from model_components.optimization_functions.nesterov_accelerated_gd import NAG
from model_components.model import Model


class ToyModel(Model):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def init_layers(self, X):
        self.layers.append(
            LinearLayer(
                input_dim=X.shape[1],
                output_dim=math.floor(X.shape[1]*2),
                optimization_fn=GradientDescent,
                weight_init_fn=XavierInit,
                bias_init_fn=ZerosInit,
                lr=self.lr,
                mu=self.mu,
            )
        )
        self.loss_fn = LSELoss()


data_params = {
    "n_samples": 100000,
    "n_features": 20,
    "n_informative": 15,
    "n_targets": 1,
    "random_state": 88,
}

training_params = {
    "lr": 0.001,
    "mu": 0.00001,
    "batch_size": 128,
    "n_epochs": 5,
    "plot_losses": True,
}

test_model_implementation(ToyModel(**training_params), problem_type="regression", **data_params)
