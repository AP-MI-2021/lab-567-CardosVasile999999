from Domain.rezervari import get_pret, get_clasa


def get_maximum_price_from_every_class(rezervari):
    """
    Determina pretul maxim pentru fiecare clasa
    :param rezervari: lista de rezervari
    :return: pretul maxim pentru fiecare rezervare
    """
    maxim = [-1] * 3
    for rezervare in rezervari:
        clasa = get_clasa(rezervare)
        pret = get_pret(rezervare)
        if clasa == 'economy' and pret > maxim[0]:
            maxim[0] = pret
        elif clasa == 'economy plus' and pret > maxim[1]:
            maxim[1] = pret
        elif clasa == 'business' and pret > maxim[2]:
            maxim[2] = pret

    return maxim
