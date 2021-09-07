def main():
    dico = {
        'Au': {
            "Te / Tf": (2970, 1603),
            "Z / A": (79, 196.967)
        },
        'Ga': {
            'Te / Tf': (2237, 29.8),
            'Z / A': (21, 69.72)
        }
    }

    print(dico['Au']['Z / A'][0])

if __name__ == '__main__':
    main()