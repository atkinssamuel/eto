from autograd.components.initialization_functions import XavierInit
from autograd.components.initialization_functions import ZerosInit
from autograd.components.loss_functions.lse_loss import LSELoss
from autograd.shared.eval import test_model_implementation
from autograd.components.layers.linear_layer import LinearLayer
from autograd.components.optimization_functions import NAG
from autograd.components.model import Model


class ToyModel(Model):
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


data_params = {
    "n_samples": 100000,
    "n_features": 20,
    "n_informative": 15,
    "n_targets": 1,
    "random_state": 88,
}

training_params = {
    "lr": 0.00001,
    "mu": 0.00001,
    "batch_size": 64,
    "n_epochs": 5,
    "plot_losses": True,
}

test_model_implementation(ToyModel(**training_params), problem_type="regression", **data_params)
