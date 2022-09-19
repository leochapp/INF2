from math import *


def surface():
    rayon = float(input("Veuillez rentrer le rayon : "))
    return pi * (rayon ** 2)


def produit():
    nombre1 = int(input("Veuillez rentrer le premier nombre : "))
    nombre2 = int(input("Veuillez rentrer le deuxième nombre : "))
    if nombre1 * nombre2 == 0:
        return "produit nul"
    elif nombre1 * nombre2 < 0:
        return "negatif"
    else:
        return "positif"


def fact(nombre):
    fact=1
    for i in range(1,nombre+1):
        fact=fact*i
    print(fact)


def bisextile():
    annee = int(input("Veuillez rentrer une annee : "))
    if annee % 4 == 0 and annee % 100 != 0 and annee % 400 == 0:
        print("L'anneée est bisextile ")
    else:
        print("L'année n'est pas bisextile ")


def coord():
    x1 = int(input("Veuuillez rentrer la valeur de x1 "))
    y1 = int(input("Veuillez rentrer la valeur de y1"))
    x2 = int(input("Veuillez rentrer la valeur de x2"))
    y2 = int(input("Veuillez rentrer la valeur de y2"))

    print(f"La distance entre ces deux points est {sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)}")


def tri(tab):
    print(sorted(tab))


def tri2(tab):
    newtab = []
    while len(tab) != 0:
        mintab = min(tab)
        for i in range(len(tab)):
            if tab[i] == mintab:
                newtab.append(tab[i])
                tab.pop(i)
    print(newtab)




def tri3(tab):
    for i in range(len(tab)):
        for j in range(i, len(tab)):
            if tab[i]>tab[j]:
                nb = tab[i]
                tab[i]=tab[j]
                tab[j]=nb
    print(tab)



