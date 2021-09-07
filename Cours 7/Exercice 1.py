class MaClasse:
    x = 23
    y = x + 5

    def __init__(self):
        self.z = 42

    @staticmethod
    def affiche():
        print(f"y = {MaClasse.y}")


def main():
    t = MaClasse()
    t.affiche()


if __name__ == '__main__':
    main()