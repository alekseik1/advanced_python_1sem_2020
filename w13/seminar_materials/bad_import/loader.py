import pickle
# from dumper import Point


with open("data.pickle", "rb") as f:
    p = pickle.load(f)
    print(p.__dict__)

