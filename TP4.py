#!/usr/bin/env python
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from math import *
import csv
import os


# Exercice 1

# def saisir():
#     nb_add = int(input("Combien de candidats voulez-vous ajouter ? : "))
#     file = open("concours.txt", "a")
#     for i in range(nb_add):
#         NCIM = int(input("Veuillez rentrer le NCIM : "))
#         NOM = str(input("Veuillez rentrer le Nom : "))
#         PRENOM = str(input("Veuillez rentrer le Prenom : "))
#         AGE = int(input(f"Veuillez rentrer l'Age de {NOM} {PRENOM} "))
#         dec = str(input(f"L'étudiant a-t-il été admis ? [y/n]"))
#
#         if dec != "y" or dec != "n":
#             test = False
#             while test == False:
#                 dec = str(input("L'étudiant a-t-il été admis ? [y/n] "))
#                 if dec == "n" or dec == "y":
#                     test = True
#         if dec == "y":
#             DECISION = "admis"
#         else:
#             dec = str(input("L'étudiant a-t-il été ajourné ? [y/n] "))
#             if dec != "y" or dec != "n":
#                 test = False
#                 while test == False:
#                     dec = str(input("L'étudiant a-t-il été ajourné ? [y/n] "))
#                     if dec == "n" or dec =="y":
#                         test=True
#             if dec == "y":
#                 DECISION = "ajourné"
#             else:
#                 DECISION = "refusé"
#
#         file.write(f"{NCIM};{NOM};{PRENOM};{AGE};{DECISION}")
#     file.close()
#
# def admis():
#     file1 = open("concours.txt", "r")
#     file2 = open("admis.txt", "")
#
#     lines = file1.readlines()
#     for line in lines:
#         if "admis" in line:
#             file2.write(line)
#     file1.close()
#     file2.close()
#
# def attente():
#     file1 = open("admis.txt", "r")
#     file2 = open("attente.txt", "a")
#     lines = file1.readlines()
#     tab_age = []
#     for line in lines: # Une ligne représente un candidat
#         age = ""
#         n = 0
#         for car in line:
#             if n == 3:
#                 age += car
#             if car == ";":
#                 n += 1
#         age = int(age[:(len(age)-1)])
#         tab_age.append(age)
#
#     for i in range(len(lines)):
#         n=0
#         string = ""
#         if tab_age[i]>=30:
#             for car in lines[i]:
#                 if car == ";":
#                     n += 1
#                 while n < 3:
#                     string += car
#         file2.write(string)
#
#     file1.close()
#     file2.close()
#
# def statistiques(dec):
#     if dec != "admis" or dec != "refusé" or dec != "ajourné":
#          print("Valeur incorrecte !")
#          test = False
#          while test == False:
#              dec = str(input("Veuillez rentrer soit 'admis', sot 'refusé' soit 'ajourné' pour consulter les statistiques"))
#              if dec == "admis" or dec == "refusé" or dec == "ajourné":
#                  test = True
#     file1 = open("concours.txt", "r")
#     lines = file1.readlines()
#     tot = len(lines)
#     nb_admis = 0
#     nb_refus = 0
#     nb_ajour = 0
#     for line in lines:
#         if "admis" in line:
#             nb_admis += 1
#         if "refusé" in line:
#             nb_refus += 1
#         if "ajourné" in line:
#             nb_ajour += 1
#
#     tabresult=[(nb_admis/tot)*100,(nb_refus/tot)*100,(nb_ajour/tot)*100]
#     matplotlib.figure(figsize=(8, 8))
#     matplotlib.pie(tabresult, labels=['Admis', 'Refusés', 'Ajournés'], normalize=True)
#     matplotlib.legend()
#     file1.close()
#
# def supprimer():
#     file1 = open("attente.txt", "r")
#     file2 = open("admis.txt", "r+")
#
#     lines = file1.readlines()
#     numbers = []
#     for i in range(len(lines)):
#         n = 0
#         string =""
#         for car in lines[i]:
#             if car == ";":
#                 n += 1
#                 if n == 1:
#                     numbers.append(string)
#                     break
#             if car == 0:
#                 string += car
#     for i in range


# Exercice 2 :

def cercle(x0, y0, rayon):
    r = rayon
    for i in range(10):
        dom = np.linspace(0, 2 * pi)
        x = x0 + np.cos(dom) * r
        y =y0 + np.sin(dom) * r

        r += rayon

        plt.plot(x, y)

    plt.show()


def cercle2():
    r = 0.5
    x0 = 4.5
    y0 = 17.5

    for i in range(1, 11):
        x0 -= 0.5
        y0 -= 1
        newx = x0
        newy = y0
        for x in range(i):
            dom = np.linspace(0, 2 * pi)
            x = newx + np.cos(dom) * r
            y = newy + np.sin(dom) * r

            plt.plot(x, y)
            newx += 1
    plt.show()


# Exercice 3 :


def saisir():
    imcos = []
    x = []
    for i in range(5, -6, -1):
        x.append(i)
        imcos.append(cos(i))

    os.chdir("C:\Users\Léo\Desktop\INF2")
    file1 = open('math.csv', "r+")
    ecrire = csv.writer(file1)
    ecrire.writerow(x)
    ecrire.writerow(imcos)
    file1.close()

def lire():
    os.chdir("C:\Users\Léo\Desktop\INF2")
    file1 = open('math.csv', "r+")
    lire = csv.reader(file1)

    # DEBUG
    print("lire")
    # DEBUG

    nblignes = len(lire)
    for i in range(nblignes):
        x = lire[i] # On récupère les deux tableau avec nos valeurs
        imcos = lire[i+1]

