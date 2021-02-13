data{
    int<lower=1> N;
    vector[N] x;
    vector[N] y;
}


parameters{
    real w;
}


model{

    w ~ normal(0,10);
    for (i in 1..m){
        y[i] ~ normal(w*x[i], 1)
    }
}