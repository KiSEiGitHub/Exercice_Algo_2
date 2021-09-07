from Cours5.Exercice1.parfait_chanceux_m import *


def main():
    n = int(input("n: "))
    somme_div = somDiv(n)
    print(f"Est parfait: {estParfait(somme_div, n)}")
    print(f"Est premier: {estPremier(somme_div)}")

    print(f"Somme div: {somDiv(n)}")
    print(f"Est parfait: {estParfait(somDiv(n), n)}")
    print(f"Est premier: {estPremier(somDiv(n))}")
    print(f"Est chanceux: {estChanceux(somDiv(n))}")

    parfaits, chanceux = [], []
    intervalle = range(2, 1001)

    for i in intervalle:
        if estParfait(somDiv(n), n):
            parfaits.append(i)
        if estChanceux(somDiv(n)):
            chanceux.append(i)

    print(f"Tableau parfait: {parfaits}")
    print(f"Tableau chanceux: {chanceux}")


if __name__ == '__main__':
    main()