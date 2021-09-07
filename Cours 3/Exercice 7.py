def unDictionnaire(**kwargs):
    return kwargs

def main():
    print(unDictionnaire(a = 2, b = 34))

    mot = {
        'd': 85,
        'e': 24,
        'f': 2
    }

    print(unDictionnaire(**mot))

if __name__ == '__main__':
    main()