# Exercice 3 // Décorateurs

def nombre(f):
    def wrapper(nombre):
        nb_fin = nombre #On récupère qu'un suel nombre ici
        if type(nombre) != int:
            try:
                nb_fin += int(nb_fin)
                #Raise ValueError("Le pramètre n'est pas un nombre")
            except:
                nb_fin = 0
        return f(nb_fin)
    return wrapper


# Exercice 1

@nombre
def somme_chiffre(nb):
    nb=str(nb)
    tab=[]
    for i in range(len(nb)):
        tab.append(int(nb[i]))
    return sum(tab)

@nombre
def nombre_chiffres(nb):
    nb=str(nb)
    return len(nb)

@nombre
def separe_nombre(nb):
    moitie = int(nombre_chiffres(nb)/2)
    fin = nombre_chiffres(nb)
    part1= ""
    part2= ""
    nb = str(nb)
    for i in range(moitie):
        part1 += nb[i]
    for i in range(moitie, fin):
        part2 += nb[i]

    part1 = int(part1)
    part2 = int(part2)

    return part1, part2

@nombre
def main_couicable():
    nombre=int(input("Veuillez rentrer un nombre : "))

    if nombre%2 == 0:
        couple = separe_nombre(nombre)
        if somme_chiffre(couple[0]) == somme_chiffre(couple[1]):
            return "Couicable"
        else:
            return "Non couicable"
    else:
        return "Non couicable"

@nombre
def somme_chiffre2(n):
    if n//10==0:
        return
    else:
        return n%10 + somme_chiffre2(n//10)


# Exercice 2

def somme_ligne(mat, i):
    taillemat = len(mat[0])

    sumligne= [0 for i in range(taillemat)]
    for i in range(taillemat):
        for j in range(taillemat): #matrice carré donc autant de lignes que de colones
            sumligne[i] += mat[i][j]
    return sumligne[i]

def somme_colone(mat, j):
    taillemat = len(mat[0]) # matrice carré

    sumcolone = [0 for i in range(taillemat)]
    for i in range(taillemat):
        for j in range(taillemat):  # matrice carré donc autant de lignes que de colones
            sumcolone[i] += mat[j][i]
    return sumcolone[j]

def somme_diag1(mat):
    taillemat = len(mat[0]) #matrice carré
    sumdiag1 = 0
    for i in range(0, taillemat):
        sumdiag1 += mat[i][i]
    return sumdiag1

def somme_diag2(mat):
    taillemat = len(mat[0])  # matrice carré
    sumdiag2 = 0
    for i in range(taillemat-1, -1, -1):
        sumdiag2 += mat[i][i]
    return sumdiag2

def magique(mat_c):
    taillemat = len(mat_c[0])  # matrice carré
    sommeLigne = []
    sommeColone = []
    for i in range(taillemat):
        sommeLigne.append(somme_ligne(mat_c, i))
        sommeColone.append(somme_colone(mat_c, i))

    totligne = sum(sommeLigne) / taillemat
    totcol = sum(sommeColone) / taillemat


    if totligne == totcol == somme_diag1(mat_c) == somme_diag2(mat_c):
        return True
    else:
        return False

def carre_magique_normal(mat_c):
    taillemat = len(mat_c[0])  # matrice carré
    nombres = taillemat**2
    allnnumbers = []

    for i in range(taillemat):
        for j in range(taillemat):
            allnnumbers.append(mat_c[i][j])

    allnnumbers = sorted(allnnumbers)
    verify = True
    for x in range(nombres):
        if allnnumbers[x] != (x+1):
            verify = False
            break
    return verify

def affiche_test_cm(*args):
    for mat in args: # On suppose que ce sont des matrices
        if magique(mat) == True:
            print(f"La matrice {mat} est magique")
            if carre_magique_normal(mat) == True:
                print(f"Le carré magique est normal")
            else:
                print(f"Le carré magique n'est pas normal")
        else:
            print(f"La matrice {mat} n'est pas magique")



