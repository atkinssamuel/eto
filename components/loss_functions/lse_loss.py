import numpy as np

from components.loss_functions.loss_function_prototype import Loss


class LSELoss(Loss):
    def compute_loss(self, y_true, y_pred):
        """
        loss = (y_true - y_pred)^2/2
        loss_signal = y_pred - y_true
        """
        y_true = y_true.reshape(-1, 1)

        loss = np.square(y_true - y_pred)
        loss_signal = y_pred - y_true

        if type(y_true[0][0]) not in {np.float32, np.float64}:
            return loss, -loss_signal
        return loss, loss_signal
