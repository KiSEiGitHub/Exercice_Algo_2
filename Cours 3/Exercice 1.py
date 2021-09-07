def table(base, debut, fin, inc):

    while debut <= fin:
        print(f"{base} * {debut} = {base * debut}")
        debut += inc


def main():
    table(7, 1, 10, 1)


if __name__ == '__main__':
    main()