# connexion.py
import tkinter as tk
from tkinter import messagebox
import hashlib

import functions

def DestroyApp(root):
    root.quit()
def se_connecter(entryUsername, entryPassword, root, callback):
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
            break

    callback(user_connexion)


def afficher_fenetre_connexion(callback, lancer_fenetre_principale):
    # Créer la fenêtre de connexion
    root = tk.Tk()
    root.title("Connexion")

    # Créer les widgets
    labelUsername = tk.Label(root, text="Nom d'utilisateur:")
    labelUsername.pack()
    entryUsername = tk.Entry(root)
    entryUsername.pack()

    labelPassword = tk.Label(root, text="Mot de passe:")
    labelPassword.pack()
    entryPassword = tk.Entry(root, show="*")
    entryPassword.pack()

    def fermer_fenetre_connexion():
        root.destroy()

    def callback_connexion():
        # Appeler la fonction pour se connecter
        se_connecter(entryUsername, entryPassword, root, callback)

    def callback_connexion_wrapper():
        callback_connexion()

    btnConnexion = tk.Button(root, text="Se connecter", command=callback_connexion_wrapper)
    btnConnexion.pack()

    btnInvite = tk.Button(root, text="Invité", command=lambda: callback(False))
    btnInvite.pack()

    # Lancer la boucle principale
    root.protocol("WM_DELETE_WINDOW", DestroyApp(root))
    root.mainloop()
