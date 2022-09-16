#Exo1

import datetime

class Date_class:

    def __init__(self):

        self.date = datetime.date.today()
        self.jour = self.date.day
        self.mois = self.date.month
        self.annee = self.date.year
        self.mois_31 = [1, 3, 5, 7, 8, 10, 12]

    def __str__(self):
        return (f"{self.jour}/{self.mois}/{self.annee}")

    def get_date(self):
        print(f"{self.jour}/{self.mois}/{self.annee}")

    def set_date(self, jour, mois, annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def jourDuLendemain(self):

        if self.mois == 2 and self.jour == 28:
            self.mois += 1
            self.jour = 1

        elif self.mois in self.mois_31:
            if self.jour == 31:
                if self.mois == 12:
                    self.mois = 1
                    self.jour = 1
                    self.annee += 1
                else:
                    self.mois += 1
                    self.jour = 1
            else:
                self.jour += 1

        elif self.mois not in self.mois_31:
            if self.jour == 30:
                self.mois += 1
                self.jour = 1
            else:
                self.jour += 1
        return (f"{self.jour}/{self.mois}/{self.annee}")


my_date = Date_class()
my_date.set_date(31,12,2021)
mois_31 = [1, 3, 5, 7, 8, 10, 12]
n = 0
iterations = 0
for i in range(12):
    n += 1
    if n == 2:
        iterations = 28
    elif n in mois_31:
        iterations = 31
    else:
        iterations = 30
    for j in range(iterations):
        print(my_date.jourDuLendemain(), end=" ")
    print('\n')