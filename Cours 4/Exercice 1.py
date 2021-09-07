def main():
    liste = [17, 38, 10, 25, 72]
    print(f"Trier la liste: {sorted(liste)}")
    liste.append(12)
    print(f"Afficher l'élément 12 à la liste: {sorted(liste)}")
    reversed(liste)
    print(f"Renvesez et affichez la liste: {liste}")
    print(f"Afficher l'élément 17: {liste[0]}")
    liste.remove(38)
    print(f"Elever l'élément 38: {liste}")
    print(f"Afficher la sous liste du 2e au 3e élément: {liste[1:3]}")
    print(f"Afficher la sous liste du début au 2e élément: {liste[0:2]}")
    print(f"Afficher la sous liste du 3e élément à la fin de la liste: {liste[2:5]}")
    print(f"Afficher la sous liste complète de la liste: {liste[-1]}")

if __name__ == '__main__':
    main()