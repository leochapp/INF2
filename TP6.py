import sqlite3
import pandas as pd

# Connexion à une base de donnée
try:
    connexion = sqlite3.connect("alesc.sqlite")
    cursor = connexion.cursor()
    print("Base de données crée et correctement connectée à SQLite")
    sql = "SELECT sqlite_version();"
    cursor.execute(sql)
    res = cursor.fetchall()
    print("La version de SQLite est: ", res)
except sqlite3.Error as error:
    print("Erreur lors de la connexion à SQLite", error)

def ajout_Logeurs():
    data = pd.read_excel("logeurs.xlsx")

    # vérification si ce n'est pas déjà dans la db
    request = ""
    cursor.execute(request)
    result = cursor.fetchall()
    print(result)


    #ajout du fichier excel en db
    for i in range(len(data)):
        nom = data["nom"][i]
        prenom = data["prenom"][i]
        num_rue = data["num_rue"][i]
        nom_rue = data["nom_rue"][i]
        code_postal = data["code_postal"][i]
        ville = data["ville"][i]
        #request = f"INSERT INTO 'logeurs' (idlogeurs, nom, prenom, num_rue, nom_rue, code_postal, ville) VALUES(NULL, nom, prenom, num_rue, nom_rue, code_postal, ville)"
        #cursor.execute(request)
        #connexion.commit()
    cursor.close()


print("La connexion SQLite est fermée")