from data.loader import load_sklearn_classification_data
from models.sklearn_lr import SklearnLR
from shared.eval import evaluate_model

class_params = {
            "n_samples": 10000,
            "n_features": 20,
            "n_classes": 2,
            "class_sep": 4,
            "random_state": 88
}

X_train, X_valid, X_test, y_train, y_valid, y_test = load_sklearn_classification_data(valid=True, split=[70, 10, 20],
                                                                                      **class_params)

LR = SklearnLR()
LR.fit(X_train, y_train)
preds = LR.predict(X_test)

evaluate_model(preds, y_test)

print("Hello World")