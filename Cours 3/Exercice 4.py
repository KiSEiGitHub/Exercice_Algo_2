from math import pi


def volume_masse_elip(a, b, c, x):
    v = 4 / 3 * pi * a * b * c
    m = v * x
    return v, m


def main():
    volume, masse = volume_masse_elip(10, 2, 5, 2)
    print(f"Volume = {round(volume, 2)}")
    print(f"Masse = {round(masse, 2)}")



if __name__ == '__main__':
    main()