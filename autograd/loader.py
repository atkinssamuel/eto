import numpy as np
import pandas as pd
from sklearn.datasets import make_classification, make_regression
from sklearn.model_selection import train_test_split


def load_sklearn_data(
    problem_type, valid: bool = False, split: list = None, **data_params: dict
) -> list:
    """
    Loads in an artificial classification dataset using sklearn's make_classification function

    Parameters
    ----------
    problem_type: str
        A string that indicates the problem type ("classification" or "regression")
    valid: bool
        A boolean variable that determines if a validation dataset should be returned

    split: list of int/float
        A list that dictates the train/valid/test or train/test split. Can be of size 2 for just a train/test split
        or a size of 3 for a train/valid/test split. The list will be normalized so it can either be a list of integers
        or a list of floating point fractions:

        [80, 20] or [0.8, 0.2]

    data_params: dict
        A dictionary of optional arguments for the make_classification/make_regression function

        E.g.:

        class_params = {
            "n_samples": 100,
            "n_features": 20,
            "n_classes": 2,
            "class_sep": 4,
            "random_state": 88
        }

    Returns
    -------
    split dataset: list of np.arrays
        A list of numpy arrays. If valid is True, returns:

        [X_train, X_valid, X_test, y_train, y_valid, y_test]

        Otherwise, returns:

        [X_train, X_test, y_train, y_test]

        X_train: np.array of shape [N_train, N_features]
        X_valid: np.array of shape [N_valid, N_features]
        X_test: np.array of shape [N_test, N_features]
        y_train: np.array of shape [N_train,]
        y_valid: np.array of shape [N_valid,]
        y_test: np.array of shape [N_test,]
    """
    if problem_type == "classification":
        X, y = make_classification(**data_params)
    elif problem_type == "regression":
        X, y = make_regression(**data_params)
    else:
        raise Exception("Incorrect problem type. Supported problem types are \"classification\" and \"regression\"")

    if split is None:
        if valid is False:
            split = [0.8, 0.2]
        else:
            split = [0.7, 0.15, 0.15]
    else:
        split = list(np.array(split) / np.sum(split))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=split[-1])

    if valid is False:
        return [X_train, X_test, y_train, y_test]
    else:
        test_size_split = X.shape[0] / X_train.shape[0] * split[1]
        X_train, X_valid, y_train, y_valid = train_test_split(
            X_train, y_train, test_size=test_size_split, random_state=1
        )
        return [X_train, X_valid, X_test, y_train, y_valid, y_test]
