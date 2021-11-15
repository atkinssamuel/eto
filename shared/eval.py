from sklearn.metrics import classification_report


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
