import sys
import pickle
import pystan

st_code = sys.argv[1]
st_obj = sys.argv[2]

sm = pystan.StanModel(file=st_code)

with open(st_obj, "wb") as f:
    pickle.dump(sm, f)

print("done")


