from random import *
#Exercice 1
class Rectangle:
    def __init__(self, longueur, largeur):
         self.__longueur = longueur
         self.__largeur = largeur

    def setLargeur(self, largeur):
        if type(self.__largeur) == float:
            self.__largeur = largeur
        else:
            raise TypeError("La largeur doit être de type float ")

    def setLongueur(self, longueur):
        if type(self.__longueur) == float:
            self.__longueur = longueur
        else:
            raise TypeError("La longueur doit être de type float ")

    def getLargeur(self):
        return self.__largeur

    def getLongueur(self):
        return self.__longueur

    def perimetre(self):
        return (2*self.__longueur + 2*self.__largeur)

    def aire(self):
        return (self.__longueur*self.__largeur)

    def isBigger(self, rectangle_other):
        if rectangle_other.aire() > self.aire():
            return rectangle_other
        elif rectangle_other.aire() == self.aire():
            return rectangle_other # ce sont les même peu importe
        else:
            return self

    def detail(self):
        is_carre = False
        if self.__longueur == self.__largeur:
            is_carre = True
        if is_carre:
            print(f"Longueur : [{self.__longueur}] - Largeur : [{self.__largeur} - Périmètre : [{self.perimetre()}] - Aire : [{self.aire()}] - C'est un carré")
        else:
            print(f"Longueur : [{self.__longueur}] - Largeur : [{self.__largeur} - Périmètre : [{self.perimetre()}] - Aire : [{self.aire()}] - Ce n'est pas un carré")

# def main1():


#Exo 2





# Exercice 3

class Pokemon:
    def __init__(self, nom, np, atk):
        self.__nom = nom
        self.__np = np
        self.__atk = atk

    @property
    def getNom(self):
        return self.__nom

    @property
    def getNp(self):
        return self.__np

    @property
    def getAtk(self):
        return self.__atk

    @getNom.setter
    def Nom(self, nom):
        self.__nom = nom

    @getNp.setter
    def Np(self, np):
        if np < 0:
            raise ValueError
        else:
            self.__np = np

    @getAtk.setter
    def Atk(self, atk):
        self.__atk = atk

    def is_dead(self):
        if self.__np == 0:
            return True
        else:
            return False

    def attaquer(self, Pokemon_p):
        hp_pok2 = Pokemon_p.getNp
        rand = random()
        atk_2 = rand * Pokemon_p.getAtk
        hp_pok2 -= atk_2
        if hp_pok2<0:
            hp_pok2 = 0
        Pokemon_p.Np = hp_pok2

    def combat(self, Pokemon_p):
        Pokemon_p.attaquer(self)
        self.attaquer(Pokemon_p)

    def detail(self):
        return self.__nom, self.__np, self.__atk

class PokemonFeu(Pokemon):
    def __init__(self, nom, np, atk):
        super().__init__(nom, np, atk)


    def attaquer(self, Pokemon_p):
        if isinstance(Pokemon_p, PokemonPlante) == True:
            hp_pok2 = Pokemon_p.getNp
            rand = random()
            atk_2 = 2 * rand * Pokemon_p.getAtk
            hp_pok2 -= atk_2
            if hp_pok2 < 0:
                hp_pok2 = 0
            Pokemon_p.Np = hp_pok2

        elif isinstance(Pokemon_p, Pokemon):
            hp_pok2 = Pokemon_p.getNp
            rand = random()
            atk_2 = rand * Pokemon_p.getAtk
            hp_pok2 -= atk_2
            if hp_pok2 < 0:
                hp_pok2 = 0
            Pokemon_p.Np = hp_pok2
        elif isinstance(Pokemon_p, PokemonEau) or isinstance(Pokemon_p, PokemonFeu):
            hp_pok2 = Pokemon_p.getNp
            rand = random()
            atk_2 = 0.5*rand * Pokemon_p.getAtk
            hp_pok2 -= atk_2
            if hp_pok2 < 0:
                hp_pok2 = 0
            Pokemon_p.Np = hp_pok2

class PokemonEau(Pokemon):
    def __init__(self, nom, np, atk):
        super().__init__(nom, np, atk)

    def attaquer(self, Pokemon_p):
        if isinstance(Pokemon_p, PokemonFeu) == True:
            hp_pok2 = Pokemon_p.getNp
            rand = random()
            atk_2 = 2 * rand * Pokemon_p.getAtk
            hp_pok2 -= atk_2
            if hp_pok2 < 0:
                hp_pok2 = 0
            Pokemon_p.Np = hp_pok2

        elif isinstance(Pokemon_p, Pokemon):
            hp_pok2 = Pokemon_p.getNp
            rand = random()
            atk_2 = rand * Pokemon_p.getAtk
            hp_pok2 -= atk_2
            if hp_pok2 < 0:
                hp_pok2 = 0
            Pokemon_p.Np = hp_pok2

        elif isinstance(Pokemon_p, PokemonEau) or isinstance(Pokemon_p, PokemonPlante):
            hp_pok2 = Pokemon_p.getNp
            rand = random()
            atk_2 = 0.5*rand * Pokemon_p.getAtk
            hp_pok2 -= atk_2
            if hp_pok2 < 0:
                hp_pok2 = 0
            Pokemon_p.Np = hp_pok2

class PokemonPlante(Pokemon):
    def __init__(self, nom, np, atk):
        super().__init__(nom, np, atk)

    def attaquer(self, Pokemon_p):
        if isinstance(Pokemon_p, PokemonEau) == True:
            hp_pok2 = Pokemon_p.getNp
            rand = random()
            atk_2 = 2 * rand * Pokemon_p.getAtk
            hp_pok2 -= atk_2
            if hp_pok2 < 0:
                hp_pok2 = 0
            Pokemon_p.Np = hp_pok2

        elif isinstance(Pokemon_p, Pokemon):
            hp_pok2 = Pokemon_p.getNp
            rand = random()
            atk_2 = rand * Pokemon_p.getAtk
            hp_pok2 -= atk_2
            if hp_pok2 < 0:
                hp_pok2 = 0
            Pokemon_p.Np = hp_pok2
        elif isinstance(Pokemon_p, PokemonPlante) or isinstance(Pokemon_p, PokemonFeu):
            hp_pok2 = Pokemon_p.getNp
            rand = random()
            atk_2 = 0.5*rand * Pokemon_p.getAtk
            hp_pok2 -= atk_2
            if hp_pok2 < 0:
                hp_pok2 = 0
            Pokemon_p.Np = hp_pok2

def main():
    poke1 = PokemonPlante("Bulb", 100, 20)
    poke2 = PokemonFeu("DracoFeu", 100, 90)
    while poke1.getNp != 0 and poke2.getNp !=0:
        poke1.combat(poke2)
    if poke1.getNp != 0:
        print(f"Le pokémon {poke1.getNom} a gagné face à {poke2.getNom} et il lui restait {poke1.getNp} points de vie")
    else:
        print(f"Le pokémon {poke2.getNom} a gagné face à {poke1.getNom} et il lui restait {poke2.getNp} points de vie")

