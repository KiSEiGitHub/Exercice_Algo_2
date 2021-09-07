def main():
    n = int(input("Entrer un nombre entre 1 et 10: "))

    while not(1 <= n <= 10):
        n = int(input("Entrer un nombre entre 1 et 10: "))
    
    print(f"Vous avez rentrer: {n}")


if __name__ == '__main__':
    main()