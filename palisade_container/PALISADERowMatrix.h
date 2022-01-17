//
// Created by atkinswsl on 1/16/22.
//

#ifndef ETO_PALISADEROWMATRIX_H
#define ETO_PALISADEROWMATRIX_H


class PALISADERowMatrix{
public:
    vector<PALISADEVector> prm;

    PALISADERowMatrix(vector<PALISADEVector> palisade_row_matrix);
};

PALISADERowMatrix::PALISADERowMatrix(vector<PALISADEVector> palisade_row_matrix){
    prm = palisade_row_matrix;
}

#endif //ETO_PALISADEROWMATRIX_H
