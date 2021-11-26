from abc import abstractmethod


class Loss:
    @abstractmethod
    def compute_loss(self, y_true, y_pred):
        """
        Returns the loss and the loss error signal dL/dy_hat where y_hat is the input to the loss signal (y_pred).

        Parameters
        ----------
        y_true: np.array
            A numpy array of labels
        y_pred: np.array
            A numpy array of label predictions

        Returns
        -------
        loss, loss_signal: np.array and np.array
            A numpy array that is the loss and a numpy array that is the error signal that is to be back-propagated.

        """
        pass