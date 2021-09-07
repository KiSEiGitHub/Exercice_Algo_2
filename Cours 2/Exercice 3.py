def main():
    pSeuil = 2.3
    vSeuil = 7.41

    pression = float(input("Pression: "))
    volume = float(input("Volume: "))

    if pression > pSeuil and volume > vSeuil:
        print('Arrêt immédiat')

    elif pression > pSeuil and volume < vSeuil:
        print('Augmenter le volume')

    elif pression < pSeuil and volume > vSeuil:
        print('Diminuer le volume')
    
    else: 
        print('Tout va bien')

if __name__ == '__main__':
    main()