from src.palisade_container.PALISADE import PALISADE
import numpy as np

palisade = PALISADE()

np.random.seed(0)

def left_shift(m: np.array, l: int):
    l = l % len(m)
    return np.hstack((m[l:], m[:l]))


# palisade_example()


# fv = [np.random.randint(1, 10) for i in range(8192)]
# x1 = [1, 2, 3, 4, 5, 6, 7, 0]
x2 = [3, 4, 5, 6, 7, 8, 9, 0]

# pfv = palisade.encrypt_vector(fv, wrapped=False)
# pv1 = palisade.encrypt_vector(x1)
pv2 = palisade.encrypt_vector(x2)
# print(palisade.decrypt_vector(pv2))
# print("\nnp.dot:", np.dot(x1, x2))
# print("v_dot:", palisade.decrypt_vector(palisade.v_dot(pv1, pv2)))
#
# print("\nnp.multiply:", np.multiply(x1, x2))
# print("v_hadamard:", palisade.decrypt_vector(palisade.v_hadamard(pv1, pv2)))
#
# print("\nnp.add:", np.add(x1, x2))
# print("v_add:", palisade.decrypt_vector(palisade.v_add(pv1, pv2)))
#
# print("\nnp.sum:", np.sum(x1))
# print("v_sum:", palisade.decrypt_vector(palisade.v_sum(pv1)))
#
# print("\nnp.dot:", np.dot(x1, x2))
# print("vc_dot:", palisade.decrypt_vector(palisade.vc_dot(pv1, x2)))

# print("\nleft_shift:", left_shift(x2, 3))
# palisade.set_rotation_vector_indices(pv2, [20])
# v_rot_res = palisade.decrypt_vector(palisade.v_rot(pv2, 20))
# print("v_rot:" + f"{v_rot_res}")

print("\nHello World")