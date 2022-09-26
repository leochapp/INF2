#Exo 1
def example():
    for i in range(1,10):
        for j in range(1,10 - i): print(" ",end="")
        for j in range(0,i): print(i,end="")
        for j in range(0,i-1): print(i,end="")
        print()

def pyramid():
    for i in range(1,10):
        for j in range(1,10 - i): print(" ",end="")
        for j in range(1,i): print(j,end="")
        print(i, end="")
        for j in range(i-1,0,-1): print(j,end="")
        print()

#Exo 2

def diviseurs(nombre1, nombre2):
    diviseurs_commun = []
    if nombre1>nombre2:
        for i in range(1, nombre2+1):
            if nombre1 % i == 0 and nombre2 % i == 0:
                diviseurs_commun.append(i)
    else:
        for i in range(1, nombre1+1):
            if nombre1 % i == 0 and nombre2 % i == 0:
                diviseurs_commun.append(i)

    print("==============  Liste des diviseurs communs  ==============")
    print()
    for i in range(len(diviseurs_commun)):
        print(diviseurs_commun[i])

#Exo 3

from math import *

def moyenne():
    nb = int(input("Veuillez entrer le nombre de données à saisir : "))
    Listenb = []
    for i in range(nb):
        Listenb.append(int(input(f"entrer la valeur {i+1} : ")))

    newListpos = []
    newListneg = []
    for y in range(len(Listenb)):
        if Listenb[y]>0:
            newListpos.append(Listenb[y])
        else:
            newListneg.append(Listenb[y])

    if len(newListpos) != 0:
        minpos = min(newListpos)
    else:
        minpos = +inf
    if len(newListneg) != 0:
        minneg = max(newListneg)
        valminneg = sqrt(minneg**2)
    else:
        valminneg = +inf
    valdef = 0

    if valminneg == minpos:
        valdef = minneg
    elif valminneg > minpos:
        valdef = minpos
    else:
        valdef = minneg

    print(f"La valeur la plus proche de zéro est {valdef}")

    if len(Listenb) >2:
        Listenb.sort() #Triage pour retirer les valeurs extrêmes
        Listenb.pop(nb - 1)
        Listenb.pop(0)
        moyenne = float(sum(Listenb)/len(Listenb))
        print(f"La moyenne est {moyenne}")
    else:
        print("On ne peut pas retirer les deux extrêmes car la liste est trop courte")
        moyenne = float(sum(Listenb) / len(Listenb))
        print(f"La moyenne est donc {moyenne}")

#Exo 4

def text():
    entered_text = str(input("veuillez entrer un texte"))

    nb_caract = len(entered_text)
    print(f"Il y a {nb_caract} caractère dans ce texte")


    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count_letter = 0
    for i in range(len(entered_text)):
        if entered_text[i].upper() in alphabet:
            count_letter = count_letter +1
    print(f"Il y a {count_letter} lettres dans ce texte")


    count_voyelles = 0
    voyelles = "AEIOUY"
    for i in range(len(entered_text)):
        if entered_text[i].upper() in voyelles:
            count_voyelles = count_voyelles +1
    print(f"Il y a {count_voyelles} voyelles dans ce texte")

    count_nb = 0
    nb = "0123456789"
    for i in range(len(entered_text)):
        if entered_text[i] in nb:
            count_nb = count_nb +1
    print(f"Il y a {count_nb} chiffres dans ce texte")

#Exo 5

def admissions(dico):
    admis={}
    non_admis={}

    for nom in dico:
        if dico[nom] > 10:
            admis[nom] = dico[nom]
        else:
            non_admis[nom] =dico[nom]


    notes_admis = []
    for nom in admis:
        notes_admis.append(admis[nom])

    print(admis)
    if notes_admis:
        print(f"La moyenne des admis est {sum(notes_admis)/len(notes_admis)}")
    else:
        print("Aucun élève n'a eu l'UV")

    notes_nadmis = []
    for nom in non_admis:
        notes_nadmis.append(non_admis[nom])

    print(non_admis)

    if notes_nadmis:
        print(f"La moyenne des non admis est {sum(notes_nadmis) / len(notes_nadmis)}")
    else:
        print("Aucun élève n'a été recalé")