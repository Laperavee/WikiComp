import tkinter as tk
import mysql.connector

# Paramètres de connexion à la base de données
connection_params = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'dictionnaire'
}

def db(type):
    db = mysql.connector.connect(**connection_params)
    if type:
        db.close()

def PushRequest(request):
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(request)
            resultats = c.fetchall()
        return resultats

def AfficherDictionnaire(cnv):
    request = "SELECT titre FROM dictionnaire"
    resultats = PushRequest(request)
    for definition in resultats:
        label = tk.Label(cnv, text=definition[0])
        label.pack()
    global dictionnaire_affiche
    dictionnaire_affiche = True

def InsertionDefinition():
    titre = "Titre de la définition"
    definition = "Contenu de la définition"
    request = 'INSERT INTO dictionnaire(titre, definition) VALUES (%s, %s);'
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(request, (titre, definition))
            db.commit()


def ModificationDefinition():
    print(1)


def Modification(request):
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(request)
