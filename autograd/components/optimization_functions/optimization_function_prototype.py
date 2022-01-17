class OptimizationFunction:
    def __init__(self, lr=0.01, mu=0.01):
        """
        Initializes the parameters used in the update function

        Parameters
        ----------
        lr: float
            The learning rate
        mu: float
            The momentum term
        """
        self.lr = lr
        self.mu = mu

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
