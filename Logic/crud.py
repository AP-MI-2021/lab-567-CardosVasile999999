from Domain.rezervari import gestioneaza_rezervari
from Domain.rezervari import get_id


def create(lst_rezervari, id_rezervare, nume, clasa, pret, checkin):
    """
    Creare lista noua
    :param lst_rezervari: lista tutror persoanelor cu rezervari
    :param id_rezervare: id-ul rezervarii trebuie sa fie unic
    :param nume: numele persoanei care a facut rezervarea
    :param clasa: clasa care poate fi doar: economy, economy plus sau business
    :param pret: pret rezervare
    :param checkin: checking facut , poate avea doar doua valori  : da/nu
    :return: Creaza fiecare element rezervare in parte
    """
    if read(lst_rezervari, id_rezervare) is not None:
        raise ValueError(f'Exista deja o rezervare cu id-ul {id_rezervare}')

    rezervare = gestioneaza_rezervari(id_rezervare, nume, clasa, pret, checkin)
    return lst_rezervari + [rezervare]


def read(lst_rezervari, id_rezervare=None):
    """
    Citire o rezervare
    :param lst_rezervari: lista de rezervari
    :param id_rezervare: id rezervarii respective
    :return:
         - rezervarea cu id_rezervare, daca exista
         -lista cu toate rezervariile daca id_rezervare = None
         -None daca nu exista o rezervare cu id_rezervare
    """

    if not id_rezervare:
        return lst_rezervari

    rezervare_cu_id = None
    for rezervare in lst_rezervari:
        if get_id(rezervare) == id_rezervare:
            rezervare_cu_id = rezervare

    if rezervare_cu_id:
        return rezervare_cu_id
    return None


def update(lst_rezervari, new_rezervare):
    """
    Modifica o rezervare
    :param lst_rezervari: o rezervare pe care vrem sa o modificam
    :param new_rezervare: lista dupa modificare
    :return: lista actualizata
    """
    new_rezervari = []
    for rezervare in lst_rezervari:
        if get_id(rezervare) != get_id(new_rezervare):
            new_rezervari.append(rezervare)
        else:
            new_rezervari.append(new_rezervare)

    return new_rezervari


def delete(lst_rezervari, id_rezervare):
    """
    Stergem o rezervare
    :param lst_rezervari: o lista de rezervari
    :param id_rezervare: id listei pe care vrem sa-l stergem
    :return: lista dupa ce am sters o rezervare
    """
    new_rezervari = []
    for rezervare in lst_rezervari:
        if get_id(rezervare) != id_rezervare:
            new_rezervari.append(rezervare)

    return new_rezervari
