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




def ajoutFichier():
    file = "logeurs.xlsx"
    data = pd.read_excel(file)
    for i in range(len(data)):
        composition = (data.nom[i], data.prenom[i], data.numero_rue[i],data.nom_rue[i], data.code_postal[i], data.ville[i])
        request = f"INSERT into logeurs (nom, prenom, numero_rue, nom_rue, code_postal, ville) VALUES composition"
        cursor.execute(request)
        connexion.commit()


query = f"SELECT * FROM logements"
cursor.execute(query)
result = cursor.fetchall()
print(result)


cursor.close()
connexion.close()
print("La connexion SQLite est fermée")