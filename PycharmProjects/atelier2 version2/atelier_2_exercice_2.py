# -*- coding: utf-8 -*-
"""
#auteur : Johanna Ghinevra
#date : 08/09/2020
#version : 1
#description : atelier 2 L3
"""

#exercice 2

def est_bissextile(année:int)->bool :
    """ la fonction retourne true si l'année est bissextile, false sinon,
    une année est bissextile si elle est divisible par 4 et pas par 100 ou bien
    divisible par 400"""

    if((année%4==0)and(année%100!=0))or(année%400==0):
        return(True)
    else :
        return(False)

    #ou return((année%4==0)and(année%100!=0))or(année%400==0))

def test():
    """fonction destinée à tester la fonction est_bissextile"""
    print("test année bissextile, divisible par 4 mais pas par 100 :  ", est_bissextile(2020))
    print("test année non bissextile, divisible ni par 4 ni par 100 ni par 400 : ", est_bissextile(2019))
    print("test année bissextile divisible par 400 : ", est_bissextile(400))
    
test()
    
    

