"""
Author     : Johanna & Gwenaël
Date       : 15/09/2020
Version    : 1
Description: Atelier 4 exercice 5
"""

def ouvrante(car:str)->bool:
    """ fonction vérifiant si le caractère est une parenthèse,crochet ou accolade ouvrante"""
    return(car=="("or car=="{" or car=="[")


def fermante(car:str)->bool:
    """ fonction vérifiant si le caractère est une parenthèse,crochet ou accolade fermante"""
    return(car==")"or car=="}" or car=="]")

def renverse(car:str)->str:
    """ fonction retournant un caractère, si c'est une parenthèse,un crochet ou accolade, renvoie son inverse
    sinon renvoie le caractère de départ"""
    if not(fermante(car) or ouvrante(car)):
        retour= car
    elif fermante(car):
        if(car=='}'):
            retour='{'
        elif(car==')'):
            retour='('
        else:
            retour='['
    else :
        if(car=='{'):
            retour='}'
        elif(car=='('):
            retour=')'
        else:
            retour=']'
    return(retour)


def operateur(car:str)->bool:
    """ fonction vérifiant si le caractère est un opérateur"""
    return (car == "+" or car == "-" or car == "*" or car=="/")

def nombre(car:str)->bool:
    """ fonction vérifiant si le caractère est un entier positif"""
    return(car.isdigit())

def caractere_valide(car:str)->bool:
    """fonction vérifiant si le caractère est valide """
    return(ouvrante(car)or fermante(car) or operateur(car) or nombre(car) or car==" ")

def verif_parenthese(expression:str)->bool:
    """ fonction vérifiant si la chaîne est algébriquement correcte"""
    isOk= True
    P=[]
    for i in expression:
        if not caractere_valide(i):
            isOk= False
        elif ouvrante(i) :
            P.append(i)
        elif fermante(i):
            if(P[-1]==renverse(i)):
                P.pop()
            else:
                isOk=False
    if(len(P)>0):
        isOk= False
    return(isOk)


print(verif_parenthese("((3+2)*6-1"))


