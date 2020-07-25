# Cave Adventure
# Développement : Majoran, Pverte, romignou
# Date de développement : juillet, août 2020

import time
import random
#import des modules time et random

choix = ""
retour = ""
examen = ""
#réinitialisation des variables binaires choix et retour

def démarrage():
    print("")
    print("Vous êtes kidnappé par un monstre hideux. Vous êtes de ce fait dans une caverne. Vous vous réveillez de votre repos qui vous a semblé presque éternel.")
    print("")
    time.sleep(2)
    print("Vous scrutez des yeux l'endroit autour de vous. Rien ne vous semble familier. Vous voyez autour de vous une table en bois, et une torche accrochée au mur.")
    time.sleep(2)
    print("Qu'allez-vous faire ?")
    print("")
    print("EXAMINER la table")
    print("RECUPERER la torche")
    print("")
    examen = input("")
    #démarrage de l'histoire
    
#------------------------------------------------------------------------------------------------
    
def instructions():
    choix = ""
    print("")
    print("INSTRUCTIONS")
    print("")
    print("Vous êtes en train de jouer à CAVE ADVENTURE.")
    print("C'est un jeu d'aventure textuel où vous devez explorer les lieux environnants pour résoudre des énigmes et ainsi progresser dans le jeu.")
    print("Réalisez des actions en écrivant les commandes affichées qui sont en majuscules, et ce lorsque vous y êtes invité. (veuillez écrire la totalité de vos commandes en minuscules.)")
    print("Faites confiance à votre sens de l'orientation et de déduction, ainsi qu'à votre logique !")
    print(": ")
    #liste des instructions
    retour = input("RETOURNER à l'écran d'accueil... : ")
    if retour == "retourner":
        retour = ""
        écran_d_accueil()
    else:
        pass

#------------------------------------------------------------------------------------------------

def entrée_invalide():
    choix = ""
    print("Entrée invalide !")
    time.sleep(1)
    écran_d_accueil()
#prendre en compte les entrées invalides dans l'écran d'accueil

#------------------------------------------------------------------------------------------------
        
def écran_d_accueil():
    print("")
    print("======================")
    print("=== CAVE ADVENTURE ===")
    print("======================")
    print("")
    print("Bienvenue sur Cave Adventure ! Vous pouvez DEMARRER l'aventure ou voir les INSTRUCTIONS.")
    
    choix = input("Tapez votre réponse en minuscules : ")
    if choix == "démarrer":
        démarrage()
        #appeler la fonction démarrage
    
    elif choix == "instructions":
        instructions()
        #appeler la fonction instructions
    
    else:
        entrée_invalide()
        #appeler la fonction entrées invalides
        
#------------------------------------------------------------------------------------------------
        
écran_d_accueil()

#démarrage du programme à proprement parler
