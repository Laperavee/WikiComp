import tkinter as tk
from tkinter import font
import functions
def InsertDefinition(titre,definition,root): # Fonction permettant l'insertion d'une description, suivie de la fermeture de la fenêtre de modification
    functions.InsertionDefinition(titre,definition)
    root.destroy()
def insertionwindow(): # Fonction permettant l'affichage de la fenêtre d'insertion
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Nouvelle définition")
    custom_font = font.Font(size=16)

    labelInfo = tk.Label(root, text="Insérer une définition", font=custom_font)
    labelInfo.pack()
    labelTitre = tk.Label(root, text="Titre")
    labelTitre.pack()
    entryTitre = tk.Entry(root)
    entryTitre.pack()

    labelDefinition = tk.Label(root, text="Définition")
    labelDefinition.pack()
    entryDefinition = tk.Entry(root, width=100)
    entryDefinition.pack()

    btnSend = tk.Button(root, text="Enregistrer la définition",command=lambda: InsertDefinition(entryTitre.get(),entryDefinition.get(),root))
    btnSend.pack()
