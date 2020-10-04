# -*- coding: utf-8 -*-
"""
#auteur : Johanna Ghinevra
#date : 08/09/2020
#version : 1
#description : atelier 2 L3


"""

from math import *

#exercice 3

def discriminant(a:float,b:float,c:float)->float:
    """ la fonction discriminant calcule delta"""
    return(b**2 - (4*a*c))

def racine_unique(a:float,b:float)->float:
    """la fonction racine_unique calcule la racine unique"""
    if(a!=0):
        return(-b/(2*a))
    else:
        return(0)

def racine_double(a : float,b : float ,delta : float ,num : int)->float:
    """la fonction racine_double calcule une des racines doubles (selon num),
    on part du principe que a ne peut être différent de 0"""
    if(num==1):
        return(( -b + sqrt(delta))  /  (2*a))
    elif(num==2):
        return((-b - sqrt(delta))/(2*a))



def str_equation(a : float ,b: float,c: float)->str:
    """ la fonction str_equation retourne l'équation en str, si
    a ou b=0 on ne note pas les x, si c=0 on ne note pas le +"""

    if(a!=0): # comme a!=0 on peut virer ça et ne mettre que msg=......
        msg = str(a) + "x²"

    if(b!=0):
        msg += "+" + str(b) + "x"

    if(c!=0):
        msg +=  "+"+ str(c)

    return( msg +"=0")

def solution_equation(a:float,b:float,c:float)->str:
    """ la fonction solution_equation retourne le nombre de racine"""
    msg= " solution de l'équation" + str_equation(a,b,c)

    if(discriminant(a,b,c)==0): 
        return(msg+" solution unique, x=")
    elif(discriminant(a,b,c)>0):
        return(msg + " deux racines, x1= ")
    else:
        return(msg + " pas de solution réelle")

def equation(a:float,b:float,c:float)->str:
    """ la fonction equation retourne la solution de l'équation à l'aide
    des fonctions précédentes """
    if (discriminant(a, b, c) == 0):
        return ( solution_equation(a,b,c) + str(racine_unique(a,b)))
    elif (discriminant(a, b, c) > 0):
        return (solution_equation(a, b, c) + str(racine_double(a, b, discriminant(a,b,c),1)) + " et x2= "+ str(racine_double(a,b,discriminant(a,b,c),2)))
    else:
        return (solution_equation(a, b, c) )



def test():
    print("cas où il y'a 2 racines")
    print(equation(1,25,1))
    print(equation(10, 47, 2))
    print("cas où il n'y a pas de solution réelle")
    print(equation(5, 2, 15))
    print(equation(78, 3, 10))
    print("cas où il y'a une solution unique")
    print(equation(1, 2, 1))

test()



