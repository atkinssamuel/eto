//
// Created by atkinswsl on 1/16/22.
//

#ifndef ETO_UTILS_H
#define ETO_UTILS_H

vector<double> splice_vector(vector<double> x, int start, int end) {
    if (start < 0)
        throw std::invalid_argument("Received a start value less than 0.");
    if (end > int(x.size()))
        throw invalid_argument("Received an end value greater than the size of the input vector");
    auto first = x.cbegin() + start;
    auto last = x.cbegin() + end;

    vector<double> vec(first, last);
    return vec;
}

double round_double(double value, int decimal_places) {
    const double multiplier = std::pow(10.0, decimal_places);
    return std::round(value * multiplier) / multiplier;
}

int next_2_power(int n) {
    int p = 1;
    if (n && !(n & (n - 1)))
        return n;
    else {
        while (p < n)
            p <<= 1;
        return p;
    }
}

vector<double> lth_diagonal(vector<vector<double>> matrix, int l) {
    /*
        Extracts the lth diagonal from the input matrix
    */
    vector<double> res;
    if (matrix.size() >= matrix[0].size()) {
        // more rows than columns
        int col_ind = l % matrix[0].size();
        for (int i = 0; i < int(matrix.size()); i++) {
            res.push_back(matrix[i][col_ind]);
            col_ind++;
            col_ind = col_ind % matrix[0].size();
        }
    } else {
        // more columns than rows
        int row_ind = (matrix.size() - l) % matrix.size();
        for (int i = 0; i < int(matrix[0].size()); i++) {
            res.push_back(matrix[row_ind][i]);
            row_ind++;
            row_ind = row_ind % matrix.size();
        }
    }
    return res;
}

void print_matrix(vector<vector<double>> m) {
    for (int i = 0; i < int(m.size()); i++) {
        for (int j = 0; j < int(m[0].size()); j++)
            std::cout << m[i][j] << " ";
        std::cout << std::endl;
    }
}

void print_vector(vector<double> v) {
    for (int i = 0; i < int(v.size()); i++)
        std::cout << v[i] << " ";
    std::cout << std::endl;
}

vector<double> double_vector(vector<double> vector){
    for (int i = 0; i < int(vector.size()); i++){
        vector.push_back(vector[i]);
    }
    return vector;
}

#endif //ETO_UTILS_H
