
class Sommet:
    counter = 0


    def __init__(self, id):
        self.__id = id
        Sommet.counter += 1

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def __str__(self):
        return self.__id

    def getNbSommets(self):
        return Sommet.counter

    def __del__(self):
        Sommet.counter -=1
        self.__id.clear()

    def __hash__(self):
