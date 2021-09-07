def somme(x):
    return sum(x)

def main():
    t = [int(input("Entrer nombre: ")) for _ in range(10)]
    s = somme(t)
    print(f"Somme = {s}")


if __name__ == '__main__':
    main()