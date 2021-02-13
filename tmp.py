import pystan
import numpy as np

sm = pystan.StanModel(file="./stan_models/linear_model_0.stan")

n = 3
x = np.linspace(0, 1, n)
y = 3*x

data = {"N":n, "x":x, "y":y}
fit = sm.sampling(data=data)

params = fit.stract()
W = params["w"]

print(W)
