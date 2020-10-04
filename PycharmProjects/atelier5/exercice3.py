"""
auteurs : Johanna et Gwen
date : 21/09
description : atelier5 exo3
version:1
"""
from random import randint

def choose_element_list(list_in_wich_to_choose:list):
    """
    retourne un élément aléatoire de la fonction
    :param list_in_wich_to_choose: une liste
    :return: un élément de la liste
    """
    return list_in_wich_to_choose[randint(0,len(list_in_wich_to_choose)-1)]

#
# #test
# lst_sorted=[0,1,2,3,4,5,6,7,8,9,10]
# print('Liste triée au départ', lst_sorted)
# e1 = choose_element_list(lst_sorted)
# print('à la première éxecution', e1 , ' a été selectionné')
# e2 = choose_element_list(lst_sorted)
# print('à la seconde éxecution', e2 , ' a été selectionné')
# assert e1 != e2
