import tkinter
import functions
from tkinter import *

def wrapper_function(func, *args, **kwargs):
    func(*args, **kwargs)
    btnAffichage.config(state=DISABLED)
root=Tk()
cnv=Canvas(root, width=400, height=400, background="ivory")
cnv.pack()
dictionnaire_affiche = False
root.resizable(False, False)


btnAffichage = tkinter.Button(cnv, text="Afficher le dictionnaire", command=lambda: wrapper_function(functions.AfficherDictionnaire, cnv))
btnAffichage.pack()


btnInsertion = tkinter.Button(cnv, text="Insérer une définition")
btnInsertion.pack()
btnSortie = tkinter.Button(cnv, text="Sortir")
btnSortie.pack()
""" continueV = True
while continueV == True:
    print("")
    
              "Modifier une définition \n"
          "Supprimer une définition \n"

    choix = int(input("Que voulez-vous faire ? "))

    match choix:
        case 1:
            functions.AfficherDictionnaire()
            print("Appuyer sur Entrée pour continuer")
        case 2:
            print("Pas de fonction disponible")
        case 3:
            print("Pas de fonction disponible")
        case 4:
            titre = str(input("Veuillez saisir le titre : "))
            definition = str(input("Veuillez saisir la définition : "))
            functions.InsertionDefinition(titre, definition)
        case 5:
            continueV = False

"""
cnv.pack()
root.mainloop()
