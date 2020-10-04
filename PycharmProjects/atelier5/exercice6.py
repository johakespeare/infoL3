"""
Author     : Johanna & Gwenaël
Date       : 21/09/2020
Version    : 1
Description: Atelier 5
"""

import time
import random
import matplotlib


def sort_list(list_elt:list)->list:
    liste:list=list_elt[:]
    for j in liste :
        for i in range(1,len(liste)):
            if(liste[i]<liste[i-1]):
                liste[i],liste[i-1]= liste[i-1],liste[i]
    return(liste)

# print(sort_list([9,8,7,6,5,4]))
# print(sort_list([5,9,1,4,6]))




def perf_mix(func1: callable, func2: callable, lst_size: list, nbr_exec: int = 10) -> (list, list):
    """
    Calcule performance des fonctions en parametre

    :param func1: 1ere fonction à tester
    :param func2: 2e fonction à tester
    :param lst_size: liste des tailles des listes pour les parametres
    :param nbr_exec: nombre d'execution pour les moyennes (default 10)

    :return: (perf1, perf2)
    """
    perfs_f1 = []
    perfs_f2 = []

    for size in lst_size:
        # Calule de perfs pour func1
        start_time = time.perf_counter()
        lst = [i for i in range(size)]
        for i in range(nbr_exec):
            func1(lst)

        stop_time = time.perf_counter()
        perfs_f1.append((stop_time - start_time) / nbr_exec)

        # Calcule de perfs pour func2
        start_time = time.perf_counter()
        for i in range(nbr_exec):
            func2(lst)

        stop_time = time.perf_counter()
        perfs_f2.append((stop_time - start_time) / nbr_exec)

    return (perfs_f1, perfs_f2)


def draw_graph(lst_size: list, perfs: list):
    """
    Dessine un graphique matplotlib des perfs en fonction de lst_size

    :param lst_size: Axe des abcisses
    :param perfs: Performances des fonctions
    """

    fig, ax = plt.subplots()
    ax.plot(lst_size, perfs[0], label="Fonction 1")
    ax.plot(lst_size, perfs[1], label="Fonction 2")
    ax.set(xlabel="Taille des listes", ylabel="Temps d'execution moyen", title="Graph des perfs")
    ax.legend(loc="upper center")
    plt.show()


sizes = [5, 10, 20, 40, 80, 100, 500, 1000]
perfs = perf_mix(mix_list, random.shuffle, sizes, 10)
draw_graph(sizes, perfs)