class Vecteur2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vecteur2D(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vecteur: {self.x}, {self.y}"


def main():
    v1, v2 = Vecteur2D(1, 2), Vecteur2D(3, 4)
    print(v1)
    print(v2)

if __name__ == '__main__':
    main()