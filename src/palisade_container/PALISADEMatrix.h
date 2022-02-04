//
// Created by atkinswsl on 1/30/22.
//

#ifndef PALISADE_CONTAINER_PALISADEMATRIX_H
#define PALISADE_CONTAINER_PALISADEMATRIX_H

#include "PALISADEVector.h"

class PALISADEMatrix {
public:
    bool _row_wise;
    vector<int> shape;
    int rows;
    int columns;
    vector<PALISADEVector> matrix;
    PALISADEMatrix(vector<PALISADEVector> matrix, bool row_wise);
    bool row_wise();
};

PALISADEMatrix::PALISADEMatrix(vector<PALISADEVector> matrix, bool row_wise) {
    this->matrix = matrix;
    _row_wise = row_wise;

    if (_row_wise) {
        rows = int(matrix.size());
        columns = matrix[0]._size;
    } else {
        rows = matrix[0]._size;
        columns = int(matrix.size());
    }
    shape.push_back(rows);
    shape.push_back(columns);
}

bool PALISADEMatrix::row_wise() {
    return _row_wise;
}

#endif //PALISADE_CONTAINER_PALISADEMATRIX_H
