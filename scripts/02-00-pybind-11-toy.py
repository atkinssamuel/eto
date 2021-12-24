from cpp.build.CKKSEncryption import *

print("Instantiating CKKS Encryption Class:")
enc_class = CKKSEncryption()

print("CKKS Encrypt:")
print(enc_class.Encrypt([1, 2, 3]))

print("Hello World")