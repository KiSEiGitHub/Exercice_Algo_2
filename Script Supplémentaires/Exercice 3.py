def main():
    nb_supp_100 = []
    t = []
    n = 1

    print("Entrer nombres")
    while n != 0:
        n = int(input(">> "))
        if n >= 100:
            nb_supp_100.append(n)
            t.append(n)
        t.append(n)

    print(f'Nombre au dessus de 100: {len(nb_supp_100)}')
    print(f'Somme: {sum(t)}')

if __name__ == '__main__':
    main()