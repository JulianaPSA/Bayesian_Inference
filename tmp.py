import pystan
import numpy as np
import pickle

# sm = pystan.StanModel(file="./stan_models/linear_model_0.stan")
sm = pickle.load(open("./stan_models/linear_model_0.pic", "rb"))

n = 3
x = np.linspace(0, 1, n)
y = 3*x

data = {"N": n, "x": x, "y": y}
fit = sm.sampling(data=data)

params = fit.extract()
W = params["w"]

print(W.mean())
