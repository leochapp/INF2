import tkinter.ttk
from tkinter import *
from math import *
from tkinter import messagebox, ttk


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

        self.historique = []

        self.var = tkinter.StringVar()
        tkinter.Label(top, textvariable=self.var, width=30).pack()
        self.var.set("") # Variable contenant le calcul

        # Génération des boutons

        bouton_par1 = Button(bottom, height=3, width=5, text='(', bg="cyan", borderwidth=4, command=self.par1, relief="raised")
        bouton_par1.grid(row=0,column=0, sticky=W, padx=2, pady=2)

        bouton_par2 = Button(bottom, height=3, width=5, text=')', bg="cyan", borderwidth=4, command=self.par2, relief="raised")
        bouton_par2.grid(row=0, column=1, sticky=W, padx=2, pady=2)

        bouton1 = Button(bottom, height=3, width=5, text='1', bg="cyan", borderwidth=4, command=self.add1, relief="raised")
        bouton1.grid(row=1,column=0, sticky=W, padx=2, pady=2)

        bouton2 = Button(bottom, height=3, width=5, text='2', bg="cyan", borderwidth=4, command=self.add2, relief="raised")
        bouton2.grid(row=1,column=1, sticky=W, padx=2, pady=2)

        bouton3 = Button(bottom, height=3, width=5, text='3', bg="cyan", borderwidth=4, command=self.add3, relief="raised")
        bouton3.grid(row=1,column=2, sticky=W, padx=2, pady=2)

        bouton4 = Button(bottom,height=3, width=5, text='4', bg="cyan", borderwidth=4, command=self.add4, relief="raised")
        bouton4.grid(row=2,column=0, sticky=W, padx=2, pady=2)

        bouton5 = Button(bottom, height=3, width=5, text='5', bg="cyan", borderwidth=4, command=self.add5, relief="raised")
        bouton5.grid(row=2,column=1, sticky=W, padx=2, pady=2)

        bouton6 = Button(bottom, height=3, width=5, text='6', bg="cyan", borderwidth=4, command=self.add6, relief="raised")
        bouton6.grid(row=2,column=2, sticky=W, padx=2, pady=2)

        bouton7 = Button(bottom, height=3, width=5, text='7', bg="cyan", borderwidth=4, command=self.add7, relief="raised")
        bouton7.grid(row=3,column=0, sticky=W, padx=2, pady=2)

        bouton8 = Button(bottom, height=3, width=5, text='8', bg="cyan", borderwidth=4, command=self.add8, relief="raised")
        bouton8.grid(row=3,column=1, sticky=W, padx=2, pady=2)

        bouton9 = Button(bottom, height=3, width=5, text='9', bg="cyan", borderwidth=4, command=self.add9, relief="raised")
        bouton9.grid(row=3,column=2, sticky=W, padx=2, pady=2)

        bouton0 = Button(bottom, height=3, width=5, text='0', bg="cyan", borderwidth=4, command=self.add0, relief="raised")
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

        bouton_historic = Button(text="H", bg="cyan", height=2, width=4, borderwidth=4, command=self.msg)
        bouton_historic.pack(side=RIGHT, padx=1)




# Actions des boutons quand on clique dessus

    def sin(self):
        if "=" in self.var.get():
            ch = self.var.get()
            index = ch.find('=')
            ch = ch[index + 2:]
            self.var.set(ch)
            temp = "sin(" + self.var.get()
            self.var.set(temp)
        else:
            operator = ["*", "/", "+", "-"]
            ch = self.var.get()
            max = len(ch) - 1
            if max != -1:
                if ch[max] not in operator:
                    temp = self.var.get() + "*sin("
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
            operator = ["*", "/", "+", "-"]
            ch = self.var.get()
            max = len(ch) - 1
            if max != -1:
                if ch[max] not in operator:
                    temp = self.var.get() + "*cos("
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
            operator = ["*", "/", "+", "-"]
            ch = self.var.get()
            max = len(ch) - 1
            if max != -1:
                if ch[max] not in operator:
                    temp = self.var.get() + "*tan("
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
            temp = "sqrt(" + self.var.get()
            self.var.set(temp)
        else:
            operator = ["*","/","+","-"]
            ch = self.var.get()
            max = len(ch)-1
            if max != -1:
                if ch[max] not in operator:
                    temp = self.var.get() + "*sqrt("
                    self.var.set(temp)
                else:
                    temp = self.var.get() + "sqrt("
                    self.var.set(temp)
            else:
                temp = self.var.get() + "sqrt("
                self.var.set(temp)

    def carr(self):
        if "=" in self.var.get():
            ch = self.var.get()
            index = ch.find('=')
            ch = ch[index + 2:]
            self.var.set(ch)

        temp = self.var.get() + "**2"
        self.var.set(temp)

    def pi(self):
        ch = self.var.get()
        max = len(ch) - 1

        if "=" in self.var.get():
            self.var.set('')
        if ch[max].isdigit():
            temp = self.var.get() + '*pi'
            self.var.set(temp)
        else:
            temp = self.var.get() + 'pi'
            self.var.set(temp)

    def add1(self):
        if "=" in self.var.get():
            self.var.set('')
        temp = self.var.get() + '1'
        self.var.set(temp)

    def add2(self):
        if "=" in self.var.get():
            self.var.set('')
        temp = self.var.get() + '2'
        self.var.set(temp)

    def add3(self):
        if "=" in self.var.get():
            self.var.set('')
        temp = self.var.get() + '3'
        self.var.set(temp)

    def add4(self):
        if "=" in self.var.get():
            self.var.set('')
        temp = self.var.get() + '4'
        self.var.set(temp)

    def add5(self):
        if "=" in self.var.get():
            self.var.set('')
        temp = self.var.get() + '5'
        self.var.set(temp)

    def add6(self):
        if "=" in self.var.get():
            self.var.set('')
        temp = self.var.get() + '6'
        self.var.set(temp)

    def add7(self):
        if "=" in self.var.get():
            self.var.set('')
        temp = self.var.get() + '7'
        self.var.set(temp)

    def add8(self):
        if "=" in self.var.get():
            self.var.set('')
        temp = self.var.get() + '8'
        self.var.set(temp)

    def add9(self):
        if "=" in self.var.get():
            self.var.set('')
        temp = self.var.get() + '9'
        self.var.set(temp)

    def add0(self):
        if "=" in self.var.get():
            self.var.set('')
        temp = self.var.get() + '0'
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
        temp = self.var.get() + '*'
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
        ch = self.var.get()
        nb = ch.count("sin") + ch.count("cos") + ch.count("tan") + ch.count("sqrt")
        nb_diff = ch.count(")")
        nbtot = nb - nb_diff
        if nbtot>0:
            for i in range(nbtot):
                temp = self.var.get() + ')'
                self.var.set(temp)

        if "=" in self.var.get():
            ch = self.var.get()
            index = ch.find('=')
            ch = ch[index+2:]
            self.var.set(ch)

        if self.var.get().isdigit == False:
            self.var.set('')
        else:

            #idée de simplification à développer
            chaine = self.var.get()
            #chaine = chaine.replace('²', '**2')
            #chaine = chaine.replace('x', "*")
            #chaine = chaine.replace('√', 'sqrt')
            try:
                res = eval(self.var.get())
                operation = f"{chaine} = {str(res)}"
                self.var.set(operation)
                self.historique.append(operation)

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