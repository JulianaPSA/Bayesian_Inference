data{
    int<lower=1> D;
    int<lower=1> N;
    matrix[N,D] X;
    vector[N] y;
}

parameters{
    vector[D] w;
}

model{
    w ~ multi_normal(rep_vector(0, D), diag_matrix(rep_vector(10,D)));
    for (i in 1:N){
        y[i] ~ normal(X[i]*w, 1);
    }
}