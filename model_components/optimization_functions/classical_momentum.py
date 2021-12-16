from model_components.optimization_functions.optimization_function_prototype import (
    OptimizationFunction,
)


class ClassicalMomentum(OptimizationFunction):
    def __init__(self, lr=0.01, momentum=0.01):
        super().__init__(lr, momentum)

    def update(self, parameter, gradient, momentum=None):
        """
        Returns the updated parameter given the parameter and the gradient of the parameter

        Classical Momentum formulation:

        The parameter update is as follows:

        theta_t+1 = theta_t + v_t+1
        v_t+1 = u * v_t - lr * dL/d(theta)

        Parameters
        ----------
        parameter: np.array
            A numpy array of parameters (weights)
        gradient: np.array
            A numpy array of parameter gradients
        momentum: np.array
            A numpy array that contains the momentum value for the previous time step

        Returns
        -------
        updated_parameter: np.array
            A numpy array of updated parameters (weights)
        momentum: np.array
            A numpy array that contains the momentum value for the current time step
        """
        v = self.momentum * momentum - self.lr * gradient
        return parameter + v, v
