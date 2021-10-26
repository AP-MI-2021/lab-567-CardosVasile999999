def gestioneaza_rezervari(id_rezervare, nume, clasa, pret, checkin):
    """
    Gestioneaza rezervarile unei companii aeriene
    :param id_rezervare: id-ul rezervarii trebuie sa fie unic
    :param nume: numele persoanei care a facut rezervarea
    :param clasa: clasa care poate fi doar: economy, economy plus sau business
    :param pret: pret rezervare
    :param checkin: checking facut , poate avea doar doua valori  : DA/NU
    :return: o rezervare pentru companie aeriana
    """
    return {
        'id': id_rezervare,
        'nume': nume,
        'clasa': clasa,
        'pret': pret,
        'checkin': checkin
    }


def get_id(rezervare):
    """
    Gett-er pentru id-ul rezervarii
    :param rezervare: rezervarea
    :return: id-ul rezervarii date ca parametru
    """
    return rezervare['id']


def get_nume(rezervare):
    """
    Gett-er pentru numele rezervarii
    :param rezervare: rezervarea
    :return: numele rezervarii date ca parametru
    """
    return rezervare['nume']


def get_clasa(rezervare):
    """
    Gett-er pentru clasa rezervarii
    :param rezervare: rezervarea
    :return: clasa rezervarii date ca parametru
    """
    return rezervare['clasa']


def get_pret(rezervare):
    """
    Gett-er pentru pretul rezervarii
    :param rezervare: rezervarea
    :return: pretul rezervarii date ca parametru
    """
    return rezervare['pret']


def get_checkin(rezervare):
    """
    Gett-er pentru checkin rezervarii
    :param rezervare: rezervarea
    :return: checkin-ul rezervarii date ca parametru
    """
    return rezervare['checkin']


def get_str(rezervare):
    """
    Gett-er pentru id-ul rezervarii
    :param rezervare: rezervarea
    :return: id-ul rezervarii date ca parametru
    """
    return f'serbus {get_id(rezervare)}'
