//
// Created by atkinswsl on 1/30/22.
//

#ifndef PALISADE_CONTAINER_PALISADEMATRIX_H
#define PALISADE_CONTAINER_PALISADEMATRIX_H

#include "PALISADEVector.h"

class PALISADEMatrix {
public:
    bool _row_wise;
    vector<PALISADEVector> matrix;
    PALISADEMatrix(vector<PALISADEVector> matrix, bool row_wise);
    bool row_wise();
};

PALISADEMatrix::PALISADEMatrix(vector<PALISADEVector> matrix, bool row_wise) {
    this->matrix = matrix;
    _row_wise = row_wise;
}

bool PALISADEMatrix::row_wise() {
    return _row_wise;
}

#endif //PALISADE_CONTAINER_PALISADEMATRIX_H
