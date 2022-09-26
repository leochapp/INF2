# Exercice 1

def palindrome(mot):
    mot = mot.lower()
    if len(mot) == 0:
        return True
    else:
        if mot[0] == mot[len(mot)-1]:
            return palindrome(mot[1:len(mot)-1])
        else:
            return False

def palindrome_verif():
    mot=str(input("Veuillez rentrer un mot : "))

    if palindrome(mot) == True:
        print(f"Le mot '{mot}' est un palindrome")
    else:
        print(f"Le mot '{mot}' n'est pas un palindrome")

# Exercice 2

def crypter(ch):
    newch = ""
    for i in ch:
        if i.isnumeric() == True:
            nb = i+1
            nb = chr(nb)
            newch += nb
        if i.isalpha() == True:
            nb = ord(i)
            if nb == 122:
                nb = 97
            elif nb == 90:
                nb = 65
            else:
                nb += 1
            nb=chr(nb)
            newch += nb
        else:
            newch += i
    return newch

# Exercice 3

def nb_min(password):
    counter = 0
    for car in password:
        if 96<ord(car)<123: # On peut vérifier si c'est une minuscule en vérifiant que le caractère dans la table ASCII est un nombre compris entre a et z
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
    for car in password:
        if car.isalpha() == False :
            counter += 1
    return counter

def long_min(password):
    tab = []
    nb_seq = 0
    count = 0
    for car in password:
        if 96 < ord(car) < 123:
            count += 1
        if ord(car)>122 or ord(car)<97:
            tab.append(count)
            count = 0
            nb_seq += 1
    return max(tab)

def long_maj(password):
    tab = []
    nb_seq = 0
    count = 0
    for car in password:
        if  64 < ord(car) < 91:
            count += 1
        if ord(car)>90 or ord(car)<65:
            tab.append(count)
            count = 0
            nb_seq += 1
    return max(tab)

def score(password):
    nbcar = len(password)
    return (4*(nbcar) + ((nbcar-nb_maj(password))*2) + (nbcar-nb_min(password)*3) + (nb_alpha(password)*5) - (long_min(password)*2) - (long_maj(password)*3))

# Programme principal (mis dans une fonction pour être plus simple d'appel

def mdp():
    password = str(input("Veuillez renrter un mot de passe : "))
    level = score(password)
    if level<20:
        print("La sécurité de votre mot de passe est très faible")
    elif level<40:
        print("La sécurité de votre mot de passe est faible")
    elif level<80:
        print("La sécurité de votre mot de passe est forte")
    else:
        print("La sécurité de votre mot de passe est très forte")
