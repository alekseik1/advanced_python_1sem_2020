import pickle

f = open('1.txt', 'w')
try:
    pickle.dumps(f)
finally:
    f.close()

