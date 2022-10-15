import tkinter.ttk
from functools import partial
from tkinter import *
from math import *



class Fenetre(Tk):

    def __init__(self):
        super().__init__()
        self.title("Calculatrice")
        label_welcome = Label(self, text="Calculatrice")
        label_welcome.pack( )

        ecran_x = self.winfo_screenwidth()
        ecran_y = self.winfo_screenheight()
        # Dimensions de la fenêtre
        fenetre_x = 280
        fenetre_y = 450
        pos_x = ecran_x // 2 - fenetre_x // 2
        pos_y = ecran_y // 2 - fenetre_y // 2
        geometrie = f"{fenetre_x}x{fenetre_y}+{pos_x}+{pos_y}"
        self.resizable(width=False, height=False)
        self.geometry(geometrie)
        self.config(bg="grey", relief="solid", )


        # Variable contenant le calcul

        top = Frame(self)
        bottom = Frame(self, bg="grey")
        top.pack(side=TOP, pady= 10)
        bottom.pack(side=BOTTOM, expand=False)

        # Génération de l'affichage des valeurs :

        #mise en place de l'historique
        self.historique = []
        self.counter = -1

        self.var = tkinter.StringVar()
        tkinter.Label(top, textvariable=self.var, width=30).pack()
        self.var.set("") # Variable contenant le calcul

        self.ang = tkinter.StringVar()
        self.ang.set("deg")



        # Génération des boutons

        col = 0
        row = 1
        for i in range(1,10): # <--  Génération boutons 1 à 9
            if col not in [0,1,2]:
                col = 0
            bouton = Button(bottom, height=3, width=5, text=str(i), bg="cyan", borderwidth=4, command=partial(self.addx, i), relief="raised")
            bouton.grid(sticky=W, padx=2, pady=2, row=row,column=col)
            col += 1
            if i == 3:
                row = 2
            if i == 6:
                row = 3


        bouton_par1 = Button(bottom, height=3, width=5, text='(', bg="cyan", borderwidth=4, command=self.par1,relief="raised")
        bouton_par1.grid(row=0, column=0, sticky=W, padx=2, pady=2)

        bouton_par2 = Button(bottom, height=3, width=5, text=')', bg="cyan", borderwidth=4, command=self.par2,relief="raised")
        bouton_par2.grid(row=0, column=1, sticky=W, padx=2, pady=2)

        bouton0 = Button(bottom, height=3, width=5, text='0', bg="cyan", borderwidth=4, command=partial(self.addx, 0), relief="raised")
        bouton0.grid(row=4,column=1, sticky=W, padx=2, pady=2)

        bouton_pi = Button(bottom, height=3, width=5, text='π', bg="cyan", borderwidth=4, command=self.pi, relief="raised")
        bouton_pi.grid(row=0,column=2, sticky=W, padx=2, pady=2)

        bouton_carr = Button(bottom, height=3, width=5, text='²', bg="cyan", borderwidth=4, command=self.carr, relief="raised")
        bouton_carr.grid(row=0, column=3, sticky=W, padx=2, pady=2)

        bouton_sqrt = Button(bottom, height=3, width=5, text='√', bg="cyan", borderwidth=4, command=self.sqrt, relief="raised")
        bouton_sqrt.grid(row=1, column=3, sticky=W, padx=2, pady=2)

        bouton_add = Button(bottom, height=3, width=5, text='+', bg="yellow", borderwidth=4, command=self.add, relief="raised")
        bouton_add.grid(row=1,column=4, sticky=W, padx=2, pady=2)

        bouton_min = Button(bottom, height=3, width=5, text='-', bg="yellow", borderwidth=4, command=self.min, relief="raised")
        bouton_min.grid(row=2,column=4, sticky=W, padx=2, pady=2)

        bouton_mult = Button(bottom, height=3, width=5, text='x', bg="yellow", borderwidth=4, command=self.mult, relief="raised")
        bouton_mult.grid(row=3,column=4, sticky=W, padx=2, pady=2)

        bouton_div = Button(bottom, height=3, width=5, text='/', bg="yellow", borderwidth=4, command=self.div, relief="raised")
        bouton_div.grid(row=4,column=4, sticky=W, padx=2, pady=2)

        bouton_egal = Button(bottom, height=3, width=5, text='=', bg="red", borderwidth=4, command=self.egal, relief="raised")
        bouton_egal.grid(row=4,column=0, sticky=W, padx=2, pady=2)

        bouton_pt = Button(bottom, height=3, width=5, text='.', bg="cyan", borderwidth=4, command=self.pt, relief="raised")
        bouton_pt.grid(row=4, column=2, sticky=W, padx=2, pady=2)

        bouton_clear = Button(bottom, height=3, width=5, text='C', bg="white", borderwidth=4, command=self.clear, relief="raised")
        bouton_clear.grid(column=4, row=0, sticky=W, padx=2, pady=2)

        bouton_sin = Button(bottom, height=3, width=5, text='sin', bg="cyan", borderwidth=4, command=self.sin, relief="raised")
        bouton_sin.grid(row=2, column=3, sticky=W, padx=2, pady=2)

        bouton_cos = Button(bottom, height=3, width=5, text='cos', bg="cyan", borderwidth=4, command=self.cos, relief="raised")
        bouton_cos.grid(row=3, column=3, sticky=W, padx=2, pady=2)

        bouton_tan = Button(bottom, height=3, width=5, text='tan', bg="cyan", borderwidth=4, command=self.tan, relief="raised")
        bouton_tan.grid(row=4, column=3, sticky=W, padx=2, pady=2)

        boutonquit = Button(text="quit", bg="cyan",height=2, width=4, borderwidth=4, command=self.destroy)
        boutonquit.pack(side=RIGHT, padx=1)

        bouton_historic = Button(text="H", bg="cyan", height=2, width=4, borderwidth=4, command=self.hist)
        bouton_historic.pack(side=RIGHT, padx=1)

        bouton_ang = Button(textvariable=self.ang, bg="cyan", height=2, width=4, borderwidth=4, command=self.angch)
        bouton_ang.pack(side=RIGHT, padx=1)

        bouton_recap = Button(text="R", bg="cyan", height=2, width=4, borderwidth=4, command=self.msg)
        bouton_recap.pack(side=LEFT, padx=1)

        bouton_SUPP = Button(text="<=", bg="cyan", height=2, width=4, borderwidth=4, command=self.supp)
        bouton_SUPP.pack(side=RIGHT, padx=1)






# Actions des boutons quand on clique dessus

    def supp(self):
        ch = self.var.get()
        i = len(ch) - 1
        self.var.set(ch[:i])

    def hist(self):
        if self.counter == -1:
            self.counter = len(self.historique) - 1
            self.var.set(self.historique[self.counter])
        else:
            self.counter -= 1
            self.var.set(self.historique[self.counter])

    def angch(self):
        if self.ang.get() == "deg":
            self.ang.set("rad")
        else:
            self.ang.set("deg")

    def sin(self):

        if "=" in self.var.get():
            ch = self.var.get()
            index = ch.find('=')
            ch = ch[index + 2:]
            self.var.set(ch)
            temp = "sin(" + self.var.get()
            self.var.set(temp)
        else:
            operator = ["x", "/", "+", "-"]
            ch = self.var.get()
            max = len(ch) - 1
            if max != -1:
                if ch[max] not in operator:
                    temp = self.var.get() + "xsin("
                    self.var.set(temp)
                else:
                    temp = self.var.get() + "sin("
                    self.var.set(temp)
            else:
                temp = self.var.get() + "sin("
                self.var.set(temp)

    def cos(self):

        if "=" in self.var.get():
            ch = self.var.get()
            index = ch.find('=')
            ch = ch[index + 2:]
            self.var.set(ch)
            temp = "cos(" + self.var.get()
            self.var.set(temp)
        else:
            operator = ["x", "/", "+", "-"]
            ch = self.var.get()
            max = len(ch) - 1
            if max != -1:
                if ch[max] not in operator:
                    temp = self.var.get() + "xcos("
                    self.var.set(temp)
                else:
                    temp = self.var.get() + "cos("
                    self.var.set(temp)
            else:
                temp = self.var.get() + "cos("
                self.var.set(temp)

    def tan(self):
        if "=" in self.var.get():
            ch = self.var.get()
            index = ch.find('=')
            ch = ch[index + 2:]
            self.var.set(ch)
            temp = "tan(" + self.var.get()
            self.var.set(temp)
        else:
            operator = ["x", "/", "+", "-"]
            ch = self.var.get()
            max = len(ch) - 1
            if max != -1:
                if ch[max] not in operator:
                    temp = self.var.get() + "xtan("
                    self.var.set(temp)
                else:
                    temp = self.var.get() + "tan("
                    self.var.set(temp)
            else:
                temp = self.var.get() + "tan("
                self.var.set(temp)

    def sqrt(self):
        if "=" in self.var.get():
            ch = self.var.get()
            index = ch.find('=')
            ch = ch[index + 2:]
            self.var.set(ch)
            temp = "√(" + self.var.get()
            self.var.set(temp)
        else:
            operator = ["x","/","+","-"]
            ch = self.var.get()
            max = len(ch)-1
            if max != -1:
                if ch[max] not in operator:
                    temp = self.var.get() + "x√("
                    self.var.set(temp)
                else:
                    temp = self.var.get() + "√("
                    self.var.set(temp)
            else:
                temp = self.var.get() + "√("
                self.var.set(temp)

    def carr(self):
        if "=" in self.var.get():
            ch = self.var.get()
            index = ch.find('=')
            ch = ch[index + 2:]
            self.var.set(ch)

        temp = self.var.get() + "²"
        self.var.set(temp)

    def pi(self):
        ch = self.var.get()
        max = len(ch) - 1
        try:
            n = ch[max]
        except:
            n = False

        if "=" in self.var.get():
            ch = self.var.get()
            index = ch.find('=')
            ch = ch[index + 2:] + "*pi"
            self.var.set(ch)
        elif n != False:
             if n.isdigit():
                 temp = self.var.get() + '*pi'
                 self.var.set(temp)
             else:
                 temp = self.var.get() + 'pi'
                 self.var.set(temp)
        else:
             temp = self.var.get() + 'pi'
             self.var.set(temp)

    def addx(self, x):
        x = str(x)
        if "=" in self.var.get():
            ch = self.var.get()
            index = ch.find('=')
            ch = ch[index+2:]
            self.var.set(ch)
        temp = self.var.get() + x
        self.var.set(temp)

    def add(self):
        if "=" in self.var.get():
            ch = self.var.get()
            index = ch.find('=')
            ch = ch[index+2:]
            self.var.set(ch)
        temp = self.var.get() + '+'
        self.var.set(temp)

    def min(self):
        if "=" in self.var.get():
            ch = self.var.get()
            index = ch.find('=')
            ch = ch[index+2:]
            self.var.set(ch)
        temp = self.var.get() + '-'
        self.var.set(temp)

    def mult(self):
        if "=" in self.var.get():
            ch = self.var.get()
            index = ch.find('=')
            ch = ch[index+2:]
            self.var.set(ch)
        temp = self.var.get() + 'x'
        self.var.set(temp)

    def div(self):
        if "=" in self.var.get():
            ch = self.var.get()
            index = ch.find('=')
            ch = ch[index+2:]
            self.var.set(ch)
        temp = self.var.get() + '/'
        self.var.set(temp)

    def egal(self):
        if "=" in self.var.get():
            ch = self.var.get()
            index = ch.find('=')
            ch = ch[index+2:]
            self.var.set(ch)

        if self.var.get().isdigit == False:
            self.var.set('')

        else:
            # Fermture des parenthèses si elles ne sont pas fermées
            ch = self.var.get()
            nb = ch.count("sin") + ch.count("cos") + ch.count("tan") + ch.count("sqrt")
            nb_diff = ch.count(")")
            nbtot = nb - nb_diff
            if nbtot > 0:
                for i in range(nbtot):
                    temp = self.var.get() + ')'
                    self.var.set(temp)

            #idée de simplification à développer
            # chaine = chaine.replace('x', "*")

            chaine = self.var.get()
            calcul = self.var.get()

            calcul = calcul.replace("√", "sqrt")
            calcul = calcul.replace('²', "**2")
            calcul = calcul.replace('x',"*")

            if self.ang.get() == "rad":
                # Traitement sur les angles en rad ( cos, sin et tan )
                if "sin" or "cos" or "tan" in calcul:
                    index = None
                    count = None
                    nb = calcul.count("sin") + calcul.count("cos") + calcul.count("tan")
                    for i in range(nb):
                        for i in range(len(calcul)):
                            car = calcul[i]
                            if car == "(" and calcul[i - 2] in ["i", "a", "o"] and calcul[i + 1] != "r":
                                index = i
                                newch = calcul[index:]
                                for x in range(len(newch)):
                                    if newch[x] == ")":
                                        count = x + i
                                        break

                                calcul = calcul[:index + 1] + "radians(" + calcul[index + 1:count + 1] + ")" + calcul[count + 1:]

            try:
                res = eval(calcul)
                operation = f"{chaine} = {str(res)}"
                self.var.set(operation)
                self.historique.append(operation)
                self.counter = -1

            except:
                self.var.set(f"Value Error")

    def pt(self):
        if "=" in self.var.get():
            self.var.set('')
        temp = self.var.get() + '.'
        self.var.set(temp)

    def clear(self):
        if "=" in self.var.get():
            self.var.set('')
        self.var.set('')
        self.counter = -1

    def par1(self):
        if "=" in self.var.get():
            self.var.set('')
        temp = self.var.get() + '('
        self.var.set(temp)

    def par2(self):
        if "=" in self.var.get():
            self.var.set('')
        temp = self.var.get() + ')'
        self.var.set(temp)

    def msg(self):

        popup = Tk()
        popup.wm_title("Historique")
        label = Label(popup, text="Historique")
        label.pack()


        #Dimensions de la fenêtre
        x = 250
        y = 380
        geometrie = f"{x}x{y}"
        popup.resizable(width=False, height=True)
        popup.geometry(geometrie)
        popup.config(bg="grey", relief="solid")

        # Génération de l'historique :
        histo = self.historique
        text = Text(popup, height=20, width=40)
        text.insert(INSERT, "Début de l'historique : \n")
        for i in range(len(histo)):
            text.insert(INSERT, f"{histo[i]} \n")
        text.insert(INSERT, "=====Fin de l'historique======\n")
        text.configure(state='disabled')
        text.pack()



        B_quit = Button(popup, text="quitter", command=popup.destroy)
        B_quit.pack(side=TOP)

        popup.mainloop()


def main():
    fenetre = Fenetre()
    fenetre.mainloop()