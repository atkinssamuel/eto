from model_components.optimization_functions.optimization_function_prototype import (
    OptimizationFunction,
)


class GradientDescent(OptimizationFunction):
    def __init__(self, lr=0.01, momentum=0.01):
        super().__init__(lr, momentum)

    def update(self, parameter, gradient, momentum=None):
        """
        Computes a gradient descent parameter update

        W = W - LR * dL/dW
        """
        return parameter - self.lr * gradient
