"""
The purpose of this script is to characterize the performance of the implemented encrypted matrix multiply
"""
from src.components.initialization_functions.xavier_init import XavierInit
from src.loader import load_sklearn_data
from src.palisade.ops import PALISADEOperations
from src.shared.timer import Timer

data_params = {
    "n_samples": 50000,
    "n_features": 20,
    "n_informative": 15,
    "n_targets": 1,
    "random_state": 88,
}

(
    X_train,
    X_valid,
    X_test,
    y_train,
    y_valid,
    y_test,
) = load_sklearn_data("regression", valid=True, split=[90, 8, 2], **data_params)

ops = PALISADEOperations(batch_size=20, v=False)
timer = Timer()

W = XavierInit().init(X_test.shape[1])

timer.start()
X_enc = ops.enc_rm(X_test)
timer.end(precision=3, title=f"ops.enc_rm time to encrypt a matrix of size {X_test.shape}")
print("")

timer.start()
matmul_res = ops.rm_cv_mult(X_enc, W)
timer.end(precision=3, title=f"ops.rm_cv_mult time to compute matrix multiply of an encrypted {X_test.shape} matrix by "
                             f"a constant vector of size {W.shape}")
print("")

timer.start()
preds = ops.dec_rm(matmul_res)
timer.end(precision=3, title=f"ops.dec_rm time to decrypt a matrix of size {X_test.shape}")

"""
ops.enc_rm time to encrypt a matrix of size (1000, 20): 15.966s

ops.rm_cv_mult time to compute matrix multiply of an encrypted (1000, 20) matrix by a constant vector of size (20,): 66.665s

ops.dec_rm time to decrypt a matrix of size (1000, 20): 12.847s
"""
