from abc import abstractmethod


class OptimizationFunction:
    def __init__(self, lr=0.01, momentum=0.01):
        """
        Initializes the parameters used in the update function

        Parameters
        ----------
        lr: float
            The learning rate
        momentum: float
            The momentum term
        """
        self.lr = lr
        self.momentum = momentum

    def update(self, parameter, gradient):
        """
        Returns the updated parameter given the parameter and the gradient of the parameter

        Parameters
        ----------
        parameter: np.array
            A numpy array of parameters (weights)
        gradient: np.array
            A numpy array of parameter gradients

        Returns
        -------
        updated_parameter: np.array
            A numpy array of updated parameters (weights)
        """
        pass