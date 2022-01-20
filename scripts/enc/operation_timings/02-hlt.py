"""
The purpose of this script is to characterize the performance of the homomorphic linear transform algorithm mentioned
in 2.3 of https://eprint.iacr.org/2018/1041.pdf
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
result = ops.hlt(X, v_enc)
timer.start()

print("ops.hlt:  ", np.array(ops.dec_rm(result)[:5]).reshape(-1,))
print("np.matmul:", np.matmul(X, v)[:5])

timer.end(title=f"ops.hlt for matrix of shape {X.shape} and a vector of size {v.shape[0]}")