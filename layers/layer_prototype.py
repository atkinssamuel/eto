from abc import abstractmethod


class Layer:
    @abstractmethod
    def forward(self, X):
        """
        The forward pass computed by the layer

        Parameters
        ----------
        X: np.array
            The input array

        Returns
        -------
        out: np.array
            Some transformed output
        """
        pass

    @abstractmethod
    def backward(self, E, lr=0.001):
        """
        Computes the updated error signal and updates the internal weights of the layer

        Parameters
        ----------
        E: np.array
            The error signal
        lr: float
            The learning rate

        Returns
        -------
        E_hat: np.array
            The updated error signal
        """
