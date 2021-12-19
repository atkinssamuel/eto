from sklearn.metrics import classification_report

from data.loader import load_sklearn_classification_data
from model_components.model import Model


def evaluate_model(preds, y_true, model_title=None):
    """
    Evaluates the predictions of the model
    Parameters
    ----------
    preds: np.array of integers
        A numpy array of integer predictions. Must be 1-dimensional (shape [N,])

    y_true: np.array of integers
        A numpy array of integer true values. Must be 1-dimensional (shape [N,])

    model_title: str
        An optional argument that delineates the name of the model

    """
    print(f"Evaluating Model:" if model_title is None else f"Evaluating {model_title}:")
    print(classification_report(y_true, preds))


def test_model_implementation(model: Model, **class_params):
    """
    The purpose of this function is to test the implementation of a class that inherits the Model object

    Parameters
    ----------
    model: object
        An instantiation of a class that inherits the master Model class

    class_params: dict
        dictionary of optional arguments for the make_classification function

        E.g.:

        class_params = {
            "n_samples": 100,
            "n_features": 20,
            "n_classes": 2,
            "class_sep": 4,
            "random_state": 88
        }

    """

    (
        X_train,
        X_valid,
        X_test,
        y_train,
        y_valid,
        y_test,
    ) = load_sklearn_classification_data(valid=True, split=[70, 10, 20], **class_params)

    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    evaluate_model(preds, y_test)
