from components.optimization_functions.optimization_function_prototype import (
    OptimizationFunction,
)


class ClassicalMomentum(OptimizationFunction):
    def __init__(self, lr=0.01, mu=0.01):
        super().__init__(lr, mu)
        self.v = 0

    def update(self, parameter, gradient):
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

        Returns
        -------
        updated_parameter: np.array
            A numpy array of updated parameters (weights)
        """
        # v_t+1 = u (self.mu) * v_t (self.v) - lr * dL/d(theta) (gradient)
        self.v = self.mu * self.v - self.lr * gradient

        # theta_t+1 = theta_t (parameter) + v_t+1 (self.v)
        return parameter + self.v
