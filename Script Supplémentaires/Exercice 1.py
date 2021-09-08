from math import pi


class ConeDroit:
    def __init__(self, rayon, hauteur):
        self.rayon = rayon
        self.hauteur = hauteur

    def volume(self):
        return 1 / 3 * pi * self.rayon ** 2 * self.hauteur


def main():
    rayon = 6
    hauteur = 18
    a = ConeDroit(rayon, hauteur)
    print(f"Rayon: {rayon}")
    print(f"hauteur: {hauteur}")
    print(f'Volume cone: {round(a.volume(), 2)}')


if __name__ == '__main__':
    main()