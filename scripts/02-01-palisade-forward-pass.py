from data.loader import load_sklearn_data
from components.layers.sigmoid_layer import SigmoidLayer
from components.loss_functions.lse_loss import LSELoss
from components.layers.linear_layer import LinearLayer
from components.optimization_functions import NAG
from components.model import Model
from shared.eval import evaluate_model


class LSEModel(Model):
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
        self.layers.append(SigmoidLayer())
        self.loss_fn = LSELoss()


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
(
    X_train,
    X_valid,
    X_test,
    y_train,
    y_valid,
    y_test,
) = load_sklearn_data("classification", valid=True, split=[70, 10, 20], **class_params)

model = LSEModel(**training_params)
model.fit(X_train, y_train)
preds = model.predict(X_test)

evaluate_model(preds, y_test, "classification")



encrypted_preds = encrypted_predict(encrypted_X)

print("Hello World")
