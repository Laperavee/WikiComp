import tkinter as tk
import tkinter.messagebox

import functions
import connexion
import insertion
import update

btnAffichage = None
def wrapper_function(func, *args, **kwargs): # Fonction affichant le bouton de suppression du tableau (Wrapper_function permet d'éviter les conflits
                                             # entre fonctions. Le passage par une fonction tampon comme celle-ci évite de supprimer un tableau non existant par ex.
    treeview = func(*args, **kwargs)
    btnAffichage.config(state=tk.DISABLED)
    btnSupprimerTableau = tk.Button(frame, text="Enlever le dictionnaire",
                                   command=lambda: supprimer_tableau(treeview, btnSupprimerTableau))
    btnSupprimerTableau.pack(side="left")


def supprimer_tableau(treeview, btnSupprimerTableau): # Fonction supprimant le tableau
    treeview.pack_forget()  # Supprimer le tableau du canevas
    btnSupprimerTableau.pack_forget()  # Supprimer le bouton de suppression du tableau
    btnAffichage.config(state=tk.NORMAL)


def gestion_etat_connexion(etat): # Fonction permettant de retourner le statut de connexion True=connecté / False=invité
    # Fonction de rappel pour gérer l'état de connexion reçu depuis la fenêtre de connexion
    if etat:
        etatconnexion = True
    else:
        etatconnexion = False
    lancer_fenetre_principale(etatconnexion)


# Fonction pour lancer la fenêtre principale
def lancer_fenetre_principale(etatconnexion): # Fonction affichant la fenêtre principale
    global btnAffichage, btnInsertion, btnSortie,frame   # Déclarer les boutons comme des variables globales

    root = tk.Tk() # Créer la fenêtre principale
    root.geometry("800x600")
    root.title("Dictionnaire de données")

    frame_main = tk.Frame(root)  # Conteneur principal
    frame_main.pack(fill=tk.BOTH, expand=True)

    cnv = tk.Canvas(frame_main, background="white", height=1000, width=1000) # Conteneur secondaire
    cnv.pack(fill=tk.BOTH, expand=True)

    logo_image = tk.PhotoImage(master=root, file="alt/img/logo.png") # Logo de l'application
    tk.Label(cnv, image=logo_image).pack()

    frame = tk.Frame(cnv) # Conteneur tertiaire
    frame.pack()
    dictionnaire_affiche = False
    btnAffichage = tk.Button(frame, text="Afficher le dictionnaire", command=lambda: wrapper_function(functions.AfficherDictionnaire, cnv))
    btnAffichage.pack(side="left")
    if etatconnexion == True: # Si l'utilisateur est connecté, l'affichage des boutons Insertion et Update se font, sinon non.
        btnInsertion = tk.Button(frame, text="Insérer une définition", command=lambda: insertion.insertionwindow())
        btnInsertion.pack(side="left")
        btnUpdate = tk.Button(frame, text="Modifier une définition", command=lambda: update.updatewindow())
        btnUpdate.pack(side="left")
    root.mainloop()


# Appeler la fonction pour afficher la fenêtre de connexion
connexion.afficher_fenetre_connexion(gestion_etat_connexion)

