from cpp.build.CustomEncryptor import *

poly_modulus_degree = 8192
bit_sizes = [60, 40, 40, 60]
# scale 2^40
scale_x = 2
scale_y = 40

enc_class = CKKSEncryptor(poly_modulus_degree, bit_sizes, scale_x, scale_y)

enc_data = MatrixCiphertextContainer(enc_class)
enc_data.Encrypt([1, 2, 3])
print(enc_data.Decrypt())
print("Hello World")