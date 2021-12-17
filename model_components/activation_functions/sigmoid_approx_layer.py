import numpy as np

from model_components.layers.layer_prototype import Layer


class SigmoidApprox(Layer):
    def __init__(self, deg=3):
        self.X = None
        self.deg = deg

    @staticmethod
    def third_deg_approx(x):
        a_0, a_1, a_3 = 0.5, 1.20096, -0.81562
        return a_0 + a_1 * x / 8 + a_3 * np.power((x / 8), 3)

    @staticmethod
    def seven_deg_approx(x):
        b_0, b_1, b_3, b_5, b_7 = 0.5, 1.73496, -4.19407, 5.4302, -2.50739
        return b_0 + b_1 * x / 8 + b_3 * np.power((x / 8), 3) + b_5 * np.power((x / 8), 5) + b_7 * np.power((x / 8), 7)

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
            raise Exception("The Sigmoid approximation layer was instantiated with an unsupported degree. Specify "
                            "either degree 3 or degree 7 for this layer.")

    def backward(self, E, lr=0.001):
        """
        E_hat = sigmoid(X) * (1 - sigmoid(X))
        """
        t1 = np.multiply(
            self.sigmoid(self.X), np.ones(shape=self.X.shape) - self.sigmoid(self.X)
        )
        return np.multiply(E, t1)


