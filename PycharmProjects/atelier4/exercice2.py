"""
Author     : Johanna & Gwenaël
Date       : 15/09/2020
Version    : 1
Description: Atelier 4
"""
from random import randint
from os import path


# exercice 2

def mots_Nlettres(lst_mot: list, n: int) -> list:
    """
    Cherche les mots contenant n lettres dans lst_mot
    Keyword argument:
    lst_mot -- Liste de mots
    n -- Nombre de caractere que doit contenir le mot
    Return Liste contenant les mots de n caractéres
    """

    lst_retour = []
    for mot in lst_mot:
        if len(mot) == n:
            lst_retour.append(mot)

    return lst_retour


def test_Nlettres():
    LST = [
        "jouer", "bonjour", "punir", "jour", "revoir", "aurevoir", "pouvoir",
        "cour", "abajour", "finir", "aimer"
    ]
    for i in range(2):
        n = randint(4, 8)
        print(f"n={n} -> {mots_Nlettres(LST, n)}")


# test_Nlettres()

def commence_par(mot: str, prefix: str) -> bool:
    """
    Verifie si mot commence par prefix
    Keyword argument:
    mot -- Mot à vérifier
    prefix -- prefixe rechercher
    Return True si le prefixe est trouver, False sinon
    """

    debut_mot = mot[0:len(prefix)]
    found = False
    if prefix == debut_mot:
        found = True

    return found


def test_commence():
    for i in range(3):
        mot = input("mot ")
        prefix = input("prefix ")
        print(commence_par(mot, prefix))


# test_commence()

def finit_par(mot: str, suffixe: str) -> bool:
    """
    Verifie si mot finit par suffixe
    Keyword argument:
    mot -- Mot à vérifier
    suffixe -- suffixe rechercher
    Return True si le suffixe est trouver, False sinon
    """

    fin_mot = mot[len(mot) - len(suffixe):len(mot)]
    found = False
    if suffixe == fin_mot:
        found = True

    return found


def test_finit():
    for i in range(3):
        mot = input("mot ")
        suffixe = input("suffixe ")
        print(finit_par(mot, suffixe))


def finissent_par(lst_mot: list, suffixe: str) -> list:
    """
    Renvoi la liste de mot contenue dans lst_mot se terminant par suffixe
    Keyword argument:
    lst_mot -- Liste de mots
    suffixe -- suffixe rechercher
    """

    lst_retour = []
    for mot in lst_mot:
        if finit_par(mot, suffixe):
            lst_retour.append(mot)

    return lst_retour


def commencent_par(lst_mot: list, prefixe: str) -> list:
    """
    Renvoi la liste de mot contenue dans lst_mot commencant par prefixe
    Keyword argument:
    lst_mot -- Liste de mots
    prefixe -- prefixe rechercher
    """

    lst_retour = []
    for mot in lst_mot:
        if commence_par(mot, prefixe):
            lst_retour.append(mot)

    return lst_retour


def liste_mots(lst_mot: list, prefixe: str, suffixe: str, n: int) -> list:
    """
    Function Description
    Keyword argument:
    param -- param Description
    Return Return description
    """

    lst_retour = mots_Nlettres(lst_mot, n)
    lst_retour = commencent_par(lst_retour, prefixe)
    lst_retour = finissent_par(lst_retour, suffixe)
    return lst_retour


def test_mot():
    LST = [
        "jouer", "bonjour", "punir", "jour", "revoir", "aurevoir", "pouvoir",
        "cour", "abajour", "finir", "aimer"
    ]
    print(liste_mots(LST, "a", "r", 5))


# test_mot()

def dictionnaire(fichier: str) -> list:
    """
    Lit le contenue d'un fichier et retourne son contenue sous forme de liste
    Keyword argument:
    fichier -- Chemin d'accés (locale ou absolue) vers le fichier
    """
    lst = []
    if path.exists(fichier) and path.isfile(fichier):
        with open(fichier, "r") as file:
            line = file.readline()
            while line != "":
                lst.append(line.replace('\n', ''))
                line = file.readline()

    return lst


#print(dictionnaire("./Atelier4/littre.txt"))