# Léopold Chappuis
# Aubin Vert


# Exercice 1

def palindrome(mot):
    mot = mot.lower()
    if len(mot) == 0:
        return True
    else:
        if mot[0] == mot[len(mot)-1]:     # On compare les deux lettres aux extrémités à chaque fois et si ça marche on continue
            return palindrome(mot[1:len(mot)-1])   # Si le mot tombe à 0 caractère tout a marché et c'est un palindrome
        else:
            return False

# Programme principal qui fait un appel à la fonction récursive
def palindrome_verif():
    mot = str(input("Veuillez rentrer un mot : "))

    if palindrome(mot) == True:
        print(f"Le mot '{mot}' est un palindrome")
    else:
        print(f"Le mot '{mot}' n'est pas un palindrome")

# Exercice 2

def crypter(chaine):
    new_chaine = ""   # On déclare une deuxième chaine qu'on va implémenter avec les nouvelles valeures
    for caractere in chaine:
        if caractere.isnumeric() == True:
            # Si on a un nombre alors on prend le nombre on lui ajoute 1 puis on l'ajoute à la nouvelle chaine
            nombre = int(caractere)
            nombre += 1
            nombre = str(nombre)
            new_chaine += nombre
        elif caractere.isalpha() == True:
            # Si c'est une lettre on prend le caractère dans la table ASCII on prend son indice on lui ajoute 1 puis
            # on le repasse en caractère et on l'ajoute à new_chaine
            lettre = ord(caractere)
            if lettre == 122: # Test sur le z miniscule
                lettre = 97
            elif lettre == 90: # Test sur le Z majuscule
                lettre = 65
            else:
                lettre += 1
            lettre=chr(lettre)
            new_chaine += lettre
        else:
            new_chaine += caractere  # Si juste c'est un caractère on le concatène, pas de traitement
    return new_chaine

# Exercice 3

def nb_min(password):
    counter = 0
    for car in password:
        if 96 < ord(car) < 123:
# On peut vérifier si c'est une minuscule en vérifiant que le caractère dans la table ASCII est un nombre compris entre a et z
            counter += 1
    return counter

def nb_maj(password):
    counter = 0
    for car in password:
        if 64 < ord(car) < 91:  # Même raisonnement qu'au dessus
            counter += 1
    return counter

def nb_alpha(password):
    counter = 0
    for caractere in password:
        if caractere.isalpha() == False :
            counter += 1
    return counter

def long_min(password):
    num_max = 0
    nb_seq = 0
    count = 0
    for car in password:
        if 96 < ord(car) < 123:   # On vérifie si c'est une miniscule
            count += 1   # Si oui on compte le nombre
        elif ord(car)>122 or ord(car)<97:    # Si c'est une majuscule fin de séquence, on regarde combien il y en a eu et on reset le compteur
            if count > num_max:
                num_max = count
            count = 0
            nb_seq += 1
        if nb_seq == 0:
            num_max = count   # S'il n'y a pas de majuscule on veut quand même une valeur
    if 96 < ord(password[len(password)-1]) <123:
        if count > num_max:
            num_max = count
    return num_max

def long_maj(password):
    num_max = 0
    nb_seq = 0
    count = 0
    for car in password:
        if  64 < ord(car) < 91:   # On vérifie si c'est une majuscule
            count += 1    # Si oui on compte le nombre
        elif ord(car)>90 or ord(car)<65:   # Si c'est une miniscule fin de séquence, on regarde combien il y en a eu et on reset le compteur
            if count > num_max:
                num_max =count
            count = 0
            nb_seq += 1
        if nb_seq == 0:
            num_max = count   # S'il n'y a pas de miniscules on veut quand meme une valeur dans notre tableau
    if 64 < ord(password[len(password)-1]) <91:
        if count > num_max:
            num_max = count
    return num_max

def score(password):
    nbcar = len(password)
    # Appel de toutes les fonctions définies au dessus
    return (4*(nbcar) + ((nbcar-nb_maj(password))*2) + (nbcar-nb_min(password)*3) + (nb_alpha(password)*5) - (long_min(password)*2) - (long_maj(password)*3))

# Programme principal (mis dans une fonction pour être plus simple d'appel)

def mdp():
    password = str(input("Veuillez rentrer un mot de passe : "))
    level = score(password)
    if level<20:
        print("La sécurité de votre mot de passe est très faible")
    elif level<40:
        print("La sécurité de votre mot de passe est faible")
    elif level<80:
        print("La sécurité de votre mot de passe est forte")
    else:
        print("La sécurité de votre mot de passe est très forte")



# Recap des exercices

def main():
    test1 = str(input("Voulez vous éxécuter l'exercie 1 ? [y/n] : "))
    test1 = test1.lower()
    if test1 != "y" and test1 != "n":
        verif = False
        while verif == False:
            test1 = str(input("Veuillez rentrer y ou n : "))
            if test1 == "y" or test1 == "n":
                verif = True
    if test1 == "y":
        palindrome_verif()

    test2 = str(input("Voulez vous éxécuter l'exercice 2 ? [y/n] : "))
    test2 = test2.lower()
    if test2 != "y" and test2 != "n":
        verif = False
        while verif == False:
            test2 = str(input("Veuillez rentrer y ou n : "))
            if test2 == "y" or test2 == "n":
                verif = True
    if test2 == "y":
        chaine = str(input("Veuillez rentrer une chaine : "))
        new_chaine = crypter(chaine)
        print(new_chaine)


    test3 = str(input("Voulez vous éxécuter l'exercice 3 ? [y/n] : "))
    test3 = test3.lower()
    if test3 != "y" and test3 != "n":
        verif = False
        while verif == False:
            test3 = str(input("Veuillez rentrer y ou n : "))
            if test3 == "y" or test2 == "n":
                verif = True
    if test3 == "y":
        mdp()

    print()
    print()
    print("======Fin du TP2======")
