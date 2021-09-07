def somme(x):
    return sum(x)


def main():
    t = [int(input("Entrer nombre: ")) for _ in range(3)]
    print(sum(t))

if __name__ == '__main__':
    main()