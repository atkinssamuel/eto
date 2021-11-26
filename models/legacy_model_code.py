from src.helpers import ReLU, sigmoid, xavier_init, binary_cross_entropy, step, average

class MultiLayerBenchmark:
    def __init__(self, D, H, lr):
        initialization_scalar = np.sqrt(2 / D)

        self.lr = lr

        self.X = None

        self.W1 = xavier_init(D, H, initialization_scalar)
        self.W1_ = []
        self.b1 = xavier_init(1, H, initialization_scalar)
        self.b1_ = []

        self.W2 = xavier_init(H, 1, initialization_scalar)
        self.W2_ = []
        self.b2 = xavier_init(1, 1, initialization_scalar)
        self.b2_ = []

        self.a1, self.z1, self.a2, self.z2 = [None] * 4

        self.y = None
        self.loss = None

    def single_sample_forward(self, X):
        """
        Computes a forward pass for a single sample
        :param X: (1,D) np.array of floats
        :return: (1,) np.array of floats
        """
        self.X = X

        self.a1 = self.X @ self.W1 + self.b1
        self.z1 = ReLU(self.a1)

        self.a2 = self.z1 @ self.W2 + self.b2
        self.z2 = sigmoid(self.a2)

        return self.z2

    def batch_forward(self, X):
        """
        Computes a forward pass for a batch of inputs
        :param X: (B,D) np.array of floats
        :return: (B,) np.array of floats
        """
        a1 = X @ self.W1 + np.ones(shape=(X.shape[0], 1)) @ self.b1
        z1 = ReLU(a1)

        a2 = z1 @ self.W2 + np.ones(shape=(X.shape[0], 1)) @ self.b2
        z2 = sigmoid(a2)

        return z2.flatten()

    def compute_loss(self, prediction, label):
        """
        Computes the loss for the model, computes the loss signals, and returns the loss
        :param prediction: float
        :param label: integer
        :return: float
        """
        self.loss = binary_cross_entropy(prediction, label)
        self.y = label

        z2_ = (self.z2 - self.y) / (self.z2 * (1 - self.z2))
        a2_ = z2_ * (sigmoid(self.a2) * (1 - sigmoid(self.a2)))

        self.b2_.append(a2_)
        self.W2_.append(a2_ * np.transpose(self.z1))

        z1_ = a2_ * np.transpose(self.W2)
        a1_ = z1_ * step(self.a1)

        self.b1_.append(a1_)
        self.W1_.append(np.transpose(self.X) @ a1_)

        return self.loss

    def update_params(self):
        self.b2 -= self.lr * average(self.b2_)
        self.W2 -= self.lr * average(self.W2_)

        self.b1 -= self.lr * average(self.b1_)
        self.W1 -= self.lr * average(self.W1_)

        self.b2_ = []
        self.W2_ = []
        self.b1_ = []
        self.W1_ = []


class SingleLayerBenchmark:
    def __init__(self, D, lr):
        initialization_scalar = np.sqrt(2 / D)

        self.lr = lr

        self.W1 = xavier_init(D, 1, initialization_scalar)
        self.W1_ = []
        self.b1 = xavier_init(1, 1, initialization_scalar)
        self.b1_ = []

        self.a, self.y_hat, self.loss = [None]*3

    def single_sample_forward(self, X):
        """
        Computes the forward pass for the model
        :param X: (1,D) np.array
        :return: float
        """
        self.X = X
        self.a = X @ self.W1 + self.b1
        self.y_hat = sigmoid(self.a)
        return self.y_hat

    def batch_forward(self, X):
        """
        Computes a forward pass for a batch of inputs
        :param X: (B,D) np.array
        :return: (B,) np.array of floats
        """
        a = X @ self.W1 + np.ones(shape=(X.shape[0], 1)) * self.b1
        return sigmoid(a).flatten()

    def compute_loss(self, prediction, label):
        """
        Computes the BCE loss from the prediction and label and sets the internal loss signals
        :param prediction: float
        :param label: integer
        :return: float
        """
        self.loss = binary_cross_entropy(prediction, label)

        y_hat_ = (prediction - label)/(prediction * (1 - prediction))
        a_ = y_hat_ * sigmoid(self.a) * (1 - sigmoid(self.a))

        self.W1_.append(self.X.T * a_)
        self.b1_.append(a_)

        return self.loss

    def update_params(self):
        """
        Updates the parameters of the network by averaging over the already computed gradient signals
        :return: None
        """
        self.b1 -= self.lr * average(self.b1_)
        self.W1 -= self.lr * average(self.W1_)

        self.b1_ = []
        self.W1_ = []
        return