from tkinter import *
import string
import time

#--------------------------------------------------------------------------
# Fenêtre de Bienvenue à l'utilisateur..

#time.sleep(1)
prenom = input ("Rentrez votre prénom :")

print("Bienvenue dans l'Antivirus Xprotect system, " + str(prenom))
time.sleep(3)
print("")
print("L'Antivirus va s'ouvrir dans un instant..")
print("Liaison-tranfert avec la DATA-BASE..")
time.sleep(3)

#------------------------------------------------------------------------
# ouverture de l'Antivirus et de la Fenêtre..

windows = Tk()
frame = Frame(windows)


def infos_pc():
    # ouverture d'une mini Fenêtre pour les infos du PC
    windows = Tk()
    frame = Frame(windows)
    windows.title("Infos")
    windows.geometry("300x300")


    texte = Label (frame, text="Système d'exploitation : Windows 10", font=("Consolas", 10))
    texte.pack()
    texte = Label (frame, text="IDE de consommation : 5624-44233", font=("Consolas", 10))
    texte.pack()

    frame.pack(expand=YES)
    windows.mainloop()

def infos_antivirus():
    # ouverture d'une mini Fenêtre pour les infos du PC
    windows = Tk()
    frame = Frame(windows)
    windows.title("Infos Antivirus")
    windows.geometry("680x400")


    texte = Label (frame, text="Version des programmes externes/internes : 1.00.27", font=("Consolas", 10))
    texte.pack()
    texte = Label (frame, text="Comptabilité du logiciel : Tout est compatible..", font=("Consolas", 10))
    texte.pack()
    texte = Label (frame, text="Language informatique utilisé : Python..", font=("Consolas", 10))
    texte.pack()
    texte = Label (frame, text="Licenses et auteurs du logiciel : LICENSE(programms_444353)//fondateur= ANONYMOUS_91", font=("Consolas", 10))
    texte.pack()

    frame.pack(expand=YES)
    windows.mainloop()

def Connexion():
    windows = Tk()
    frame = Frame(windows)
    windows.title("Me connecter")
    windows.geometry("300x300")


    texte = Label (frame, text="Identifiant :", font=("Consolas", 10))
    texte.pack()


    ide = Entry(frame, font=("Consolas", 10))
    ide.pack()

    texte = Label (frame, text="Mot de passe :", font=("Consolas", 10))
    texte.pack()

    mdp = Entry(frame, font=("Consolas", 10))
    mdp.pack()

    bouton = Button(frame, text="OK", font=("Consolas", 10), command=connex)
    bouton.pack()

    frame.pack(expand=YES)
    windows.mainloop()

def connex():
    print("______________________________________________________________")
    print("Connexion au serveur distant..")
    time.sleep(3)
    print("Connexion activé..")

def adresse():
     print("______________________________________________________________")
     print("Votre adresse mail et votre mot de passe ont bien été enregistrer...")
     time.sleep(2)
     print("Voici votre Identifiant : 123-888")
     print("Et votre mot de passe : wx23")
     time.sleep(1)


def Compte():
    windows = Tk()
    frame = Frame(windows)
    windows.title("Créer un compte")
    windows.geometry("300x300")


    texte = Label (frame, text="Adresse mail :", font=("Consolas", 10))
    texte.pack()

    adress = Entry(frame, font=("Consolas", 10))
    adress.pack()

    texte = Label (frame, text="Mot de passe :", font=("Consolas", 10))
    texte.pack()

    mdp = Entry(frame, font=("Consolas", 10))
    mdp.pack()

    bouton = Button(frame, text="OK", font=("Consolas", 10), command=adresse)
    bouton.pack()

    frame.pack(expand=YES)
    windows.mainloop()

def droits():
    windows = Tk()
    frame = Frame(windows)
    windows.title("Droits et permission du logiciel")
    windows.geometry("450x300")


    texte = Label (frame, text="Accès au données du PC : [Oui/Non]", font=("Consolas", 10))
    texte.pack()
    droit_entry = Entry(frame, font=("Consolas", 10))
    droit_entry.pack()

    texte = Label (frame, text="Sauvegarde externe (pour le logiciel): [Oui/Non]", font=("Consolas", 10))
    texte.pack()
    droit_entry2 = Entry(frame, font=("Consolas", 10))
    droit_entry2.pack()

    texte = Label (frame, text="Acceptation de la LICENSE OPEN-SOURCE : [Oui/Non]", font=("Consolas", 10))
    texte.pack()
    droit_entry3 = Entry(frame, font=("Consolas", 10))
    droit_entry3.pack()

    bouton = Button(frame, text="OK", font=("Consolas", 10))
    bouton.pack()

    frame.pack(expand=YES)
    windows.mainloop()

def scann_virus():
    print("______________________________________________________________")
    print("Scann du lecteur C:")
    time.sleep(3)
    print("Result=Aucun virus ou programme(s) malveillant(s) a été détecté dans votre ordinateur..")
    #time.sleep(2)
    #texte = Label (frame, text="Scann en attente..", font=("Consolas", 10))
    #texte.pack()
    #time.sleep(4)

    frame.pack(expand=YES)
    windows.mainloop()

def scann_espions():
    print("______________________________________________________________")
    print("Scann du lecteur C:")
    time.sleep(3)
    print("Result=Aucun logiciel(s) espion(s) été détecté dans votre ordinateur..")
    #time.sleep(2)
    #texte = Label (frame, text="Scann en attente..", font=("Consolas", 10))
    #texte.pack()
    #time.sleep(4)

    frame.pack(expand=YES)
    windows.mainloop()

def scann_pr():
    windows = Tk()
    frame = Frame(windows)
    windows.title("Recherche précise de programmes..")
    windows.geometry("450x300")


    texte = Label (frame, text="Rentrez le nom du programme à cibler :", font=("Consolas", 10))
    texte.pack()
    pr_entry = Entry(frame, font=("Consolas", 10))
    pr_entry.pack()

    bouton = Button(frame, text="Suivant", font=("Consolas", 10), command=bouton_c)
    bouton.pack()

    frame.pack(expand=YES)
    windows.mainloop()

def liste():
    windows = Tk()
    frame = Frame(windows)
    windows.title("Infos Black_list")
    windows.geometry("550x300")


    texte = Label (frame, text="La Black_list contitent 3014 noms de virus...", font=("Consolas", 10))
    texte.pack()
    texte = Label (frame, text="Si vous le souhaitez, vous pouvez rajouter un nouveau nom de virus dans la Black_list :", font=("Consolas", 9))
    texte.pack()
    pr_entry = Entry(frame, font=("Consolas", 10))
    pr_entry.pack()

    bouton = Button(frame, text="OK", font=("Consolas", 10), command=bouton_list)
    bouton.pack()

    frame.pack(expand=YES)
    windows.mainloop()

def bouton_list():
    time.sleep(1)
    print("______________________________________________________________")
    print("Le nom de votre virus a bien été rajouté dans la liste des éléments externes...")

def mise():
    windows = Tk()
    frame = Frame(windows)
    windows.title("Mise à jour")
    windows.geometry("550x300")


    texte = Label (frame, text="La prochaine mise à jour de l'Antivirus sera le 15/10/2020 [Version: 2.0 - 2.02]", font=("Consolas", 9))
    texte.pack()
    texte = Label (frame, text="______________________________________________________________", font=("Consolas", 9))
    texte.pack()
    texte = Label (frame, text="", font=("Consolas", 10))
    texte.pack()
    texte = Label (frame, text="La version 2.02 aura au moins 100 voir 200 nouveaux noms de virus, et ", font=("Consolas", 9))
    texte.pack()
    texte = Label (frame, text="il aura sûrement de nouvelles fonctionalitées..", font=("Consolas", 9))
    texte.pack()

    frame.pack(expand=YES)
    windows.mainloop()

def aide():
    windows = Tk()
    frame = Frame(windows)
    windows.title("Aide")
    windows.geometry("450x300")


    texte = Label (frame, text="Si l'Antivirus ne répond plus :", font=("Consolas", 10))
    texte.pack()
    texte = Label (frame, text="Cliquez sur Options -> puis sur Actualisez l'Antivirus", font=("Consolas", 9))
    texte.pack()

    texte = Label (frame, text="Si aucun résultat s'affiche :", font=("Consolas", 10))
    texte.pack()
    texte = Label (frame, text="Il faut regarder dans la première fenêtre, ", font=("Consolas", 9))
    texte.pack()
    texte = Label (frame, text="c'est là où sont les résultats externes...", font=("Consolas", 9))
    texte.pack()

    texte = Label (frame, text="Pour n'importe quel problème laisser un commentaire sur le site de Xprotect :", font=("Consolas", 9))
    texte.pack()
    texte = Label (frame, text="https://lanonyme929.wixsite.com/xprotect", font=("Consolas", 9))
    texte.pack()

    frame.pack(expand=YES)
    windows.mainloop()

#def bouton_infos():
    #ouvrir le fichier .HTML avec l'assistance d'aide..
    #cette fonction apparaitra dans la version 1.06..

def pr_utiles():
    windows = Tk()
    frame = Frame(windows)
    windows.title("Programmes utilisés :")
    windows.geometry("500x400")


    texte = Label (frame, text="[Pr.externe A3]", font=("Consolas", 10))
    texte.pack()
    texte = Label (frame, text="//liaison sattelite externe.;act.", font=("Consolas", 9))
    texte.pack()
    texte = Label (frame, text="(enter/pr;liaison;comm.)", font=("Consolas", 9))
    texte.pack()
    texte = Label (frame, text="[//Code adjoint; enter section;]= 03/pr.ex;", font=("Consolas", 9))
    texte.pack()
    texte = Label (frame, text="Programme interne vue;", font=("Consolas", 9))
    texte.pack()

    frame.pack(expand=YES)
    windows.mainloop()

def pr_details():
    windows = Tk()
    frame = Frame(windows)
    windows.title("Détails des programmes")
    windows.geometry("500x400")


    texte = Label (frame, text="Les programmes de sécurité internes de cet Antivirus", font=("Consolas", 10))
    texte.pack()
    texte = Label (frame, text="fonctionne avec la base de données exernes des services", font=("Consolas", 10))
    texte.pack()
    texte = Label (frame, text="du serveur TINKER Windows Corporation Host.", font=("Consolas", 10))
    texte.pack()

    frame.pack(expand=YES)
    windows.mainloop()

def data():
    windows = Tk()
    frame = Frame(windows)
    windows.title("Réglage de la DATA-BASE..")
    windows.geometry("700x600")

    texte = Label (frame, text="La DATA-BASE de l'Antivirus Xprotect se", font=("Consolas", 10))
    texte.pack()
    texte = Label (frame, text="permet de relier votre ordinateur à sa DATA-BASE, pour", font=("Consolas", 10))
    texte.pack()
    texte = Label (frame, text="activer les dernières modifications de l'éditeur.", font=("Consolas", 10))
    texte.pack()
    texte = Label (frame, text="", font=("Consolas", 10))
    texte.pack()
    texte = Label (frame, text="Pour plus d'infos et de choix, rendez-vous sur la page web des paramètres de l'Antivirus Xprotect...", font=("Consolas", 8))
    texte.pack()

    frame.pack(expand=YES)
    windows.mainloop()

def bouton_c():
    print("______________________________________________________________")
    print("Scann de l'application ou programme(s)..")
    time.sleep(3)
    print("Result=Aucun virus ou programme(s) malveillant(s) a été détecté dans cette application ou programmme(s)..")

def connexion_re():
    print("______________________________________________________________")
    print("Votre compte est déconnecter..")



windows.title("Xprotect system (version 2.05)")
windows.geometry("680x700")


#c = Canvas(windows,)
#frame.pack()
#fond = PhotoImage(file="D:\photo.png")
#c.create_image(100, 1000, image=fond)

texte = Label (frame, text="Bienvenue dans l'Antivirus Xprotect system !", font=("Consolas", 15))
# side= /LEFT = gauche , RIGHT = droite , BOTTOM = en bas , et rien en haut../
texte.pack()

texte = Label (frame, text="______________________________________________________________", font=("Consolas", 10))
texte.pack()
texte = Label (frame, text="Le meilleur antivirus OPEN-SOURCE gratuit !", font=("Consolas", 10))
texte.pack()
texte = Label (frame, text="", font=("Consolas", 10))
texte.pack()
bouton = Button(frame, text="Actualiser l'Antivirus", font=("Consolas", 10))
bouton.pack()

#name_entry = Entry(frame, font=("Consolas", 10))
#name_entry.pack()


# création d'un bouton
#bouton = Button(frame, text="Suivant", font=("Consolas", 10), command=bouton_suivant)
#bouton.pack()

# création d'un menu
menu_bar = Menu(windows)

file_menu = Menu (menu_bar, tearoff=0)
file_menu2 = Menu (menu_bar, tearoff=0)
file_menu3 = Menu (menu_bar, tearoff=0)
file_menu4 = Menu (menu_bar, tearoff=0)
file_menu5 = Menu (menu_bar, tearoff=0)

menu_bar.add_cascade(label="Informations de l'ordinateur", menu=file_menu)
file_menu.add_command(label="Informations du système", command=infos_pc)
file_menu.add_command(label="Informations de l'Antivirus", command=infos_antivirus)
file_menu.add_command(label="Droits et permission du logiciel", command=droits)

menu_bar.add_cascade(label="Connexion", menu=file_menu2)
file_menu2.add_command(label="Créer un compte", command=Compte)
file_menu2.add_command(label="Me connecter", command=Connexion)
file_menu2.add_command(label="Me déconnecter", command=connexion_re)

menu_bar.add_cascade(label="Options", menu=file_menu3)
file_menu3.add_command(label="Actualisez l'Antivirus")
file_menu3.add_command(label="Mise à jour", command=mise)
file_menu3.add_command(label="Black_list", command=liste)
file_menu3.add_command(label="DATA-BASE Xprotect System", command=data)
file_menu3.add_command(label="Recherche de virus", command=scann_virus)
file_menu3.add_command(label="Recherche de logiciel espions", command=scann_espions)
file_menu3.add_command(label="Recherche précise  de programmes à vérifier", command=scann_pr)

menu_bar.add_cascade(label="Programmes", menu=file_menu4)
file_menu4.add_command(label="Programmes utilisé pour la sécurité", command=pr_utiles)
file_menu4.add_command(label="Détails des programmes", command=pr_details)

menu_bar.add_cascade(label="Aide", menu=file_menu5)
file_menu5.add_command(label="Support Assistance", command=aide)


windows.config(menu=menu_bar)
#windows.config(background="grey")
frame.pack(expand=YES)
windows.mainloop()
