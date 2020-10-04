"""
Author     : Johana & Gwenaël
Date       : 15/09/2020
Version    : 1
Description: Atelier 4
"""
#exercice 1

def full_name(str_arg:str)->str :
    """
           Renvoie le nom en majuscule et le prénom avec la première lettre en majuscule
           Keyword Arguments:
           str_arg-- le nom et le prénom
           Return:
           Retourne le nom et le prénom avec les modifications
               """
    tab=str_arg.split(" ")
    tab[0]=tab[0].upper()
    tab[1]=tab[1].capitalize()
    return "{} {}".format(tab[0],tab[1])

#print(full_name("fericean émile"))

def is_mail(str_arg:str)->(int,int):
    """
           Vérifie si le mail est valide
           Keyword Arguments:
           str_arg-- l'adresse mail
           Return:
           Retourne un tuple avec un code d'erreur
               """
    VALIDITE = (1,"x")
    ERREUR_CORPS = (0,1)
    ERREUR_AROBASE = (0,2)
    ERREUR_DOMAINE =(0,3)
    ERREUR_POINT = (0,4)
    TAB_CARACTERE = ["-","_","."]
    valide= VALIDITE

    if not '@' in str_arg :
        valide= ERREUR_AROBASE
    else:
        str_arg= str_arg.split("@")
        if "." in str_arg[1]:
            if len(str_arg[0]) > 0:
                for lettre in str_arg[0]:
                    if not (lettre.isalpha() or lettre.isnumeric() or lettre in TAB_CARACTERE):
                        valide= ERREUR_CORPS
            else:
                valide = ERREUR_CORPS
            if valide[1]==0 :
                if(str_arg[1]=="")or(len(str_arg[1])<3):
                    for lettre in str_arg[1]:
                        if not (lettre.isalpha() or lettre.isnumeric() or lettre in TAB_CARACTERE):
                            valide= ERREUR_DOMAINE
        else:
            valide=ERREUR_POINT

    return(valide)

# print(is_mail("adqfsgfn"))
# print(is_mail("johananfericean@gmail.com"))

def test_is_mail():
    MAIL_TEST = [
        "bisgambiglia_paul@univ-corse.fr",
        "bisgambiglia_paulOuniv-corse.fr",
        "bisgambiglia_paul@univ-corsePOINTfr",
        "@univ-corse.fr",
        "bisgam@f<!!!d.fr"
    ]

    for mail in MAIL_TEST:
        print(f"is_mail({mail}) -> {is_mail(mail)}")

test_is_mail()

