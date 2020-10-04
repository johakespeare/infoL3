"""
Author     : Johana & Gwenaël
Date       : 15/09/2020
Version    : 1
Description: Atelier 4 exercice 3
"""

from exercice2 import *
from random import choice
from os import path



def placesLettre(char:str,mot:str)->list:
    """
       Renvoie les indices désignant la place du caractère dans le  mot (ou une liste vide si le caractère n'est pas présent.
       Keyword Arguments:
       char-- le caractère
       mot -- le mot où on cherche la place du caractère
       Return:
       Retourne les indices désignant la place du caractère
       """
    index = []
    for i in enumerate (mot):
        if i[1].lower() == char.lower():
            index.append(i[0])
    return index

# print(placesLettre('b','bonjour'))
# print(placesLettre('a','bonjour'))
# print(placesLettre('m','maman'))

def outputStr(mot:str)->str:
    retour_mot=""
    for i in range(len(mot)):
        if mot[i] in [" ","_","-"]:
            retour_mot+= mot[i]
        else:
            retour_mot+="_"
    return(retour_mot)


#print(outputStr('bonjour'))
#print(outputStr('non binaire'))
#print(outputStr('maman'))
def pendu(err:int):
    C=['|---]', '|  o', '|  T ', '| / \\', '|_____']
    for i in range(err):
        print(C[i])

def buildDict(filename: str) -> dict:
    """
       Construit le dictionnaire à l'aide d'un fichier texte
       Keyword Arguments:
       filename-- le fichier texte
       Return:
       Retourne un dictionnaire
           """
    dico = {}
    if (path.exists(filename)):
        file = open(filename, "r")
        content = file.readline()
        file.close()
        dico = eval(content)
    return (dico)


def runGame(difficulty : int):
    dico = buildDict("./texte")
    DIFF = [1, 7, 9, 100]
    continuer = True
    mot=("", 0)
    while continuer:
        mot = choice(dico)
        if DIFF[difficulty-1] <= mot[1] < DIFF[difficulty]:
            continuer = False

    erreur = 0
    mot_display= outputStr(mot[0])
    gagne=False

    while erreur<5 and not gagne:
        print(mot_display)
        if(erreur==4):
            print("dernière chance !")
        essai = str(input("donnez une lettre"))
        tab=placesLettre(essai,mot[0])
        if (len(tab)>0):
            mot_display = list(mot_display)
            for i in tab:
                mot_display[i]=essai
            mot_display="".join(mot_display)
        else:
            erreur+=1
            pendu(erreur)

        if "_" not in mot_display:
            gagne = True
    if gagne :
        print("tu as gagné avec "+str(erreur)+" erreur(s)")
    else:
        print("tu as perdu !!!! :( ")
        print("le mot était "+ str(mot[0]))




print("Choisir un niveau de difficulté")
print("[1] - Facile")
print("[2] - intermédiaire")
print("[3] - trop dur pour toi")
diff = int(input("choisissez votre difficulté"))
runGame(diff)


