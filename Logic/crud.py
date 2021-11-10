from Domain.rezervari import gestioneaza_rezervari, get_clasa, get_checkin, get_pret
from Domain.rezervari import get_id


def create(lst_rezervari, id_rezervare, nume, clasa, pret, checkin, undo_list, redo_list):
    """
    Creare lista noua
    :param redo_list:
    :param undo_list: salvam lista pentru a face undo
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

    cls = ['economy', 'economy plus', 'business']
    danu = ['da', 'nu']
    if clasa not in cls:
        raise ValueError(f'{clasa} nu se afla in optiuniile: {cls}')
    if checkin not in danu:
        raise ValueError(f'Checkin-ul trebuie sa fie "da" sau "nu"')
    if pret <= 0:
        raise ValueError('Pretul trebuie sa fie mare mare decat 0')

    rezervare = gestioneaza_rezervari(id_rezervare, nume, clasa, pret, checkin)
    undo_list.append(lst_rezervari)
    redo_list.clear()
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


def update(lst_rezervari, new_rezervare, undo_list, redo_list):
    """
    Modifica o rezervare
    :param redo_list:
    :param undo_list: salvam lista pentru a face undo
    :param lst_rezervari: o rezervare pe care vrem sa o modificam
    :param new_rezervare: lista dupa modificare
    :return: lista actualizata
    """
    cls = ['economy', 'economy plus', 'business']
    danu = ['da', 'nu']
    if read(lst_rezervari, get_id(new_rezervare)) is None:
        raise ValueError(f'Nu exista o rezervare cu id-ul {get_id(new_rezervare)} in lista')

    new_rezervari = []
    for rezervare in lst_rezervari:
        if get_id(rezervare) != get_id(new_rezervare):
            new_rezervari.append(rezervare)
        else:
            new_rezervari.append(new_rezervare)

    if get_clasa(new_rezervare) not in cls:
        raise ValueError(f'{get_clasa(new_rezervare)} nu se afla in optiuniile: {cls}')
    if get_checkin(new_rezervare) not in danu:
        raise ValueError(f'Checkin-ul trebuie sa fie "da" sau "nu"')
    if get_pret(new_rezervare) <= 0:
        raise ValueError('Pretul trebuie sa fie mare mare decat 0')
    undo_list.append(lst_rezervari)
    redo_list.clear()
    return new_rezervari


def delete(lst_rezervari, id_rezervare, undo_list, redo_list):
    """
    Stergem o rezervare
    :param redo_list:
    :param undo_list: salvam lista pentru a face undo
    :param lst_rezervari: o lista de rezervari
    :param id_rezervare: id listei pe care vrem sa-l stergem
    :return: lista dupa ce am sters o rezervare
    """
    if read(lst_rezervari, id_rezervare) is None:
        raise ValueError(f'Nu exista o rezervare cu id-ul {id_rezervare} in lista')

    new_rezervari = []
    for rezervare in lst_rezervari:
        if get_id(rezervare) != id_rezervare:
            new_rezervari.append(rezervare)

    undo_list.append(lst_rezervari)
    redo_list.clear()
    return new_rezervari
