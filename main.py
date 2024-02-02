import fonction
import string
print("Ce programme va crypter ou décrypter un texte avec la méthode de César ou Enigma-César.")

#alphabet = list(string.ascii_lowercase)
choix_utilisateur = int(input('Choisir choix: \n "1": Cryptage avec la méthode César,\n "2": Cryptage avec la méthode Enigma-César,\n "3": Décryptage avec la méthode César,\n "4": Décryptage avec la méthode Enigma-César,\n '))

if choix_utilisateur == 1:

    # Cryptage avec la méthode de César
    clef_cesar = int(input("Donnez une nombre entier comme clef de cryptage: "))

    # Lecture du fichier 'texte.txt'
    texte_original = fonction.creer_liste_de_chaque_mot('texte.txt')

    #Créarion d'une liste pour le texte crypté
    texte_crypte = []

    # Cryptage avec la méthode de César
    for mot in texte_original:
        #Ajouter
        texte_crypte.append(fonction.cryptage_cesar(mot, clef_cesar))

    print('\n Texte original :\n', ' '.join(texte_original),"\n")
    print('Texte crypté avec la méthode de César:\n', ' '.join(texte_crypte),"\n")

elif choix_utilisateur == 2:
    # Cryptage avec la méthode Enigma-César
    clef_enigma = input('Entrer la clé séparé par des entiers séparés des virgules (ex: 1,2,3): \n')
    clef_enigma = list(map(lambda x: int(x), clef_enigma.split(',')))

    # Lecture du fichier 'texte.txt'
    texte_original = fonction.creer_liste_de_chaque_mot('texte.txt')

    #Cryptage avec la méthode Enigma César
    texte_crypte_enigma = []
    for mot in texte_original:
        texte_crypte_enigma.append(fonction.cryptage_enigma_cesar(mot, clef_enigma))

    print('\n Texte original :\n', ' '.join(texte_original),"\n")
    print('Texte crypté avec la méthode Enigma-César:\n', ' '.join(texte_crypte_enigma),"\n")

elif choix_utilisateur == 3:
    # Decryptage de la méthode César, la solution est 4
    clef_cesar = int(input("Donnez une nombre entier comme clef de cryptage: "))

    # Lecture du fichier 'texte.txt'
    texte_crypte = fonction.creer_liste_de_chaque_mot('texte_cesar.txt')

    # Décryptage du texte crypté avec la méthode de César
    texte_decrypte = []

    for mot in texte_crypte:
        #il suffit de prendre l'opposé de la clé: ici - césar
        texte_decrypte.append(fonction.cryptage_cesar(mot, - clef_cesar))
    
    print('\n Texte crypté :\n', ' '.join(texte_crypte),"\n")
    print('Texte decrypté avec la méthode de César:\n', ' '.join(texte_decrypte),"\n")

elif choix_utilisateur == 4:
    # Décryptage avec la méthode Enigma-César... Solution [3,7,10]
    clef_enigma = input('Entrer la clé séparé par des entiers séparés des virgules (ex: 1,2,3): \n')
    clef_enigma = list(map(lambda x: int(x), clef_enigma.split(',')))

    # Lecture du fichier 'texte.txt'
    texte_crypte_enigma = fonction.creer_liste_de_chaque_mot('texte_enigma.txt')

    #Decryptage du texte crypté avec la méthode Enigma César
    clef_enigma_decrypte = [-i for i in clef_enigma]
    texte_decrypte_enigma = []

    for mot in texte_crypte_enigma:
        texte_decrypte_enigma.append(fonction.cryptage_enigma_cesar(mot, clef_enigma_decrypte))

    print('\n Texte crypté :\n', ' '.join(texte_crypte_enigma),"\n")
    print('Texte décrypté avec la méthode Enigma-César:\n', ' '.join(texte_decrypte_enigma),"\n")

else:
    print('Le choix ne figure pas dans les options possible...')
