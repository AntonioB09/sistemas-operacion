class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self, other):
        return Pair(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

if __name__ == "__main__":
    a = Pair(3, 5)
    b = Pair(4, 5)

    method_name = 'a.sum(b)'
    print(eval(method_name))
