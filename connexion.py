# connexion.py
import tkinter
import tkinter as tk
from tkinter import messagebox
import hashlib

import functions

def DestroyApp(root):
    root.quit()
def se_connecter(entryUsername, entryPassword, callback):
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
    if(user_connexion==False):
        messagebox.showinfo("Connexion impossible","L'identifiant ou le mot de passe est incorrect ! \nVous êtes maintenant connecté en tant qu'invité")
    callback(user_connexion)


def afficher_fenetre_connexion(callback):
    # Créer la fenêtre de connexion
    root = tk.Tk()
    root.geometry("200x150")
    root.title("Connexion")
    frame = tkinter.Frame(root)
    frame.pack()
    # Créer les widgets
    labelUsername = tk.Label(frame, text="Nom d'utilisateur:")
    labelUsername.pack()
    entryUsername = tk.Entry(frame)
    entryUsername.pack()

    labelPassword = tk.Label(frame, text="Mot de passe:")
    labelPassword.pack()
    entryPassword = tk.Entry(frame, show="*")
    entryPassword.pack()
    def callback_connexion():
        # Appeler la fonction pour se connecter
        se_connecter(entryUsername, entryPassword, callback)

    def callback_connexion_wrapper():
        callback_connexion()

    btnConnexion = tk.Button(frame, text="Se connecter", command=callback_connexion_wrapper)
    btnConnexion.pack()

    btnInvite = tk.Button(frame, text="Invité", command=lambda: callback(False))
    btnInvite.pack()

    # Lancer la boucle principale
    root.protocol("WM_DELETE_WINDOW", DestroyApp(root))
    root.mainloop()