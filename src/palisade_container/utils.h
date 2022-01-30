//
// Created by atkinswsl on 1/16/22.
//

#ifndef ETO_UTILS_H
#define ETO_UTILS_H

vector<double> splice_vector(vector<double> x, int start, int end){
    if (start < 0){
        throw std::invalid_argument("Received a start value less than 0.");
    }
    if (end > int(x.size())){
        throw invalid_argument("Received an end value greater than the size of the input vector");
    }
    auto first = x.cbegin() + start;
    auto last = x.cbegin() + end;

    vector<double> vec(first, last);
    return vec;
}

double round_double(double value, int decimal_places){
    const double multiplier = std::pow(10.0, decimal_places);
    return std::ceil(value * multiplier) / multiplier;
}

int next_2_power(int n){
    int p = 1;
    if (n && !(n & (n - 1))){
        return n;
    }
    else {
        while (p < n)
            p <<= 1;
        return p;
    }
}

#endif //ETO_UTILS_H
