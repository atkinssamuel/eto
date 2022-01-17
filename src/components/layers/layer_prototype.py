from abc import abstractmethod


class Layer:
    @abstractmethod
    def forward(self, X):
        """
        The forward pass computed by the layer

        Parameters
        ----------
        X: np.array or C
            The input array or the input palisade container object

        Returns
        -------
        out: np.array or C
            Some transformed output that is either a numpy array or palisade container object
        """
        pass

    @abstractmethod
    def backward(self, E):
        """
        Computes the updated error signal and updates the internal weights of the layer

        Parameters
        ----------
        E: np.array
            The error signal (either a numpy array or palisade container object)

        Returns
        -------
        E_hat: np.array
            The updated error signal (either a numpy array or palisade container object)
        """
