def main():
    X = set('abcd')
    Y = set('sdbs')

    print(f"Ensemble initial de x: {X}")
    print(f"Ensemble initial de y: {Y}")

    print('-' * 50)

    print(f"Test d'appartenance de c dans x: {'c' in X}")
    print(f"Test d'appartenance de a dans y: {'a' in Y}")

    print('-' * 50)

    print(f"Ensemble de X - Y: {X - Y}")
    print(f"Ensemble de Y - X: {Y - X}")

    print('-' * 50)

    print(f"Union de X | Y : {X | Y}")

    print('-' * 50)

    print(f"Intersection de X & Y : {X & Y}")


if __name__ == '__main__':
    main()