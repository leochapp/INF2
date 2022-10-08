from tkinter import *


class Fenetre(Tk):

    def __init__(self):
        Tk.__init__(self)

        # Positionne l'écran au millieu

        ecran_x = self.winfo_screenwidth()
        ecran_y = self.winfo_screenheight()
        # Dimensions de la fenêtre
        fenetre_x = 350
        fenetre_y = 500
        pos_x = ecran_x // 2 - fenetre_x // 2
        pos_y = ecran_y // 2 - fenetre_y // 2
        geometrie = f"{fenetre_x}x{fenetre_y}+{pos_x}+{pos_y}"
        self.resizable(width=False, height=False)
        self.geometry(geometrie)
        self.config(bg="grey", relief="solid",)


        # variables :

        # self.boutonValider = Button(self, text='=', command=self.valider)

        # self.labelValider = Label(self.boutonValider, text="Valider")


        self.bouton1 = Button(self, text="1", bg="cyan", borderwidth="2")
        self.bouton1.pack()

        self.boutonquit = Button(self, text="Quitter", bg="cyan", borderwidth="2", command=self.quit)
        self.boutonquit.pack()

        self.bouton2 = Button(self, text="2",bg="cyan", borderwidth="2")




    # boutonInit = Button(text=' Initialiser',command=initialiser)
    # boutonInit.pack()




    def add(self, a, b):
        return a+b

    def sous(self, a, b):
        return a-b

    def mult(self, a, b):
        return a*b

    def div(self, a, b):
        return a/b




def main():
    fenetre = Fenetre()
    fenetre.mainloop()