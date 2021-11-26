from layers.activation_functions.sigmoid_layer import SigmoidLayer
from layers.linear_layer import LinearLayer
from layers.loss_functions.bce_loss import BCELoss
from models.model_implementations.model import Model


class LR(Model):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def init_layers(self, X):
        self.layers.append(LinearLayer(input_dim=X.shape[1], output_dim=1))
        self.layers.append(SigmoidLayer())
        self.loss_fn = BCELoss()






