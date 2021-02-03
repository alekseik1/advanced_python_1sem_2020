import pickle


data = {
    'a': [1, 2.0, 3, 4+6j, float("nan")],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

print(pickle.dumps(data))

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

