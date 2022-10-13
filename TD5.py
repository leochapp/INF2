# Exercice 1
import os.path
import PIL.Image

class Note:
    def __init__(self, titre):
        self.__titre = titre

    def setTitre(self, titre):
        self.__titre = titre

    def getTitre(self):
        return self.__titre

    def __str__(self):
        return  self.__titre

class Article(Note):

    def __init__(self,titre, texte):
        super().__init__(titre)
        self.__texte = texte

    def setTexte(self, texte):
        if isinstance(texte, str):
            self.__texte = texte
        else:
            raise TypeError

    def getTexte(self):
        return self.__texte

    def __str__(self):
        return f"{self.getTitre()} --- {self.__texte}"

class Image(Note):
    def __init__(self, titre, desc, chemin):
        super().__init__(titre)
        self.__desc = desc
        self.__chemin = chemin

    def setDesc(self, desc):
        if type(desc) == str:
            self.__desc = desc
        else:
            raise TypeError

    def setChemin(self, chemin):
        if os.path.isfile(chemin):
            self.__chemin = chemin
        else:
            raise ValueError

    def getDesc(self):
        return self.__desc

    def getChemin(self):
        return self.__chemin

    def __str__(self):
        img = PIL.Image.open(self.__chemin)
        return f"{self.getTitre()} --- {self.__desc} {img.show()}"

class Document(Note):
    def __init__(self,titre):
        super().__init__(titre)
        self.__liste = []

    def setTitre(self, titre):
        self.setTitre()

    def ajouter_note(self, note):
        if isinstance(note, Note):
            self.__liste.append(note)
        else:
            raise TypeError("Doit être une note")

    def supprimer_note(self, note):
        long = len(self.__liste)
        for i in range(long):
            if self.__liste[i] == note:
                self.__liste.pop(i)

    def getDocument(self):
        return self.getTitre(), self.__liste

    def __str__(self):
        long = len(self.__liste)
        for i in range(long):
            print(self.__liste[i])


# Bout de code pour simplifier le main()
def verif(answer):
    answer = answer.lower()
    if answer != 'y' and answer != 'n':
        verif = False
        while verif == False:
            answer = str(input("Voulez vous ajouter une note ? [y/n] : "))
            if answer == 'y' or answer =='n':
                verif = True
    return answer

def main2():
    redo = True

    while redo == True:
        redo = False
        test = verif(str(input("Voulez vous ajouter une note ? [y/n] : ")))
        if test == 'y':
            test1 = verif(str(input("Voulez vous ajouter un article ? [y/n] : ")))
            if test1 == 'y':
                title = str(input("Veuillez rentrer le titre de votre article : "))
                text = str(input("Veuille rentrer le texte de l'article : "))
                article = Article(title, text)
                test2 = verif(str(input("Voulez vous ajouter cette note à un document ? [y/n] : ")))
                if test2 == 'y':
                    title = str(input("Veuillez rentrer le titre du document : "))
                    doc = Document(title)
                    doc.ajouter_note(article)
            else:
                test = verif(str(input("Voulez vous ajouter une image ? ")))
                if test == 'y':
                    title = str(input("Veuillez rentrer le titre de votre image : "))
                    desc = str(input("Veuille rentrer la description de l'image : "))
                    path = str(input("Veuillez rentrer le chemin de l'image : "))
                    try:
                        image = Image(title, desc, path)
                    except:
                        print("chemin non valable ! ")
                    test2 = verif(str(input("Voulez vous ajouter cette image à un document ? [y/n] : ")))
                    if test2 == 'y':
                        title = str(input("Veuillez rentrer le titre du document : "))
                        doc = Document(title)
                        doc.ajouter_note(image)

            test = verif(str(input("Voulez vous accéder à un article d'un document ? [y/n] : ")))
            if test == "y":
                test2 = verif(str(input("Voulez vous visualiser toutes les notes ? [y/n] : ")))
                if test2 == "y":
                    print(doc)
                else:
                    name = str(input("Veuillez rentrer le titre de la note auquel vous voulez accéder : "))
                    liste = doc.getDocument()[1]
                    for i in range(len(liste)):
                        if liste[i].getTitre == name:
                            print(liste[i])
        question = verif(str(input("Voulez vous ajouter d'autres notes ? [y/n] : ")))
        if question == 'y':
            redo = True
        else:
            redo = False


def main():
    m1 = Note("Note 1")
    m2 = Article("Note2", "Article")
    m3 = Image("Note3","image au hasard", "./img.png")
    m4 = Article("Note4", "Autre article")
    m5 = Document("Gros doc")
    m5.ajouter_note(m1)
    m5.ajouter_note(m2)
    m5.ajouter_note(m3)
    m6 = Document("Gros Gros doc")
    m6.ajouter_note(m4)
    m6.ajouter_note(m5)
    print(m5)
    print(m6)