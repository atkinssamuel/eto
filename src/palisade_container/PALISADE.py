import numpy as np
from build.PALISADEContainer import *


class PALISADE:
    def __init__(self, batch_size=10):
        self.batch_size = batch_size
        self._palisade = PALISADEContainer(self.batch_size)

    def encrypt_vector(self, vector: np.array, wrapped: bool = True):
        """
        Encrypts the supplied vector argument as a PALISADEVector object.

        Parameters
        ----------
        vector: np.array
            The vector to be encrypted
        wrapped: bool
            An argument indicating whether the encoding should be wrapped or not

        Returns
        -------
        pv: object
            A PALISADEVector object instance
        """
        return self._palisade.encrypt_vector(vector, wrapped)

    def decrypt_vector(self, pv: object, decimal_places: int):
        """
        Decrypts the supplied PALISADEVector object and returns a rounded numpy array with the desired decimal places

        Parameters
        ----------
        pv: object
            A PALISADEVector object
        decimal_places: int
            The number of decimal places to round the entries of the decrypted numpy array to

        Returns
        -------
        vector: np.array
            The decrypted PALISADEVector object returned as a numpy array
        """
        return self._palisade.decrypt_vector(pv, decimal_places)

    def v_hadamard(self, pv1: object, pv2: object):
        """
        Takes the vector hadamard product between two PALISADEVector objects and returns a PALISADEVector result object

        Parameters
        ----------
        pv1: object
            A PALISADEVector object
        pv2: object
            A PALISADEVector object
        Returns
        -------
        pv_res: object
            A PALISADEVector object
        """
        return self._palisade.v_hadamard(pv1, pv2)

    def v_dot(self, pv1: object, pv2: object):
        """
        Takes the vector dot product between two PALISADEVector objects and returns a PALISADEVector result object

        Parameters
        ----------
        pv1: object
            A PALISADEVector object
        pv2: object
            A PALISADEVector object
        Returns
        -------
        pv_res: object
            A PALISADEVector object
        """
        return self._palisade.v_dot(pv1, pv2)

    def v_add(self, pv1: object, pv2: object):
        """
        Adds two PALISADEVector objects and returns a PALISADEVector result object

        Parameters
        ----------
        pv1: object
            A PALISADEVector object
        pv2: object
            A PALISADEVector object
        Returns
        -------
        pv_res: object
            A PALISADEVector object
        """
        return self._palisade.v_add(pv1, pv2)

    def v_sum(self, pv: object):
        """
        Sums a PALISADEVector object and returns a PALISADEVector result object

        Parameters
        ----------
        pv: object
            A PALISADEVector object
        Returns
        -------
        pv_res: object
            A PALISADEVector object
        """
        return self._palisade.v_sum(pv)

    def set_rotation_indices(self, pv: object, ind: list[int] or int):
        """
        Sets the rotation indices for future rotations

        Parameters
        ----------
        pv: object
            A PALISADEVector object
        ind: list[int] or int
            A list of integer rotations or a single integer for a single rotation
        """
        if type(ind) is int:
            self._palisade.set_rotation_indices(pv, [ind])
        else:
            self._palisade.set_rotation_indices(pv, ind)

    def v_rot(self, pv: object, rot: int):
        """
        Rotates the supplied PALISADEVector object input argument left by "rot"
        Parameters
        ----------
        pv: object
            A PALISADEVector object
        rot: int
            The rotation value

        Returns
        -------
        pv_res: object
            A PALISADEVector object with the rotated vector
        """
        if type(rot) is not int:
            raise Exception("rot input argument to palisade.v_rot must be an integer value")
        return self._palisade.v_rot(pv, rot)

    def vc_dot(self, pv: object, cv: list[int or float] or np.array):
        """
        Computes the dot product between a PALISADEVector object and a constant vector

        Parameters
        ----------
        pv: object
            A PALISADEVector object
        cv: list or np.array

        Returns
        -------
        pv_res: object
            The result of the dot product returned as a PALISADEVector object
        """
        return self._palisade.vc_dot(pv, cv)