"""
This script analyzes the performance of a standard constant-matrix ciphertext-vector multiply where the entries of the
resultant list are the dot products of the rows of the constant matrix with the ciphertext vector
"""
import numpy as np

from src.palisade.ops import PALISADEOperations
from src.shared.timer import Timer

mat_size = 500
X = np.random.rand(mat_size, mat_size)
v = np.random.rand(mat_size)

ops = PALISADEOperations(mat_size, v=False)
v_enc = ops.palisade.encrypt_vector(v)


timer = Timer()
timer.start()
result = ops.cm_v_mult(X, v_enc)
timer.end(title=f"cm_v_mult constant-matrix encrypted-vector multiply for matrix of shape {X.shape} and vector of size "
                f"{v.shape[0]}")

print("ops.cm_v_mult:", np.array(ops.dec_rm(result)[:5]).reshape(-1,))
print("np.matmul:    ", np.matmul(X, v)[:5])

"""
cm_v_mult constant-matrix encrypted-vector multiply for matrix of shape (500, 500) and vector of size 500: 108.0891s
ops.cm_v_mult: [122.3217111  124.07207915 127.38346805 123.48311977 121.45718626]
np.matmul:     [122.3217111  124.07207915 127.38346805 123.48311977 121.45718626]
"""