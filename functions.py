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

def db(type): # Fonction pour se connecter à la base de données
    db = mysql.connector.connect(**connection_params)
    if type:
        db.close()
def PushRequest(request): # Fonction permettant d'exécuter une requête d'affichage
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(request)
            resultats = c.fetchall()
        return resultats

def RecupUsers(): # Fonction de récupération des utilisateurs
    request="SELECT username, password FROM users"
    resultats =PushRequest(request)
    return resultats

def AfficherDictionnaire(cnv): # Fonction d'affichage du dictionnaire
    request = "SELECT titre, definition FROM dictionnaire"
    resultats = PushRequest(request)

    # Création du Treeview avec les colonnes "Titre" et "Définition"
    treeview = ttk.Treeview(cnv, columns=("Titre", "Définition"), show="headings")

    # Définition des en-têtes des colonnes
    treeview.heading("Titre", text="Titre")
    treeview.heading("Définition", text="Définition")

    # Ajout des données au Treeview
    for definition in resultats:
        treeview.insert("", "end", values=definition)

    treeview.column("Titre", width=150, stretch=False)
    treeview.column("Définition", stretch=True)

    treeview.pack(fill=tk.BOTH, expand=True)
    global dictionnaire_affiche
    dictionnaire_affiche = True

    return treeview

def RecupDefinition(titre): # Fonction de récupération d'une définition
    request = "SELECT definition FROM dictionnaire WHERE titre=%s"
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(request, (titre,))
            resultat = c.fetchone()
    return resultat


def AfficherTitre(): # Fonction d'affichage des titres
    request = "SELECT titre FROM dictionnaire"
    resultats = PushRequest(request)
    return resultats
def InsertionDefinition(titre,definition): # Fonction d'insertion des données
    request = 'INSERT INTO dictionnaire(titre, definition) VALUES (%s, %s);'
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(request, (titre, definition))
            db.commit()
def ModificationDefinition(definition, titre): # Fonction de modification d'une définition
    request = 'UPDATE dictionnaire SET definition=%s WHERE titre=%s'
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(request, (definition, titre))
            db.commit()
def DeleteDefinition(titre): # Fonction de suppression d'une définition
    request = 'DELETE FROM dictionnaire WHERE titre=%s'
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(request, (titre,))
            db.commit()

def Modification(request): # Fonction de modification
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(request)
def quitter_application(root): # Fonction pour fermer l'application complète
    root.quit()  # Quitter l'application