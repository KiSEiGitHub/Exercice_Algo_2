def main():
    a = 0
    b = 10

    while a < b:
        a += 1
        print(f"a: {a}")

    while b > 0:
        if b % 2 == 1:
            print(f"b: {b}")
        b -= 1

if __name__ == '__main__':
    main()