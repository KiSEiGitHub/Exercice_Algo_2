def somDiv(x):
    return sum(i for i in range(1, x + 1) if x % i == 0)


def estParfait(x, y):
    return x == y


def estPremier(x):
    return x == 1


def estChanceux(x):
    return all(estPremier(x + i + i ** 2) for i in range(x - 1))