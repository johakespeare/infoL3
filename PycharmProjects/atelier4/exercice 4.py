"""
Author     : Johanna & Gwenaël
Date       : 15/09/2020
Version    : 1
Description: Atelier 4 exercice 4
"""

def mot_correspond(mot : str, motif : str)->bool:
    """ retourne True si le mot a le même motif passé en paramètre"""
    correspond = True
    if(len(mot)==len(motif)):
        for i in range(0,len(mot)):
            if(motif[i]!="."):
                if motif[i]!=mot[i]:
                    correspond=False
                    break
    else:
        correspond = False
    return correspond


#print(mot_correspond("tarte","t.a."))

def presente(lettre:str, mot:str)->int:
    """ vérifie si la lettre est présente dans le mot"""
    return(mot.find(lettre))


def mot_possible(mot:str,lettres:str)->bool:
    """ retourne vrai si on peut former le mot avec les lettres de la liste"""
    retour = False
    L=[]
    for i in lettres:
        if presente(i,mot)!=-1 :
            L.append(i)
    if len(L)>=len(mot):
        retour = True

    return(retour)

def mots_optimaux(dico:list,lettres:str)->list:
    """ retourne les mots les plus grands contenant les lettres mises en paramètre"""
    L=[""]
    for i in dico:
        if(mot_possible(i,lettres)):
            if(len(L[-1])<len(i)):
                L.clear()
                L.append(i)
            elif (len(L[-1])==len(i)):
                L.append(i)

    return(L)

liste=['abricot','carotte','tortue','dentifrice','dents','brosse','montre','trottoir','table','lit','yeux','balcon','bouteille','acabler','cablera']
# print(mot_possible("lapin","pfdagpinl") )
# print(mot_possible("lapin","coq"))
#
# print(mot_possible("chapeau","abcehpuv"))
# print(mot_possible("chapeau","abcehpuva"))

print(mots_optimaux(liste,"abricotue"))
print(mots_optimaux(liste,"ertyhezfaoeuie"))
print(mots_optimaux(liste,"cablera"))
