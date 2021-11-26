from model_components.optimization_functions.optimization_function_prototype import OptimizationFunction


class NAG(OptimizationFunction):
    def __init__(self, lr=0.01, momentum=0.01):
        super().__init__(lr, momentum)
        self.

    def update(self, parameter, gradient):
        """
        Computes a NAG parameter update:

        https://jlmelville.github.io/mize/nesterov.html#NAG_in_practice

        p_(t+1) = p_(t) + s_(t) + u v_(t)
        """
        return parameter - self.lr * gradient