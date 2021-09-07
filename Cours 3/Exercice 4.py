from math import pi


def volume_masse_elip(a, b, c):
    return 4 / 3 * pi * a * b * c


def main():
    volume = volume_masse_elip(10, 5, 2)
    print(f"Volume = {round(volume, 2)}")


if __name__ == '__main__':
    main()