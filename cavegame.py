# Cave Adventure
# Développement : Majoran, Pverte, romignou
# Date de développement : juillet, août 2020

import time
import random
#import des modules time et random
import os
from os import name

def clear():
    if name == 'nt':
        _ = os.system("cls")
    else :
        _ = os.system("clear")

def choix(options):
    i = 0
    max = 0
    sorties = []
    while i < len(options):
        c=""
        while options[i] != '[':
            c+=options[i]
            i+=1
        x = ""
        i+=1
        while options[i] != ']':
            x+=options[i]
            i+=1
        sorties.append(x)
        print(str(max)+":"+c)
        max+=1
        c=""
        i+=1
    x=input()
    while (len(x)!=1 or ord(x[0])<48 or ord(x[0])>47+max) :
        print("Ce n'est pas un choix valide, enfin !")
        x=input()
    clear()
    return sorties[ord(x[0])-48]

def choixaction(listes):
    stop = False
    a=""
    while not(stop):
        print("Qu'allez-vous faire ?")
        a="!"+choix("Menu[0]Examiner[1]Ramasser[2]Parler[3]Se Déplacer[4]Utiliser[5]")
        if a=="!5":
            print("On ne peut rien utiliser pour l'instant...")
        if a=="!0":
            print("Le menu n'est pas encore prêt...")
        if a=="!1":
            if len(listes[0])==0:
                print("Il n'y a rien a examiner.")
            else:
                print("Que voulez-vous examiner ?")
                a="Rien[-]"
                c=len(listes[0])
                while c>0:
                    c-=1
                    a=listes[0][c]+a
                a=choix(a)
                if a!="-":
                    stop=True
        if a=="!2":
            if len(listes[1])==0:
                print("Il n'y a rien a ramasser.")
            else:
                print("Que voulez-vous ramasser ?")
                a="Rien[-]"
                c=len(listes[1])
                while c>0:
                    c-=1
                    a=listes[1][c]+a
                a=choix(a)
                if a!="-":
                    stop=True
        if a=="!3":
            if len(listes[2])==0:
                print("Il n'y a personne a qui parler.")
            else:
                print("A qui voulez-vous parler ?")
                a="Rien[-]"
                c=len(listes[2])
                while c>0:
                    c-=1
                    a=listes[2][c]+a
                a=choix(a)
                if a!="-":
                    stop=True
        if a=="!4":
            if len(listes[3])==0:
                print("Il n'y a aucun endroit ou aller.")
            else:
                print("Par ou voulez-vous partir ?")
                a="Rien[-]"
                c=len(listes[3])
                while c>0:
                    c-=1
                    a=listes[3][c]+a
                a=choix(a)
                if a!="-":
                    stop=True
    return a

fichier = open("DATABASE.txt","r")
debutsparagraphes = []
debutszones = []
pos = 0
posz = 0
x=0
for line in fichier :
    if line[0]=='[':
        debutsparagraphes.append(pos)
        x+=1
    if line[0]==']':
        posz+=pos
        debutszones.append(x)
        debutszones.append(posz)
        pos = len(line)+1
    else :
        pos+=len(line)+1
#Ce for permet de former deux listes : debutsparagraphe, avec les positions de chaque paragraphe dans une zone, et debutszones qui contient le nombre de paragraphes avant la zone intéressante, et le début de la zone.

def lectureparagraphe(database,paragraphe,zone,listes):
    database.seek(debutsparagraphes[debutszones[zone*2]+paragraphe]+debutszones[zone*2+1],0)
    ligne = database.readline()
    s =  ligne[0]
    ligne = ligne[1:]
    ligne = ligne[:-1]
    if s==']':
        #Debut de la Zone
        ligne = database.readline()
        s =  ligne[0]
        ligne = ligne[1:]
    #Debut du paragraphe
    ligne = database.readline()
    s = ligne[0]
    ligne = ligne[1:]
    ligne = ligne[:-1]
    while s != '5' and s != '9' and s != '3' and s != '[' and s != ']' and s != '8' and s!='7':
        if s == '0':
            print(ligne)
        if s == '6':
            input()
            clear()
        if s=="*" or s=="/" or s=="+" or s=="-":
            a = 0
            if s=="-":
                a=1
            if s=="*":
                a=2
            if s=="/":
                a=3
            b = 1
            max=len(ligne)
            if ligne[0]=='=':
                listes[a]=[]
            while b<max:
                c = ""
                while ligne[b]!=']':
                    c+=ligne[b]
                    b+=1
                c+="]"
                b+=1
                if ligne[0]!='-':
                    listes[a].append(c)
        ligne = database.readline()
        s = ligne[0]
        ligne = ligne[1:]
        ligne = ligne[:-1]
    if s=='7':
        c=""
        d=0
        while ligne[d]!='[':
            c+=ligne[d]
            d+=1
        d+=1
        oui = ""
        non = ""
        while ligne[d]!=']':
            oui+=ligne[d]
            d+=1
        d+=2
        while ligne[d]!=']':
            non+=ligne[d]
            d+=1
        if input()==c:
            clear()
            return oui
        clear()
        return non
    if s == ']' or s == '[':
        return "X"
    if s=='8':
        return choixaction(listes)
    if s=='9':
        print("FIN !!!")
        return "F"
    if s=='3':
        return choix(ligne)
    if s=='5':
        return ligne

def lecture(fichier,paragraphe,zone,listes) :
    resultat = str(paragraphe)
    while resultat != "X" and resultat != "F":
        p = 0
        i = 0
        while i < len(resultat) and resultat[i] != '[':
            p=p*10+ord(resultat[i])-48
            i+=1
        z = 0
        i+=1
        while (i<len(resultat) and resultat[i]!=']'):
            z=z*10+ord(resultat[i])-48
            i+=1
            zone=z
        resultat = lectureparagraphe(fichier,p,zone,listes)

#Cette boucle sert de menu principal
a=""
while a!="5":
    clear()
    print("========================================")
    print("||          NOM DU PROJET             ||")
    print("========================================")
    a = choix("Mode Histoire[0]Mode Cave Infinie[1]???[2]Instructions[3]Options[4]Quitter[5]")
    if a=="0":
        lecture(fichier,0,0,[[],[],[],[]])
    if a=="1":
        print("Le mode Cave Infinie n'est pas encore disponible.")
        input()
    if a=="2":
        print("Vous n'avez pas encore débloqué cette option.")
        input()
    if a=="3":
        print("========================================")
        print("||           INSTRUCTIONS             ||")
        print("========================================")
        print("Vous jouez à NOM DU PROJET.")
        print("Il s'agit un jeu d'aventure textuel où\nvous devrez explorer votre environnement\npour tenter de trouver des objets ou des\nindices, et ainsi debloquer de nouvelles\nzones et progresser dans le jeu.")
        print("Vous aurez pour cela besoin de faire des\nchoix. Pour cela, vous devrez, dès que\nla possibilité se présente, rentrer une\ndes commandes disponibles.")
        print("Si cela vous ennuie de recopier a chaque\nchoix un mot, vous pouvez simplifier en\nchangeant dans les options la saisie de\ndecision, qui remplacera les mots par de\nsimples chiffres.")
        print("Faites confiance à votre sens de\nl'orientation et de déduction,\nainsi qu'à votre logique !")
        input()
        clear()
    if a=="4":
        print("Il n'y a pas encore d'options.")
        input()
fichier.close()
