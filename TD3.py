#Exo1


class Date:

    def __init__(self, jour, mois, annee):

        self.__jour = jour
        self.__mois = mois
        self.__annee = annee

    def __str__(self):
        return f"[{self.__jour}/{self.__mois}/{self.__annee}]"

    def setter(self, jour, mois, annee):

        mois31 = [1, 3, 5, 7, 8, 10, 12]

        if 0>jour or jour>31 or mois <0 or mois>12 or annee <0:
            raise ValueError

        if mois not in mois31 and jour == 31:
            raise ValueError


        self.__jour = jour
        self.__mois = mois
        self.__annee = annee

    def getter(self):
        return self.__jour, self.__mois, self.__annee

    def jourDuLendemain(self):

        mois31 = [1,3,5,7,8,10,12]

        jourlen = self.__jour
        moislen = self.__mois
        anneelen = self.__annee


        if self.__jour == 30 and self.__mois not in mois31:
            jourlen = 1
            moislen += 1
        elif self.__jour == 31:
            jourlen = 1
            if self.__mois == 12:
                moislen = 1
                anneelen += 1
            else:
                moislen += 1
        else:
            jourlen += 1

        if self.__mois == 2 and self.__jour == 28:
            jourlen = 1
            moislen = 3


        return jourlen, moislen, anneelen

def principal():
    date = Date(1,1,2022)
    mois31 = [1, 3, 5, 7, 8, 10, 12]

    for mois in range(12):
        verif = date.getter()

        if verif[1] == 2:
            for jour in range(28):
                print(date, end='  ')
                lendemain = date.jourDuLendemain()
                date.setter(lendemain[0], lendemain[1], lendemain[2])

        elif verif[1] in mois31:
            for jours in range(31):
                print(date, end ='  ')

                lendemain = date.jourDuLendemain()
                date.setter(lendemain[0],lendemain[1],lendemain[2])

        else:
            for jours in range(30):
                print(date, end='  ')
                lendemain = date.jourDuLendemain()
                date.setter(lendemain[0], lendemain[1], lendemain[2])
        print()



# Exo2

class Horaire:

    def __init__(self, H, m):
        self.__Heure = H
        self.__minutes = m

    def getter(self):
        return self.__Heure, self.__minutes

    def setter(self,H, m):
        if H>24 or H<0 or m>60 or m<0:
            raise ValueError
        self.__Heure = H
        self.__minutes = m

    def __add__(self, duree):
        dur = duree.getterduree()
        durH = dur[0]
        durM = dur[1]
        hohH = self.__Heure
        hohM = self.__minutes
        totM = 0
        totH = 0
        if durM + hohM > 60:
            totM = durM +hohM -60
            hohH += 1
        else:
            totM = durM + hohM

        if hohH + durH > 23:
            totH = hohH + durH -24
        else:
            totH = hohH + durH

        return totH, totM

class Duree:

    def __init__(self, H, m):
        self.__heuredur = H
        self.__mindur = m

    def getterduree(self):
        return self.__heuredur, self.__mindur

    def setter(self, H, m):
        if H<0 or m<0 or m>60:
            raise ValueError
        self.__heuredur = H
        self.__mindur = m

class Vol:

     def __init__(self, nom, Hdepart, Mdepart, Hdurvol, Mdurvol):

         self.__nom = nom
         self.__Horaire = Horaire(Hdepart,Mdepart)
         self.__Duree = Duree(Hdurvol, Mdurvol)
         self.__Harrivee = self.__Horaire + self.__Duree

     def __str__(self):
         Hdepart = self.__Horaire.getter()[0]
         Mdepart = self.__Horaire.getter()[1]
         Hduree = self.__Duree.getterduree()[0]
         Mduree = self.__Duree.getterduree()[1]
         Harrivee = self.__Harrivee[0]
         Marrivee = self.__Harrivee[1]
         return f"L'Horaire de départ pour le vol {self.__nom} est {Hdepart}:{Mdepart}, La durée de vol est de {Hduree}:{Mduree} et l'arivée est prévue à {Harrivee}:{Marrivee} "

def principalVol():
    nom = str(input("Veuillez rentrer le nom de votre vol : "))
    Hdep = int(input("Veuillez rentrer votre Heure de départ : "))
    Mdep = int(input("Veuillez rentrer votre minute de départ : "))
    Hdur = int(input("Veuillez rentrer la durée de votre vol (heures) : "))
    Mdur = int(input("Veuillez rentrer la durée de votre vol (minutes) "))

    vol = Vol(nom,Hdep,Mdep,Hdur,Mdur)

    print(vol)