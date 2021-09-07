def compterMots(texte):
    dict = {}
    listeMots = texte.split()
    for mot in listeMots:
        if mot in dict:
            dict[mot] = dict[mot] + 1
    else:
        dict[mot] = 1
    return dict


def main():
    res = compterMots("Ala Met Asn Glu Met Cys Asn Glu Hou Ala Met Gli Asn Asn")
    for c in res.keys():
        print(c, "-->", res[c])


if __name__ == '__main__':
    main()