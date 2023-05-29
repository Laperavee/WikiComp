import tkinter as tk
from tkinter import font
import functions

def updatewindow(): # Fonction permettant l'affichage de la fenêtre indexant les différentes définitions
    root = tk.Tk()
    root.geometry("400x200")
    root.title("Modification / Suppression")
    custom_font = font.Font(size=16)

    resultats = functions.AfficherTitre()

    Titre = tk.Label(root, text="Modification des définitions", font=custom_font)
    Titre.pack()
    for resultat in resultats:
        lien = resultat[0]  # Supposons que le lien se trouve à l'indice 0 dans chaque résultat du tableau
        label_lien = tk.Label(root, text=lien, fg="blue", cursor="hand2")
        label_lien.pack()

        # Fonction de clic sur le lien
        def ouvrir_lien(url):
            titre = url.split("/")[-1]
            newwindowmodif(titre)

        # Lier la fonction de clic à l'étiquette de lien
        label_lien.bind("<Button-1>", lambda e, url=lien: ouvrir_lien(url))

    root.mainloop()

def modifrequete(description,titre,window): # Fonction permettant la modification d'une description, suivie de la fermeture de la fenêtre de modification
    functions.ModificationDefinition(description.get("1.0", "end-1c"),titre)
    window.destroy()
def deleterequete(titre,window): # Fonction permettant la suppression d'une description, suivie de la fermeture de la fenêtre de modification
    functions.DeleteDefinition(titre)
    window.destroy()
def newwindowmodif(titre): # Fonction permettant d'ouvrir la fenêtre de modification pour une définition
    window = tk.Tk()
    window.geometry("400x600")

    resultats = functions.RecupDefinition(titre)

    if resultats is not None:
        labelTitre = tk.Label(window, text=titre)
        labelTitre.pack()

        textDescription = tk.Text(window, width=30, height=10, wrap="word")
        textDescription.pack()
        textDescription.tag_configure("justified", justify="left")  # Configurer le style justifié
        textDescription.insert(tk.END, resultats[0].replace("{", "").replace("}", ""))

        btnPush = tk.Button(window, text="Modifier",
                            command=lambda: modifrequete(textDescription,labelTitre.cget("text"),window))
        btnPush.pack()
        btnSuppr = tk.Button(window, text="Supprimer", command=lambda: deleterequete(labelTitre.cget("text"),window))
        btnSuppr.pack()
    else:
        labelErreur = tk.Label(window, text="Aucune définition trouvée pour le titre donné.")
        labelErreur.pack()
    window.mainloop()
