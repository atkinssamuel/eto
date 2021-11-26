from model_components.activation_functions.sigmoid_layer import SigmoidLayer
from model_components.layers.linear_layer import LinearLayer
from model_components.loss_functions.bce_loss import BCELoss
from models.model import Model


class NN(Model):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def init_layers(self, X):
        self.layers.append(LinearLayer(input_dim=X.shape[1], output_dim=X.shape[1]*2))
        self.layers.append(SigmoidLayer())
        self.layers.append(LinearLayer(input_dim=X.shape[1]*2, output_dim=1))
        self.layers.append(SigmoidLayer())
        self.loss_fn = BCELoss()
