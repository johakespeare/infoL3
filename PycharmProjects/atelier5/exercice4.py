"""
auteurs : Johanna et Gwen
date : 21/09
description : atelier5 exo4
version:1
"""
from random import randint
from typing import*

def extract_elements_list(list_in_wich_to_choose:list,int_nbr_of_element_to_extract:int)->List[Any]:
    """
    fonction qui retourne une liste d'éléments piochés dans la liste placée en paramètres
    :param list_in_wich_to_choose:  liste dans laquelle on va piocher les éléments
    :param int_nbr_of_element_to_extract: le nombre d'éléménents que l'on pioche
    :return: liste des éléments piochés
    """
    List_indice=[]
    List_sortie=[]
    intervalle = len(list_in_wich_to_choose)-1
    while len(List_sortie)!=int_nbr_of_element_to_extract:
        n= randint(0,intervalle)
        if not n in List_indice : # vaut mieux depop les indices de la lsite indice, au lieu de reparcourir la boucle
            List_sortie.append(list_in_wich_to_choose[n])
            List_indice.append(n)
    return(List_sortie)

print(extract_elements_list([0,1,2,3,4,5,6,7,8,9,10],5))
print(extract_elements_list(["caca","proute","carotte","capote","chaton"],3))

# mélanger la liste, prendre les 5premiers éléments

def extract_elements_list2(list_in_wich_to_choose:list,int_nbr_of_element_to_extract:int)->List[Any]:
    """
    fonction qui retourne une liste d'éléments piochés dans la liste placée en paramètres
    :param list_in_wich_to_choose:  liste dans laquelle on va piocher les éléments
    :param int_nbr_of_element_to_extract: le nombre d'éléménents que l'on pioche
    :return: liste des éléments piochés
    """
    List_entree=list_in_wich_to_choose[:]
    List_sortie=[]
    while len(List_sortie)!=int_nbr_of_element_to_extract:
        n= randint(0, len(List_entree )-1)
        List_sortie.append(list_in_wich_to_choose[n])
        List_entree.pop(n)
    return(List_sortie)

print(extract_elements_list2([0,1,2,3,4,5,6,7,8,9,10],5))
print(extract_elements_list2(["caca","proute","carotte","capote","chaton"],3))

