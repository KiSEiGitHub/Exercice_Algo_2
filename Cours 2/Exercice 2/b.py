def main():
    s = input("mot: ")
    ss = input("mot: ")

    res = f"{s} est plus grand que {ss}" if len(s) > len(ss) else f"{ss} est plus grand que {s}"

    print(res)

if __name__ == '__main__':
    main()