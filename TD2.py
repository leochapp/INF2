#Exo1

def somme_chiffre(nb):
    nb = str(nb)
    tab = []
    for i in range(len(nb)):
        tab.append(int(nb[i]))
    somme = sum(tab)
    return somme

def nombre_chiffre(nb):
    nb = str(nb)
    return len(nb)

def separe_nombre(nb):
    nb = str(nb)
    moitie = int(len(nb)/2)
    moitie1 = ''.join(nb[:moitie])
    moitie2 = ''.join(nb[moitie:])
    moitie1 = int(moitie1)
    moitie2 = int(moitie2)
    return moitie1, moitie2

def couicable(nombre):
    verif = True
    nombre = str(nombre)
    for i in range(len(nombre)):
        if int(nombre[i]) % 2 != 0:
            verif = False
    tuplepart = separe_nombre(nombre)
    part1 = tuplepart[0]
    part2 = tuplepart[1]
    if somme_chiffre(part1) != somme_chiffre(part2):
        verif = False

    return verif

def somme_chiffre2(nombre):
    nombre = str(nombre)
    if len(nombre) == 1:
        return int(nombre)
    else:
        nombre = str(nombre)
        max = (len(nombre)-1)
        val = str(int(nombre[max-1])+int(nombre[max]))
        nombre = nombre[:max-1] + val
        return somme_chiffre2(int(nombre))


nb = int(input("Veuillez rentrer votre nombre pour vérifier s'il estcouicable  : "))

if couicable(nb):
    print("Le nombre est couicable")
else:
    print("Le nombre n'est pas couicable")




#Exo2 // Carré Magique

from math import *

def somme_ligne(mat, i):
    somme = sum(mat[i])
    return somme

def somme_colone(mat, j):
    taille_matrice = len(mat[0])
    somme = 0
    for i in range(taille_matrice):
        somme += mat[i][j]
    return somme

def somme_diag1(mat):
    taille_matrice = len(mat[0])
    somme = 0
    for i in range(taille_matrice):
        somme += mat[i][i]
    return somme

def somme_diag2(mat):
    taille_matrice = len(mat[0])
    somme = 0
    n=0
    for i in range((taille_matrice-1), -1, -1):
        somme += mat[n][i]
        n += 1
    return somme

def magique(mat_c):

    veriff = False
    taille_matrice = len(mat_c[0])
    sommetotligne = 0
    sommetotcolone = 0
    for i in range(taille_matrice):
        sommetotligne += somme_ligne(mat_c, i)
        sommetotcolone += somme_colone(mat_c, i)
    sommetotcolone = sommetotcolone / taille_matrice
    sommetotligne = sommetotligne / taille_matrice

    if sommetotligne == sommetotcolone == somme_diag1(mat_c) == somme_diag2(mat_c):
        veriff = True

    return veriff

def carre_magique_normal(mat_c):
    verif = True

    taille_matrice = len(mat_c[0])
    nombrelst = []
    for i in range(taille_matrice):
        for j in range(taille_matrice):
            nombrelst.append(mat_c[i][j])
    nombrelst.sort()
    nb_max = max(nombrelst)
    if sqrt(nb_max) != float(taille_matrice):
        verif = False
    else:
        for h in range(nb_max):
            if nombrelst[h] != h+1:
                verif = False

    return verif

def affiche_test_cm(*args):
    indice = 0
    for mat in args:
        indice += 1

        if magique(mat):
            print(f"La matrice {indice} est magique", end=' ')
            if carre_magique_normal(mat):
                print(f"et elle est également normale")
            else:
                print("et elle n'est pas normale ")
        else:
            print(f"La matrice {indice} n'est pas normale")