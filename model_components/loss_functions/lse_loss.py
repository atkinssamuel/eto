import numpy as np

from model_components.loss_functions.loss_function_prototype import Loss


class LSELoss(Loss):
    def compute_loss(self, y_true, y_pred):
        """
        loss = (y_true - y_pred)^2/2
        loss_signal = y_true - y_pred
        """
        y_true = y_true.reshape(-1, 1)

        loss = np.square(y_true - y_pred) / 2
        loss_signal = y_true - y_pred

        return loss, loss_signal
