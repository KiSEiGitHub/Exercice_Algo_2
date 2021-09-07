from math import sin


def main():
    for i in range(-3, 3):
        try:
            print(round(sin(i) / i, 4))
        except ZeroDivisionError:
            print("Peut pas diviser par 0")


if __name__ == '__main__':
    main()