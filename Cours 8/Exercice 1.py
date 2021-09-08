class Rectangle:
    def __init__(self, longeur = 0, largeur = 0):
        self.longeur = longeur
        self.largeur = largeur
        self.nom = "Rectangle"

    def surface(self):
        return self.largeur * self.longeur

    def __str__(self):
        return f'{self.nom}: {self.largeur} {self.largeur} {self.surface()}'

class Carre(Rectangle):
    def __init__(self, cote = 10):
        self.nom = 'Carré'
        Rectangle.__init__(self, cote, cote)

def main():
    rectangle = Rectangle(12, 8)
    print(rectangle)

    carre = Carre()
    print(carre)


if __name__ == '__main__':
    main()