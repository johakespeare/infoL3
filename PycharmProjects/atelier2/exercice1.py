"""auteur : Johanna Ghinevra
date : 08/09/2020
version : 1
description : atelier 2 L3"""

#exercice 1

def message_imc(imc:float)->str :
    """la fonction permet d'interpéter les imc"""
    """palier 1 correspond aux poids les plus bas, et palier 6 aux poids les plus élevés"""
    PALIER_1 =16.5
    PALIER_2=18.5
    PALIER_3=25
    PALIER_4=30
    PALIER_5=35
    PALIER_6=40

    if(imc<PALIER_1):
        msg = "dénutrition ou famine"
    elif(imc<PALIER_2):
        msg= " maigreur"
    elif(imc<PALIER_3):
        msg =" corpulence normale"
    elif(imc<PALIER_4):
        msg =" surpoids"
    elif(imc<PALIER_5):
        msg="obésité modérée"
    elif (imc<PALIER_6):
        msg="obésité sévère"
    else :
        msg="obésité morbide"

    return(msg)


def test():
    print(message_imc(26.7))
    print(message_imc(18))
    print(message_imc(704))
    print(message_imc(16.5))

test()