from autograd.components.optimization_functions.optimization_function_prototype import (
    OptimizationFunction,
)


class GradientDescent(OptimizationFunction):
    def __init__(self, lr=0.01, mu=0.01):
        super().__init__(lr, mu)

    def update(self, parameter, gradient):
        """
        Computes a gradient descent parameter update

        W = W - LR * dL/dW
        """
        return parameter - self.lr * gradient
