import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from math import *
import csv
import os

# Outil de vérification des entrées utilisateurs ( boolléens )

def verification(answer):
    answer = answer.lower()
    if answer != 'y' and answer != 'n':
        verif = False
        while verif == False:
            answer = str(input("Veuillez rentrer une valeur valide [y/n] : "))
            answer = answer.lower()
            if answer == 'y' or answer == 'n':
                verif = True
    return answer


# Exercice 1

def saisir():
    nb_add = int(input("Combien de candidats voulez-vous ajouter ? : "))
    NCINtab = []
    NOMtab = []
    PRENOMtab = []
    AGEtab = []
    dectab = []

    for i in range(nb_add):
        NCIN = int(input(f"Veuillez rentrer le NCIN du {i + 1}e candidat : "))
        NOM = str(input("Veuillez rentrer le Nom : "))
        PRENOM = str(input("Veuillez rentrer le Prénom : "))
        AGE = int(input(f"Veuillez rentrer l'Age de {NOM} {PRENOM} : "))
        dec = str(input(f"L'étudiant a-t-il été admis ? [y/n] : "))

        dec = verification(dec)
        if dec == "y":
            DECISION = "admis"
        else:
            dec = str(input("L'étudiant a-t-il été ajourné ? [y/n] : "))
            dec = verification(dec)
            if dec == "y":
                DECISION = "ajourné"
            else:
                DECISION = "refusé"

        NCINtab.append(NCIN)
        NOMtab.append(NOM)
        PRENOMtab.append(PRENOM)
        AGEtab.append(AGE)
        dectab.append(DECISION)
    NCIN = pd.Series(NCINtab)
    NOMs = pd.Series(NOMtab)
    PRENOMs = pd.Series(PRENOMtab)
    AGEs = pd.Series(AGEtab)
    DECs = pd.Series(dectab)

    Dataframe = pd.DataFrame({"NCIN": NCIN,
                              "NOM": NOMs,
                              "PRENOM": PRENOMs,
                              "AGE": AGEs,
                              "DECISION": DECs})

    Dataframe.to_csv('concours.txt', sep=';', index=False)

def admis():
    data = pd.read_csv('concours.txt', sep=';')
    new_data = data.loc[data.DECISION == "admis"]
    new_data.to_csv('admis.txt', sep=';', index=False)

def attente():
    data = pd.read_csv('admis.txt', sep=';')
    new_data = data.loc[data.AGE > 30]
    new_data.to_csv('attente.txt', sep=';', index=False)

def statistiques():
    data = pd.read_csv('concours.txt', sep=';')
    rows = len(data.axes[0])
    stats = data.DECISION.value_counts()
    try:
        st_admis = stats["admis"]
    except:
        st_admis = 0

    try:
        st_ajourne = stats["ajourné"]
    except:
        st_ajourne = 0

    try:
        st_refuse = stats["refusé"]
    except:
        st_refuse = 0

    st_admis = (st_admis / rows) * 100
    st_ajourne = (st_ajourne / rows) * 100
    st_refuse = (st_refuse / rows) * 100

    x = [st_admis, st_ajourne, st_refuse]
    plt.pie(x, labels=['Admis', 'Ajournés', 'Refusés'], normalize=True)
    plt.legend(bbox_to_anchor=(1, 1))
    plt.show()

def supprimer():
    data = pd.read_csv('admis.txt', sep=';')
    new_data = data.loc[data.AGE <= 30]
    new_data.to_csv('admis.txt', sep=';', index=False)

def principal():
    test0 = str(input("Voulez-vous ajouter des personnes au fichier concours ? [y/n] : "))
    test0 = verification(test0)
    val = True
    if test0 == 'n':
        try:
            data = pd.read_csv('concours.txt', sep=';')
            rows = len(data.axes[0])
            if rows == 0:
                val = False
        except:
            val = False
        if val == False:
            print("=====================================================")
            print("Aucune valeur dans ce fichier, veuillez en ajouter.")
            print()
            saisir()
    else:
        saisir()

    test = str(input("Voulez vous générer le fichier des personnes admises 'admis.txt' ? [y/n] : "))
    test = verification(test)
    if test == 'y':
        admis()

    test2 = str(input("Voulez vous générer le fichier des personnes en attentes 'attente.txt' ? [y/n] : "))
    test2 = verification(test2)
    if test2 == 'y':
        attente()

    test3 = str(input("Voulez vous générer les statistiques sur le concours ?[y/n] : "))
    test3 = verification(test3)
    if test3 == 'y':
        statistiques()

    test4 = str(input("Voulez vous supprimer les personnes en attentes du fichier des admis  ? [y/n] : "))
    test4 = verification(test4)
    if test4 == 'y':
        supprimer()


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


def saisirExo3():
    imcos = []
    x = []
    for i in range(5, -6, -1):
        x.append(i)
        imcos.append(cos(i))

    os.chdir(r"/")
    file1 = open('../math.csv', "r+")
    ecrire = csv.writer(file1)
    ecrire.writerow(x)
    ecrire.writerow(imcos)
    file1.close()

def lire():
    global x, imcos
    os.chdir(r"/")
    file1 = open('../math.csv', "r+")
    lire = csv.reader(file1)


    i = 0
    for line in lire:
        if len(line) != 0 and i<1:
            x = line
        if len(line) != 0 and i<3:
            imcos = line

        i += 1

    x = np.linspace(-2*pi, 2 * pi)
    y = np.cos(x)

    plt.xlim((-5), 5)
    plt.ylim(-1, 1)

    plt.plot(x, y)

    plt.show()

def main():

    test1 = str(input("Voulez vous éxécuter l'exercice 1 ? [y/n] : "))
    test1 = verification(test1)
    if test1 == 'y':
        principal()

    print("=======================================================")
    print("Fin de l'exercice 1 ")

    test2 = str(input("Voulez vous éxécuter l'exercice 2 ? [y/n] : "))
    test2 = verification(test2)
    if test2 == 'y':

        question1 = str(input("Voulez vous éxécuter la question 1 de l'exercice 2 ? [y/n] : "))
        question1 = verification(question1)
        if question1 == 'y':
            x0 = int(input("Veuillez rentrer un x0 : "))
            y0 = int(input("Veuillez rentrer un y0 : "))
            rayon = int(input("Veuillez rentrer un rayon : "))
            cercle(x0, y0, rayon)

        question2 = str(input("Voulez vous éxécuter la question 2 de l'exercice 2 ? [y/n] : "))
        question2 = verification(question2)
        if question2 == 'y':
            cercle2()

    print("=======================================================")
    print("Fin de l'exercice 2 ")

    test3 = str(input("Voulez vous éxécuter l'exercice 3 ? [y/n] : "))
    test3 = verification(test3)
    if test3 == 'y':
        saisirExo3()
        lire()
    print("=======================================================")
    print("Fin de l'exercice 3 ")