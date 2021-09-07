def main():
    s = input("Entrer un mot: ")
    ss = input("Entrer un autre mot: ")

    if len(s) > len(ss):
        print(f"{s} est plus grand que {ss}")
    else:
        print(f"{ss} est plus grand que {s}")

if __name__ == '__main__':
    main()