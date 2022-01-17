import numpy as np

from src.components.layers.layer_prototype import Layer


class SigmoidApprox(Layer):
    def __init__(self, deg=7):
        self.X = None
        self.deg = deg
        self.a_0, self.a_1, self.a_3 = 0.5, 1.20096, -0.81562
        self.b_0, self.b_1, self.b_3, self.b_5, self.b_7 = (
            0.5,
            1.73496,
            -4.19407,
            5.4302,
            -2.50739,
        )
        self.unsupported_exception_str = "The Sigmoid approximation layer was instantiated with an unsupported " \
                                         "degree. Specify either degree 3 or degree 7 for this layer."

    def third_deg_approx(self, x):
        return self.a_0 + self.a_1 * x / 8 + self.a_3 * np.power((x / 8), 3)

    def third_deg_grad(self, x):
        return self.a_1 / 8 + 3 * self.a_3 * np.power((x / 8), 2)

    def seven_deg_grad(self, x):
        return (
            self.b_1 / 8
            + 3 * self.b_3 * np.power((x / 8), 2)
            + 5 * self.b_5 * np.power((x / 8), 4)
            + 7 * self.b_7 * np.power((x / 8), 6)
        )

    def seven_deg_approx(self, x):
        return (
            self.b_0
            + self.b_1 * x / 8
            + self.b_3 * np.power((x / 8), 3)
            + self.b_5 * np.power((x / 8), 5)
            + self.b_7 * np.power((x / 8), 7)
        )

    def forward(self, X):
        """
        If self.deg == 3: return the third degree polynomial approximation of the sigmoid function
        If self.deg == 7: return the seven degree polynomial approximation of the sigmoid function
        Else: raise an exception
        """
        self.X = X
        if self.deg == 3:
            return self.third_deg_approx(X)
        elif self.deg == 7:
            return self.seven_deg_approx(X)
        else:
            raise Exception(self.unsupported_exception_str)

    def backward(self, E):
        if self.deg == 3:
            grad = self.third_deg_grad(self.X)
        elif self.deg == 7:
            grad = self.seven_deg_grad(self.X)
        else:
            raise Exception(self.unsupported_exception_str)
        return np.multiply(E, grad)
