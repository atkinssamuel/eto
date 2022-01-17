"""
The purpose of this script is to implement a linear regression model using SGD with CKKS encryption
"""
from src.loader import load_sklearn_data
from src.components.model import Model





class_params = {
    "n_samples": 10000,
    "n_features": 20,
    "n_classes": 2,
    "class_sep": 8,
    "random_state": 88,
}

(
    X_train,
    X_valid,
    X_test,
    y_train,
    y_valid,
    y_test,
) = load_sklearn_data("classification", valid=True, split=[70, 10, 20], **class_params)



print("Hello World")