"""
Author     : Johanna & Gwenaël
Date       : 21/09/2020
Version    : 1
Description: Atelier 5
"""

# l  = [1, 2, 3, 4]
# l2 = l[:] -> copie réel de l (cf. i.mutabilité des objets)

from random import randint

def gen_list_random_int(int_binf:int = 0, int_bsup:int = 10, int_nbr:int = 10) -> list:
    """
    Génére une liste de nombre aléatoire
    :param int_binf: Borne inférieure incluse (defaut 0)
    :param int_bsup: Borne supérieure excluse (defaut 10)
    :param int_nbr: Nombre d'élément de la liste (defaut 10)
    :return: Liste de int_nbr nombres aléatoire générer entre int_binf et int_bsup
    """

    lst:list = []
    for i in range(int_nbr):
        lst.append(randint(int_binf, (int_bsup - 1)))

    return lst

gen_list_random_int()
print(gen_list_random_int())
print(gen_list_random_int(-10, 10, 20))
print(gen_list_random_int(-100, 100, 10000))