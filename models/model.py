from abc import abstractmethod


class Model:
    """
    This is the over-arching "Model" class that all subsequent models must inherit from to ensure that the model
    functionality is consistent
    """
    def __init__(self):
        self.model = None

    @abstractmethod
    def fit(self, X, y):
        """
        Updates the state of self.model by fitting this model to the X and y data.

        Parameters
        ----------
        X: np.array
            A numpy array of input data. This array has shape [N, M] where N is the number of data points and M is the
            number of data features
        y: np.array
            A numpy array of target data. This array has shape [N,] where N is the number of data points and each data
            entry is an integer that represents the class that this data entry belongs to. For binary classification,
            the y numpy array has only 0's and 1's
        """
        pass

    @abstractmethod
    def predict(self, X):
        """
        Predicts on the supplied X data using self.model

        Parameters
        ----------
        X: np.array
            A numpy array of input data. This array has shape [N, M] where N is the number of data points and M is the
            number of data features

        Returns
        -------
        preds: np.array
            Returns a numpy array of predictions of shape [N,]. Each entry in the array must be an integer that
            represents the class that this data entry belongs to. For binary classification, the preds numpy array
            has only 0's and 1's.
        """
        pass
