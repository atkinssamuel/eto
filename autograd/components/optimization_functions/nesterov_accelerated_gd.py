from autograd.components.optimization_functions.optimization_function_prototype import (
    OptimizationFunction,
)


class NAG(OptimizationFunction):
    def __init__(self, lr=0.01, mu=0.01):
        super().__init__(lr, mu)
        self.phi = 0

    def update(self, parameter, gradient):
        """
        Returns the updated parameter given the parameter and the gradient of the parameter

        https://jlmelville.github.io/mize/nesterov.html#NAG_in_practice

        Nesterov's Accelerated GD (NAG):

        phi_t+1 = theta_t - e_t * grad
        theta_t+1 = phi_t+1 + u * (phi_t+1 - phi_t)

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
        phi_next = parameter - self.lr * gradient
        parameter_next = phi_next + self.mu * (phi_next - self.phi)
        self.phi = phi_next
        return parameter_next
