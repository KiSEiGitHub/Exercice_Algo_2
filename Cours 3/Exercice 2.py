from math import pi

def cube(x):
    return x ** 3

def volumeSphere(r):
    return (4 / 3) * pi * r ** 3

def main():
    volume = cube(2)
    print(f"Volume sphère = {round(volumeSphere(volume), 2)} cm3")


if __name__ == '__main__':
    main()