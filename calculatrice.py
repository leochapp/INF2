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
        self.geometry(geometrie)
        self.config(bg="grey", relief="solid",)


        # Frame1

        f1 = Frame(self, bg="blue")
        f1.pack(side=TOP, padx=5)
        bouton1 = Button(f1, text='Bouton 1')
        bouton1.grid(padx=10, pady=20)

        # Frame 2

        f2 = Frame(self, bg="yellow")
        f2.pack(side=BOTTOM, padx=5)
        labelF2 = Label(f2, text="Frame 2")
        labelF2.grid(row=0, column=1, columnspan=3, padx=10, pady=20)
        bouton2 = Button(f2, text='Bouton 2')
        bouton2.grid(row=1, column=1, columnspan=3, padx=10, pady=20)

        # variables :
        self.variable = ""

        self.boutonegal = Button(self, text="1", bg="cyan", borderwidth="2", command=self.egal)
        self.boutonegal.pack()


        self.bouton1 = Button(self, text="1", bg="cyan", borderwidth="2", command=self.add1)
        self.bouton1.pack()

        self.boutonquit = Button(self, text="Quitter", bg="cyan", borderwidth="2", command=self.quit)
        self.boutonquit.pack()

    def add1(self):
        self.variable += "1"

    def egal(self):
        self.variable = int(self.variable)




def main():
    fenetre = Fenetre()
    fenetre.mainloop()