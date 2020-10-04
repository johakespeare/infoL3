import random as rd
import numpy as np
"""
algorithme simpliste et compliqué pour la machine
car pas travaillé
"""
def plusPetit(tab,debut,fin):
    indice_min = debut
    for i in range(debut+1,fin):
        if(tab[indice_min]>tab[i]):
            indice_min=i
    return(indice_min)

def tri_selection(tab,debut,fin):
    for i in range(debut,fin-1):
        indiceMin=plusPetit(tab,i,fin)
        if(indiceMin!=i):
            tmp = tab[indiceMin]
            tab[indiceMin]=tab[i]
            tab[i]= tmp
    return(tab)

if __name__ == "__main__":
    tab= np.random.randint(0,10,10)
    print("le tableau de base",tab)
    print(tri_selection(tab,0,10))

