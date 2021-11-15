from sklearn.linear_model import LogisticRegression
from models.model import Model


class SklearnLR(Model):
    """
    Class that implements an sklearn LR model
    """

    def __init__(self, **params):
        super().__init__()
        self.model = LogisticRegression(**params)

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)
