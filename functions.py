import tkinter as tk
from tkinter import ttk

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

def RecupUsers():
    request="SELECT username, password FROM users"
    resultats =PushRequest(request)
    return resultats

def AfficherDictionnaire(cnv):
    request = "SELECT titre, definition FROM dictionnaire"
    resultats = PushRequest(request)

    # Créer le Treeview avec les colonnes "Titre" et "Définition"
    treeview = ttk.Treeview(cnv, columns=("Titre", "Définition"), show="headings")

    # Définir les en-têtes des colonnes
    treeview.heading("Titre", text="Titre")
    treeview.heading("Définition", text="Définition")

    # Ajouter les données au Treeview
    for definition in resultats:
        treeview.insert("", "end", values=definition)

    treeview.column("Titre", width=150, stretch=False)
    treeview.column("Définition", stretch=True)

    treeview.pack(fill=tk.BOTH, expand=True)
    global dictionnaire_affiche
    dictionnaire_affiche = True

    return treeview
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
def quitter_application(root):
    root.quit()  # Quitter l'application
