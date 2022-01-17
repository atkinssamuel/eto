import numpy as np
from build.PALISADEContainer import *


palisade_example()

palisade = PALISADE()

x1 = [1, 2, 3]
x2 = [3, 4, 5]

pv1 = palisade.encrypt_vector(x1)
pv2 = palisade.encrypt_vector(x2)

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

print("\nHello World")