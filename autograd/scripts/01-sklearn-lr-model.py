from autograd.components.model import Model
from autograd.shared.eval import test_model_implementation
from sklearn.linear_model import LogisticRegression


class SklearnLR(Model):
    """
    Class that implements an sklearn LR model
    """
    def __init__(self):
        super().__init__()
        self.model = LogisticRegression()

    def init_layers(self, X):
        pass

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)


class_params = {
    "n_samples": 10000,
    "n_features": 20,
    "n_classes": 2,
    "class_sep": 4,
    "random_state": 88,
}

test_model_implementation(SklearnLR(), **class_params)
