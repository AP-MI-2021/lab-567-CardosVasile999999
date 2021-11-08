from Domain.rezervari import get_pret, get_clasa


def get_maximum_price_from_every_class(rezervari):
    """
    Determina pretul maxim pentru fiecare clasa
    :param rezervari:
    :return:
    """
    maxim = {
        "economy": 0,
        "economy plus": 0,
        "business": 0
    }
    for rezervare in rezervari:
        if get_pret(rezervare) > maxim[get_clasa(rezervare)]:
            maxim[get_clasa(rezervare)] = get_pret(rezervare)

    return maxim
