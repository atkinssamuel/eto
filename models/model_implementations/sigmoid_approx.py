from model_components.activation_functions.sigmoid_approx_layer import SigmoidApprox
from model_components.layers.linear_layer import LinearLayer
from model_components.layers.rescaling_layer import RescalingLayer
from model_components.loss_functions.bce_loss import BCELoss
from model_components.optimization_functions.nesterov_accelerated_gd import NAG
from models.model import Model


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
