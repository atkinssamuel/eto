import numpy as np


def create_enc_row_matrix(X: np.array, palisade: object):
    """
    Returns a list of palisade encrypted vector objects. Each element in the list is one ciphertext representing a row
    in X.

    Parameters
    ----------
    X: np.array
        Input matrix.
    palisade: object
        A palisade encryption object used to encrypt the rows of the input matrix.

    Returns
    -------
    row_matrix: list[PALISADEVector]
        A list of palisade vectors.
    """
    print("Encrypting matrix")
    row_matrix = []
    checkpoint_freq = 250
    for i in range(X.shape[0]):
        if i % checkpoint_freq == 0:
            print(f"Encrypting Vector {i}/{X.shape[0]} ({round(100 * i/X.shape[0])}%)")
        row_matrix.append(palisade.encrypt_vector(X[i, :]))
    return row_matrix

def rm_c_mult()