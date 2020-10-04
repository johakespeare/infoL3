""" @auteur : johanna
date : 10/09/2020
description : atelier3 exercice 2
version 1
"""

import math
from math import *

def position_1(L,e):
    taille = len(L)
    compteur = -1
    for i in range (0,taille):
        if L[i]==e:
            compteur=i
    return(compteur)


def position_2(L,e):
    i=0
    taille = len(L)
    compteur=-1
    while i<taille:
        if L[i]==e:
            compteur=i
        i+=1
    return(compteur)



def test_position():
    L=[7,12,3,0,4]
    L2=[8,16,2,1]
    L3=[5615,6848,3]
    print(position_1(L,3))
    print(position_2(L,7))
    print(position_1(L2, 7))
    print(position_2(L2, 7))
    print(position_1(L3, 6848))
    print(position_2(L3, 6848))


def nb_occurences(L,e):
    taille = len(L)
    compteur = 0
    for i in range(0, taille):
        if L[i] == e:
            compteur +=1
    return (compteur)

def test_occurence():
    L=[1,1]
    L2=[2,8,5,9,1,9]
    L3=[1,2,9,4]

    print(nb_occurences(L,1))
    print(nb_occurences(L,0))

    print(nb_occurences(L2, 9))
    print(nb_occurences(L2, 0))

    print(nb_occurences(L3, 1))
    print(nb_occurences(L3, 0))




def est_triee(L):
    taille = len(L)
    est_croissant = True
    for i in range(0,taille-1):
        if(L[i]>L[i+1]):
            est_croissant=False
    return(est_croissant)


def test_est_triee():
    L=[0,1,2,3,4]
    print(est_triee(L))
    L=[2,8,65,0,1]
    print(est_triee(L))


def est_triee_2(L):
    est_croissant=True
    taille = len(L)
    i=0
    fin = False
    while fin != True :
        print(i)
        if(L[i+1]<L[i]):
            est_croissant=False
            fin = True
        if i==taille-2:
            fin = True
        else:
            i+=1
    return(est_croissant)

def test_est_triee_2():
    L=[0,1,2,3,4]
    print(est_triee_2(L))
    L=[2,8,65,0,1]
    print(est_triee_2(L))

def a_repetitions(L):
    T=[]
    repetition = False
    while (repetition == False) or (len(T)!=len(L)):
        for element in L:
            if not(element in T):
                T.append(element)
            else:
                repetition = True
    return(repetition)

def position_tri(L,e):
    taille = len(L)
    res = 0
    taille2 = floor(taille/2)

    if e< L[taille2] :
        Liste2 =[]
        for i in range(0,taille2):
            Liste2.append(L[i])
        res = position_tri(Liste2,e)
    elif e > L[taille2]:
        Liste2 =[]
        for i in range(taille2,taille):
            Liste2.append(L[i])
        res = position_tri(Liste2, e) + taille2

    elif e == L[taille2]:
        res = taille2

    else:
        res = -1

    return(res)


def test_position_tri():
    L2 = [2, 8,  9, 19]
    print(position_tri(L2,2))
    L2 = [2, 8, 9, 19]
    print(position_tri(L2, 19))
    L2 = [2, 8, 9, 19]
    print(position_tri(L2, 9))
    L2 = [8, 9, 19]
    print(position_tri(L2, 8))



test_position_tri()

def test_a_repetitions():
    L = [1, 1]
    L2 = [2, 8, 5, 9, 1]
    L3 = [1, 2, 9, 4]
    print(a_repetitions(L))
    print(a_repetitions(L2))
    print(a_repetitions(L3))

    print("L/2")
    print(L/2)
    print(L2/2)

test_a_repetitions()

