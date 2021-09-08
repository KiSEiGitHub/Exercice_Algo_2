def main():
    t = []

    print("Entrez prix")
    print("0 pour terminer")
    n = 1

    while n != 0:
        n = float(input(">> "))
        t.append(n)

    total = sum(t)
    TVA = float(input("TVA: "))

    formule = total + (total * TVA / 100)

    print(f'Prix TTC: {round(formule, 2)} €')

if __name__ == '__main__':
    main()