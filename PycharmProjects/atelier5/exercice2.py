"""
Author     : Johanna & Gwenaël
Date       : 21/09/2020
Version    : 1
Description: Atelier 5
"""

from random import randint


def mix_list(list_to_mix: list) -> list:
    """
    Mélange la liste
    :param list_to_mix: Liste à mélanger
    :return: Liste mélanger
    """

    buff: list = []
    liste: list = list_to_mix[:]
    for i in range(len(list_to_mix)):
        aleatoire: int = randint(0, len(liste) - 1)
        buff.append(list_to_mix[aleatoire])
        liste.pop(aleatoire)

    return buff

# for i in range(len(list_to_mix)):
#   j=randint(i,len(list_to_mix)-1)
#   mixed_list[i],mixed_list[j]= mixed_list[j],mixted_list[i]


def test_mix():
    lst = [i for i in range(100)]
    print(f"Sorted lst: {lst} --> randomized {mix_list(lst)}")
    lst = [i for i in range(-10, 10, 2)]
    print(f"Sorted lst: {lst} --> randomized {mix_list(lst)}")


test_mix()