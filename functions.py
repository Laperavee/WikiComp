import tkinter as tk
from tkinter import ttk

import mysql.connector

import insertion

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

def RecupDefinition(titre):
    request = "SELECT definition FROM dictionnaire WHERE titre=%s"
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(request, (titre,))
            resultat = c.fetchone()
    return resultat


def AfficherTitre():
    request = "SELECT titre FROM dictionnaire"
    resultats = PushRequest(request)
    return resultats
def InsertionDefinition(titre,definition):
    request = 'INSERT INTO dictionnaire(titre, definition) VALUES (%s, %s);'
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(request, (titre, definition))
            db.commit()
def ModificationDefinition(definition, titre):
    request = 'UPDATE dictionnaire SET definition=%s WHERE titre=%s'
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(request, (definition, titre))
            db.commit()
def DeleteDefinition(titre):
    request = 'DELETE FROM dictionnaire WHERE titre=%s'
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(request, (titre,))
            db.commit()

def Modification(request):
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(request)
def quitter_application(root):
    root.quit()  # Quitter l'application