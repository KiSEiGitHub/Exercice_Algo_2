def maFonction(x):
        return 2 * x **3 + x - 5

def tabuler(fonction, borneInf, borneSup, nbPas):
    h = (borneSup - borneInf) / float(nbPas)

    while borneInf < borneSup:
        print(f"{borneInf, fonction}")
        borneInf += h

def main():
    mafonction = maFonction(5)
    a = int(input("Borne inf: "))
    b = int(input("Borne Supp: "))
    while a > b:
        b = int(input("Borne supp: "))

    tabuler(mafonction, a, b, 10)


if __name__ == '__main__':
    main()