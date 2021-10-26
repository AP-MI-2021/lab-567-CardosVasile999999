from Domain.rezervari import gestioneaza_rezervari
from Domain.rezervari import get_id

def create(lst_rezervari, id_rezervare, nume, clasa, pret, checkin):
    """

    :param lst_rezervari:
    :param id_rezervare:
    :param nume:
    :param clasa:
    :param pret:
    :param checkin:
    :return:
    """
    rezervare = gestioneaza_rezervari(id_rezervare, nume, clasa, pret, checkin)
    return lst_rezervari + [rezervare]


def read(lst_rezervari, id_rezervare=None):
    """

    :param lst_rezervari:
    :param id_rezervare:
    :return:
    """
    rezervare_cu_id = None
    for rezervare in lst_rezervari:
        if get_id(rezervare) == id_rezervare:
            rezervare_cu_id = rezervare

    if rezervare_cu_id:
        return rezervare_cu_id
    return lst_rezervari
