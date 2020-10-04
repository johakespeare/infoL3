"""
auteur : Johanna Fericean
date : 17/09/2020
version : 1
description : bilan atelier 3
"""

def fill_list(b_inf:int,b_sup:int,max_len:int)->list:
    """ cette fonction permet de créer une liste avec des nombres rentrés par l'utilisateur
    compris entre l'intervalle b_inf et b_sup
    elle retourne donc la liste  L[]   """
    L=[] # on initie une liste vide dans laquelle on mettra nos valeurs
    pas_intervalle=-1 # on initie notre condition d'arrêt, si elle est égale à 1, la boucle while s'arrêtera
    while len(L)<max_len or pas_intervalle==1 :
        i = input("donnez un nombre") #on demande à l'utilisateur de rentrer un nombre
        if i.isdigit(): # si c'est un chiffre, alors on vérifie si il est présent dans l'intervalle
            if(int(i)<=b_sup)and(int(i)>=b_inf):
                L.append(i) #on ajoute le nombre de l'utilisateur dans la liste
            else:
                print(" le nombre n'appartient pas à l'intervalle") # si le nombre n'est pas compris dans l'intervalle, on sort de la boucle
                pas_intervalle = 1
        else:
            print("i n'est pas un nombre") #si ce n'est pas un nombre on sort de la boucle
            pas_intervalle=1
    return(L)


def test_fill():
    """ cette fonction permet de tester la fonction fill_list
       on choisit  2 intervalles, [0,20] pour les 3premiers tests puis [0,1000] pour les suivants """
    CONSTANTE_DEBUT = 0
    CONSTANTE_FIN= 20
    CONSTANTE_DEBUT_2 = 0
    CONSTANTE_FIN_2 = 1000
    TAILLE_MAX= 10
    print("test 1")
    # on teste avec que des valeurs comprises entre 0 et 20
    print(fill_list(CONSTANTE_DEBUT,CONSTANTE_FIN,TAILLE_MAX))
    print("test 2")
    # on teste avec des valeurs non comprses dans l'intervalle(sauf la première)
    print(fill_list(CONSTANTE_DEBUT, CONSTANTE_FIN, TAILLE_MAX))
    print("test 3")
    #on saisie de suite une valeur incorrecte
    print(fill_list(CONSTANTE_DEBUT, CONSTANTE_FIN, TAILLE_MAX))

    #on teste avec des intervalles plus grandes
    print("on teste avec des intervalles plus grandes")
    print("test 1")
    # on teste avec que des valeurs comprises entre 0 et 1000
    print(fill_list(CONSTANTE_DEBUT_2, CONSTANTE_FIN_2, TAILLE_MAX))
    print("test 2")
    # on teste avec des valeurs non comprses dans l'intervalle(sauf la première)
    print(fill_list(CONSTANTE_DEBUT_2, CONSTANTE_FIN_2, TAILLE_MAX))
    print("test 3")
    # on saisie de suite une valeur incorrecte
    print(fill_list(CONSTANTE_DEBUT_2, CONSTANTE_FIN_2, TAILLE_MAX))


#on appelle notre fonction test
test_fill()