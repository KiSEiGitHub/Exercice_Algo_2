def pile(*args):
    p = []
    if not args:
        return p
    for elem in args:
        p.append(elem)
    return list(p)


def empile(p, a):
    p.append(a)


def depile(p):
    try:
        return p.pop()
    except:
        print("La pile est vide !")


def main():
    print(" Pile initiale ".center(50, '-'))
    lifo = pile(5, 8, 9)
    _extracted_from_main_4(lifo, '"Entree"', " Empilage ")
    empile(lifo, 11)
    _extracted_from_main_4(lifo, 'Entree"', " Depilages ")
    for _ in range(5):
        depile(lifo)
    print("lifo :", lifo)

def _extracted_from_main_4(lifo, arg1, arg2):
    print("lifo :", lifo, '\n')
    rien = input(arg1)
    print(arg2.center(50, '-'))


if __name__ == '__main__':
    main()