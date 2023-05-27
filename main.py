import tkinter as tk
from tkinter import ttk

import functions
from tkinter import *

def wrapper_function(func, *args, **kwargs):
    treeview= func(*args, **kwargs)
    btnAffichage.config(state=DISABLED)
    btnSupprimerTableau = tk.Button(frame, text="Enlever le dictionnaire",command=lambda: supprimer_tableau(treeview, btnSupprimerTableau))
    btnSupprimerTableau.pack(side="left")

def supprimer_tableau(treeview,btnSupprimerTableau):
    treeview.pack_forget()  # Supprimer le tableau du canevas
    btnSupprimerTableau.pack_forget()  # Supprimer le bouton de suppression du tableau
    btnAffichage.config(state=NORMAL)


root=Tk()
root.geometry("800x600")

frame_main = tk.Frame(root)  # Conteneur principal
frame_main.pack(fill=tk.BOTH, expand=True)

cnv=Canvas(frame_main, background="white", height=1000, width=1000)
cnv.pack(fill=tk.BOTH, expand=True)

logo=PhotoImage(file="alt/img/logo.png")
Label(cnv, image=logo).pack()

frame = tk.Frame(cnv)
frame.pack()
dictionnaire_affiche = False

btnAffichage = tk.Button(frame, text="Afficher le dictionnaire", command=lambda: wrapper_function(functions.AfficherDictionnaire, cnv))
btnAffichage.pack(side="left")

btnInsertion = tk.Button(frame, text="Insérer une définition")
btnInsertion.pack(side="left")
btnSortie = tk.Button(root, text="Sortir", command=lambda: functions.quitter_application(root))
btnSortie.pack(relx=1.0, rely=1.0, anchor="ne")

root.mainloop()
