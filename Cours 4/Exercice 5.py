def main():
    t = [i + j for i in "abc" for j in "de"]
    print(t)

if __name__ == '__main__':
    main()