from tkinter import *
from tkinter.messagebox import showinfo


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



        # Génération des boutons

        self.bouton1 = Button(self,height = 3, width = 5, text='1',bg="cyan", borderwidth=2)
        self.bouton1.pack()
        self.bouton1.place(x=0, y=0)

        self.bouton2 = Button(self, height = 3, width = 5,text='2', bg="cyan", borderwidth=2)
        self.bouton2.pack()
        self.bouton2.place(x=6, y=0)

        self.bouton3 = Button(self, height = 3, width = 5,text='3', bg="cyan", borderwidth=2)
        self.bouton3.pack()
        self.bouton3.place(x=12, y=0)
        self.bouton4 = Button(self, height = 3, width = 5,text='4', bg="cyan", borderwidth=2)
        self.bouton4.pack()
        self.bouton5 = Button(self, height = 3, width = 5,text='5', bg="cyan", borderwidth=2)
        self.bouton5.pack()
        self.bouton6 = Button(self, height = 3, width = 5,text='6', bg="cyan", borderwidth=2)
        self.bouton6.pack()
        self.bouton7 = Button(self, height = 3, width = 5,text='7', bg="cyan", borderwidth=2)
        self.bouton7.pack()
        self.bouton8 = Button(self, height = 3, width = 5,text='8', bg="cyan", borderwidth=2)
        self.bouton8.pack()
        self.bouton9 = Button(self, height = 3, width = 5,text='9', bg="cyan", borderwidth=2)
        self.bouton9.pack()
        self.bouton_eg = Button(self, height = 3, width = 5,text='=', bg="red", borderwidth=2)
        self.bouton_eg.pack()
        self.bouton_add = Button(self, height = 3, width = 5,text="+", bg="yellow", borderwidth=2)
        self.bouton_add.pack()
        self.bouton_min = Button(self, height = 3, width = 5,text="-", bg="yellow", borderwidth=2)
        self.bouton_min.pack()
        self.bouton_div = Button(self, height = 3, width = 5,text="/", bg="yellow", borderwidth=2)
        self.bouton_div.pack()
        self.bouton_mult = Button(self, height = 3, width = 5,text="*", bg="yellow", borderwidth=2)
        self.bouton_mult.pack()


        self.boutonquit = Button(self, text="Quitter", bg="cyan", borderwidth="2", command=self.quit)
        self.boutonquit.pack()






def main():
    fenetre = Fenetre()

    fenetre.mainloop()