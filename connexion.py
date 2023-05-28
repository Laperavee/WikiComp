import tkinter as tk
from tkinter import messagebox
import hashlib

import functions


def se_connecter(entryUsername, entryPassword, fenetre_connexion, callback, fermer_fenetre_connexion):
    # Récupérer les valeurs du nom d'utilisateur et du mot de passe
    username = entryUsername.get()
    password = entryPassword.get()

    users = functions.RecupUsers()
    user_connexion = False

    # Vérifier les informations de connexion
    for user in users:
        if username == user[0] and hashlib.md5(password.encode()).hexdigest() == user[1]:
            # Afficher un message de réussite
            messagebox.showinfo("Connexion réussie", "Vous êtes connecté !")
            user_connexion = True
            callback(user_connexion)
            fermer_fenetre_connexion()
            break

    if not user_connexion:
        # Afficher un message d'erreur
        messagebox.showerror("Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect.")
        callback(user_connexion)

def afficher_fenetre_connexion(callback, lancer_fenetre_principale):
    # Créer la fenêtre de connexion
    fenetre_connexion = tk.Toplevel()
    fenetre_connexion.title("Connexion")

    # Créer les widgets
    labelUsername = tk.Label(fenetre_connexion, text="Nom d'utilisateur:")
    labelUsername.pack()
    entryUsername = tk.Entry(fenetre_connexion)
    entryUsername.pack()

    labelPassword = tk.Label(fenetre_connexion, text="Mot de passe:")
    labelPassword.pack()
    entryPassword = tk.Entry(fenetre_connexion, show="*")
    entryPassword.pack()

    etat = tk.BooleanVar()  # Variable pour stocker l'état de la connexion

    def fermer_fenetre_connexion():
        fenetre_connexion.destroy()

    def callback_connexion():
        # Appeler la fonction pour se connecter
        se_connecter(entryUsername, entryPassword, fenetre_connexion, callback, fermer_fenetre_connexion)

    btnConnexion = tk.Button(fenetre_connexion, text="Se connecter", command=callback_connexion)
    btnConnexion.pack()

    btnInvite = tk.Button(fenetre_connexion, text="Invité", command=lambda: fenetre_connexion.destroy())
    btnInvite.pack()

    # Lancer la boucle principale de la fenêtre de connexion
    fenetre_connexion.protocol("WM_DELETE_WINDOW", lambda: callback(False))
    fenetre_connexion.mainloop()
