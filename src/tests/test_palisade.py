import numpy as np
import pytest

from src.palisade_container.PALISADE import PALISADE


def test_nothing():
    assert(True)

class TestPALISADE:
    def __init__(self):
        self.palisade_obj = PALISADE()

    def test_encrypt_vector(self):
        input_arr = np.array([1, 2, 3, 4, 5])
        encrypted_vector = self.palisade_obj.encrypt_vector(input_arr, wrapped=True)
        assert encrypted_vector.unpadded_size == 5, "Unpadded size not correctly configured after calling encrypt_vector"
        assert encrypted_vector.size == 8, "Size not correctly configured after calling encrypt_vector"
