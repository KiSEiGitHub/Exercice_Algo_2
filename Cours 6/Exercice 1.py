from math import sqrt


def trinome(a, b, c):
    delta = b ** 2 - 4 * a * c

    if delta > 0.0:
        racine_delta = sqrt(delta)
        return 2, (-b - racine_delta) / (2 * a), (-b + racine_delta) / (2 * a)
    elif delta < 0.0:
        return 0
    else:
        return 1, (-b / (2 * a))


def main():

    valeur_1 = trinome(1, -3, 2)
    valeur_2 = trinome(1, -2, 1)
    valeur_3 = trinome(1, 1, 1)

    print(f"{valeur_1 = }")
    print(f"{valeur_2 = }")
    print(f"{valeur_3 = }")

if __name__ == '__main__':
    main()