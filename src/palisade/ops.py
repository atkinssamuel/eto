from src.palisade_container.build.PALISADEContainer import *

import numpy as np


class PALISADEOperations:
    def __init__(self, batch_size, checkpoint_frequency=250, v=True):
        self.palisade = PALISADEContainer(batch_size)
        self.checkpoint_frequency = checkpoint_frequency
        self.v = v
        self.vec_size = 8192

    def enc_rm(self, X: np.array, v: bool = False):
        """
        Returns a list of palisade encrypted vector objects. Each element in the list is one ciphertext representing a row
        in X.

        Parameters
        ----------
        X: np.array
            Input matrix
        v: bool
            Verbose flag

        Returns
        -------
        row_matrix: list[PALISADEVector]
            A list of palisade vectors
        """
        if self.v or v:
            print("Encrypting matrix")
        row_matrix = []
        r = X.shape[0]
        for i in range(r):
            self._checkpoint(i, r, v, label="Row")
            row_matrix.append(self.palisade.encrypt_vector(X[i, :]))
        return row_matrix

    def dec_rm(self, rm: list[object], v: bool = False):
        """
        Returns a numpy array that is the decrypted row matrix contained in a list of palisade vector objects.

        Parameters
        ----------
        rm: list[PALISADEVector]
            A list of palisade vectors
        v: bool
            Verbose flag

        Returns
        -------
        X: np.array
            Output matrix
        """
        if self.v or v:
            print("Decrypting matrix")
        X = []
        r = len(rm)
        for i in range(r):
            self._checkpoint(i, r, v, label="Row")
            X.append(self.palisade.decrypt_vector(rm[i]))
        return np.array(X)

    def hlt(self, cm: np.array, vector: object, v: bool = False):
        """
        Homomorphic linear transform algorithm mentioned in 2.3 of https://eprint.iacr.org/2018/1041.pdf

        Parameters
        ----------
        cm: np.array
            Constant matrix
        vector: object
            Palisade vector object
        v: bool
            Verbose flag

        Returns
        -------

        """
        result = None
        U = np.zeros(shape=(self.vec_size, self.vec_size))
        U[: cm.shape[0], : cm.shape[1]] = cm
        print("Setting rotation vector")
        self.palisade.set_rotation_vector(vector)

        for l in range(U.shape[0]):
            print(f"Row {l}")
            comp = self.palisade.vc_dot(self.palisade.v_rot(vector, l), self.u_l(U, l))
            if result is None:
                result = comp
            else:
                result = self.palisade.v_add(result, comp)
        return result

    def cm_v_mult(self, cm: np.array, vector: object, v: bool = False):
        """
        Performs a constant-matrix encrypted-vector multiply. Returns a list of palisade encrypted vector objects.

        Parameters
        ----------
        cm: np.array
            Constant matrix
        vector: object
            Palisade vector object
        v: bool
            Verbose flag

        Returns
        -------
        result: list[object]
            A list of ciphertexts each containing one row of the output column vector
        """
        if self.v or v:
            print("Constant-matrix encrypted-vector multiply")
        result = []
        r = cm.shape[0]
        for i in range(r):
            self._checkpoint(i, r, v, label="Row")
            result.append(self.palisade.vc_dot(vector, cm[i, :]))
        return result

    def rm_cv_mult(self, rm: list[object], cv: np.array, v=False):
        """
        Returns a list of palisade encrypted vector objects, each of size 1. These elements in the list are the
        ciphertexts representing the result of multiplying an encrypted row matrix with a constant vector passed in as
        a numpy array.

        Parameters
        ----------
        rm: list[object]
            A list of palisade vector objects representing the input row matrix
        cv: np.array
            The numpy array being used to perform the matrix - constant-vector multiply
        v: bool
            Verbose flag

        Returns
        -------
        result: list[object]
            A list of ciphertexts each containing one row of the output column vector
        """
        if self.v or v:
            print("Row-matrix constant-vector multiply")
        result = []
        r = len(rm)
        for i in range(r):
            self._checkpoint(i, r, v, label="Row")
            result.append(self.palisade.vc_dot(rm[i], cv))
        return result

    def _checkpoint(self, i, size, v: bool = True, label=None):
        """
        Checkpoints the current loop iteration by printing the loop progress
        """
        if (self.v or v) and (i == 0 or (i + 1) % self.checkpoint_frequency == 0):
            prog = f"{i+1}/{size} ({round(100 * (i+1) / size)}%)"
            if label is None:
                print(prog)
            else:
                print(label + " " + prog)

    @staticmethod
    def u_l(U: np.array, l: int):
        """
        Computes the l-th diagonal vector

        Parameters
        ----------
        U: np.array
            Input matrix
        l: int
            The diagonal vector to be computed

        Returns
        -------
        u_l: np.array
            l-th diagonal vector
        """
        u = []
        col = l % U.shape[0]
        for row in range(U.shape[0]):
            u.append(U[row, col])
            col += 1
            col = col % U.shape[0]
        return np.array(u)
