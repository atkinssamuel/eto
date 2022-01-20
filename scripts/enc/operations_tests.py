from src.palisade.ops import PALISADEOperations
import numpy as np

ops = PALISADEOperations(batch_size=64)

X = np.array([[1, 2, 2],
             [2, 3, 1],
             [4, 2, 1]])
v = np.array([1, 5, 9])

X_enc = ops.enc_rm(X)
X_dec = ops.dec_rm(X_enc)

print("X:", X)
print("X_dec:", X_dec)

print("\nnp.matmul:", np.matmul(X, v))
print("ops.rm_cv_mult:", ops.dec_rm(ops.rm_cv_mult(X_enc, v)).reshape(-1,))

