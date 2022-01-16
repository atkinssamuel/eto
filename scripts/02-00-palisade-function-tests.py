import numpy as np
from palisade_container.build.PALISADEContainer import *

# palisade_example()

palisade = PALISADE()

x1 = [1, 2, 3]
x2 = [3, 4, 5]

pv = palisade.encrypt_vector(x1)
pv2 = palisade.encrypt_vector(x2)

print("\nNumpy dot product result:", np.dot(x1, x2))
print("Encrypted computation result:", palisade.decrypt_vector(palisade.dot(pv, pv2)))

print("\nNumpy hadamard product result:", np.multiply(x1, x2))
print("Encrypted computation result:", palisade.decrypt_vector(palisade.hadamard(pv, pv2)))

print("\nNumpy add vectors result:", np.add(x1, x2))
print("Encrypted computation result:", palisade.decrypt_vector(palisade.add(pv, pv2)))

print("\nNumpy sum result:", np.sum(x1))
print("Encrypted computation result:", palisade.decrypt_vector(palisade.sum(pv)))

print("Hello World")