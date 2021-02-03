import pickle


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    p = Point(4, 5.6)
    with open("data.pickle", "wb") as f:
        pickle.dump(p, f)

