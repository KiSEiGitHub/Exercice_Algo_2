from math import sqrt

def n_check(x):
    if x > 0:
        print(f"Racine carré de {x} = {round(sqrt(x), 2)}")
    else:
        print("Erreur")

def main():
    n = float(input("Saisir un flottant: "))
    n_check(n)

if __name__ == '__main__':
    main()