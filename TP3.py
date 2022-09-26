from math import *

from googlemaps import *


# Exercice 1

class Gmap:
    def coordgps(adress):
        gmaps = Client(key='AIzaSyBTeRxf61DWGHagCM2SOVupUhdo2POEkxE')
        geocode_result = gmaps.geocode(adress)
        lat = geocode_result[0]["geometry"]["location"]["lat"]
        lng = geocode_result[0]["geometry"]["location"]["lng"]
        return lat,lng

class Lieu():

    def __init__(self):
        self.nom = str(input("Veuillez rentrer un nom : "))
        self.adresse = str(input("Veuillez rentrer une adresse : "))

        coord = Gmap.coordgps(self.adresse)

        self.latitude = coord[0]
        self.longitude = coord[1]

    def detail(self):
        print(f"Le lieu {self.nom} est situé au {self.adresse} et\na pour Latitude {self.latitude} \n et pour Longitude {self.longitude}")






# Exercice 2

def property(f):
    def wrapper(self, nom, prenom, age, sexe):
        nom = str(nom)
        prenom = str(prenom)
        if type(age) !=  int:
            verif = False
            while verif ==False:
                try:
                    age = int(input(f"Veuillez rentrer une valeur valide pour l'age de {prenom} : "))
                    verif = True
                except:
                    print("Veuillez réessayer")
                    verif = False
        sexe = str(sexe)
        func = f(self, nom, prenom, age, sexe)
        return func
    return wrapper

class Personne:

    @property
    def __init__(self, nom, prenom, age, sexe):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.sexe = sexe

    def getName(self):
        return self.nom
    def getPrenom(self):
        return self.prenom
    def getAge(self):
        return self.age
    def getSexe(self):
        return self.sexe
    def sameLastName(self, Personne):
        if self.nom == Personne.getName():
            return True
        else:
            return False
    def oldest(self, Personne):
        if self.age > Personne.getAge():
            return self.prenom, self.nom
        else:
            return Personne.getPrenom(), Personne.getName()



# Exercice 3

def property1(f):
    def wrapper(self, a, b):
        if type(a) and type(b) != float:
            try:
                a = float(a)
                b = float(b)
            except:
                verifa = False
                verifb = False
                print("Valeur incorrecte \n ====================================== ")
                if type(a) == float:
                    while verifb == False:
                        try:
                            b= float(input("Veuillez rentrer une valeur correcte pour le nombre 1 : "))
                            verifb = True
                        except:
                            verifb = False

                if type(b) == float:
                    while verifa == False:
                        try:
                            b= float(input("Veuillez rentrer une valeur correcte pour le nombre 2 : "))
                            verifa = True
                        except:
                            verifa = False
        return f(self, a, b)
    return wrapper

class Point:

    def __init__(self):
        self.abs = 0
        self.ord = 0

    def getter(self):
        return self.abs, self.ord

    @property1
    def setter(self, abs, ord):
        self.abs = abs
        self.ord = ord

    def calculerDistance(self, p):
        coords = p.getter()
        abs2 = coords[0]
        ord2 = coords[1]
        nb1 = (abs2-self.abs)**2
        nb2 = (ord2-self.ord)**2
        return sqrt(nb1+nb2)

    def calculerMillieu(self, p):
        coords = p.getter()
        abs2 = coords[0]
        ord2 = coords[1]
        return (abs2+self.abs)/2, (ord2+self.ord)/2



def property2(f):  # Vérifier que ce qui est passé à setter et __init__ sont bien des objets Point
    def wrapper(self, pt1, pt2, pt3):
        if type(pt1) is Point == False: #Si la personne a rentré un tuple de 2 coord au lieu d'un objet point
            if type(pt1) is tuple and len(pt1) == 2:
                nb = pt1
                pt1 = Point
                pt1.setter(nb[0], nb[1])
            else:
                print("Veuillez renseigner des coordonnées valables pour le point 1 ")
                abs = input("Veuillez renseigner l'absice : ")
                ord = input("Veuillez renseigner l'ordonnée : ")
                pt1.setter(abs, ord)
        if type(pt2) is Point == False: #Si la personne a rentré un tuple de 2 coord au lieu d'un objet point
            if type(pt2) is tuple and len(pt2) == 2:
                nb = pt2
                pt2 = Point
                pt2.setter(nb[0], nb[1])
            else:
                print("Veuillez renseigner des coordonnées valables pour le point 2 ")
                abs = input("Veuillez renseigner l'absice : ")
                ord = input("Veuillez renseigner l'ordonnée : ")
                pt2.setter(abs, ord)
        if type(pt3) is Point == False:  # Si la personne a rentré un tuple de 2 coord au lieu d'un objet point
            if type(pt3) is tuple and len(pt3) == 2:
                nb = pt3
                pt3 = Point
                pt3.setter(nb[0], nb[1])
            else:
                print("Veuillez renseigner des coordonnées valables pour le point 3 ")
                abs = input("Veuillez renseigner l'absice : ")
                ord = input("Veuillez renseigner l'ordonnée : ")
                pt1.setter(abs, ord)
        return f(self, pt1, pt2, pt3)
    return wrapper

class TroisPoints():

    @property2
    def __init__(self, premier, deuxieme, troisieme):
        self.premier = premier
        self.deuxieme = deuxieme
        self.troisieme = troisieme

    def getter(self):
        tuple1 = self.premier.getter()
        tuple2 = self.deuxieme.getter()
        tuple3 = self.troisieme.getter()
        return (tuple1, tuple2, tuple3)

    @property2
    def setter(self, premier, deuxieme, troisieme):
        self.premier = premier
        self.deuxieme = deuxieme
        self.troisieme = troisieme

    def sontAlignes(self):
        AB = self.premier.calculerDistance(self.deuxieme)
        AC = self.premier.calculerDistance(self.troisieme)
        BC = self.deuxieme.calculerDistance(self.troisieme)
        if (AC+BC == AB) or (AB+BC == AC) or (AB+AC == BC):
            align = True
        else:
            align = False
        return align

    def estIsocele(self):
        AB = self.premier.calculerDistance(self.deuxieme)
        AC = self.premier.calculerDistance(self.troisieme)
        BC = self.deuxieme.calculerDistance(self.troisieme)
        if (AB == AC) or (AB==BC) or (AC==BC):
            iso = True
        else:
            iso = False
        return iso