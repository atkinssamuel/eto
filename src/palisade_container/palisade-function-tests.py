from src.palisade_container.PALISADE import PALISADE
import numpy as np

palisade = PALISADE()

np.random.seed(0)


def left_shift(m: np.array, l: int):
    l = l % len(m)
    return np.hstack((m[l:], m[:l]))


cm = [[np.random.randint(0, 5) for i in range(3)] for j in range(3)]
x1 = [1, 2, 3]
x2 = [3, 4, 5]

pv1 = palisade.encrypt_vector(x1)
pv2 = palisade.encrypt_vector(x2)

print(palisade.decrypt_vector(pv2))
print("\nnp.dot:", np.dot(x1, x2))
print("v_dot:", palisade.decrypt_vector(palisade.v_dot(pv1, pv2)))

print("\nnp.multiply:", np.multiply(x1, x2))
print("v_hadamard:", palisade.decrypt_vector(palisade.v_hadamard(pv1, pv2)))

print("\nnp.add:", np.add(x1, x2))
print("v_add:", palisade.decrypt_vector(palisade.v_add(pv1, pv2)))

print("\nnp.sum:", np.sum(x1))
print("v_sum:", palisade.decrypt_vector(palisade.v_sum(pv1)))

print("\nnp.dot:", np.dot(x1, x2))
print("vc_dot:", palisade.decrypt_vector(palisade.vc_dot(pv1, x2)))

print("\nleft_shift:", left_shift(x2, 3))
palisade.set_rotation_indices(pv2, 3)
print("v_rot:", palisade.decrypt_vector(palisade.v_rot(pv2, 3)))

print("\nnp.matmul:", np.matmul(cm, x1))
print("cm_v_mult:", palisade.decrypt_vector(palisade.cmv_mult(cm, pv1)))

print("\nHello World")
