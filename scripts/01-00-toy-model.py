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
                output_dim=1,
                optimization_fn=NAG,
                lr=self.lr,
                mu=self.mu,
            )
        )
        self.layers.append(SquaredLayer())
        self.layers.append(RescalingLayer(1 / 100))
        self.layers.append(SigmoidLayer())
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

test_model_implementation(ToyModel(**training_params), **class_params)