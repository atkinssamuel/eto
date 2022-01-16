import numpy as np

from components.loss_functions.loss_function_prototype import Loss


class BCELoss(Loss):
    def compute_loss(self, y_true, y_pred):
        """
        loss = - (y_true * log(y_pred) + (1- y_true) * log(1 - y_pred))
        loss_signal = (y_true - y_pred) / [y_pred * (1 - y_pred)]
        """
        y_true = y_true.reshape(-1, 1)
        t1 = np.multiply(y_true, np.log(y_pred + np.ones(shape=y_pred.shape) * 0.0001))
        t2 = np.multiply(
            (np.ones(shape=y_true.shape) - y_true),
            np.log(
                np.ones(shape=y_pred.shape)
                - y_pred
                + np.ones(shape=y_pred.shape) * 0.0001
            ),
        )
        loss = -np.add(t1, t2).reshape(-1, 1)
        loss_signal = (
            (y_true - y_pred)
            / (
                y_pred * (np.ones(shape=y_pred.shape) - y_pred)
                + np.ones(shape=y_pred.shape) * 0.0001
            )
        ).reshape(-1, 1)

        return loss, loss_signal
