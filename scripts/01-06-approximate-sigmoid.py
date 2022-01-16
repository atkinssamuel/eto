from shared.eval import test_model_implementation
from components.layers.sigmoid_approx_layer import SigmoidApprox
from components.layers.linear_layer import LinearLayer
from components.layers.rescaling_layer import RescalingLayer
from components.loss_functions.bce_loss import BCELoss
from components.optimization_functions import NAG
from components.model import Model


class SigApprox(Model):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def init_layers(self, X):
        self.layers.append(
            LinearLayer(
                input_dim=X.shape[1],
                output_dim=1,
                optimization_fn=NAG,
                lr=self.lr,
                mu=self.mu,
            )
        )
        self.layers.append(RescalingLayer(10))
        self.layers.append(SigmoidApprox(deg=7))
        self.loss_fn = BCELoss()


class_params = {
    "n_samples": 10000,
    "n_features": 20,
    "n_classes": 2,
    "class_sep": 8,
    "random_state": 88,
}

training_params = {
    "lr": 0.01,
    "mu": 0.01,
    "batch_size": 1028,
    "n_epochs": 50,
    "plot_losses": True,
}

test_model_implementation(SigApprox(**training_params), **class_params)
