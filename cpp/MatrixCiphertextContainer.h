//
// Created by atkinswsl on 12/24/21.
//

#ifndef CPP_MATRIXCIPHERTEXTCONTAINER_H
#define CPP_MATRIXCIPHERTEXTCONTAINER_H
#include "seal/seal.h"

using namespace seal;
using namespace std;

class MatrixCiphertextContainer {
public:
    Ciphertext encrypted_data;
};


#endif //CPP_MATRIXCIPHERTEXTCONTAINER_H
