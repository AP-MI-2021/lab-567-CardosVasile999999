def gestioneaza_rezervari(id_rezervare, nume, clasa, pret, checkin):
    """
    Gestioneaza rezervarile unei companii aeriene
    :param id_rezervare: id-ul rezervarii trebuie sa fie unic
    :param nume: numele persoanei care a facut rezervarea
    :param clasa: clasa care poate fi doar: economy, economy plus sau business
    :param pret: pret rezervare
    :param checkin: checking facut , poate avea doar doua valori  : da/nu
    :return: o rezervare pentru companie aeriana
    """
    return [id_rezervare, nume, clasa, pret, checkin]


def get_id(rezervare):
    """
    Gett-er pentru id-ul rezervarii
    :param rezervare: rezervarea
    :return: id-ul rezervarii date ca parametru
    """
    return rezervare[0]


def get_nume(rezervare):
    """
    Gett-er pentru numele rezervarii
    :param rezervare: rezervarea
    :return: numele rezervarii date ca parametru
    """
    return rezervare[1]


def get_clasa(rezervare):
    """
    Gett-er pentru clasa rezervarii
    :param rezervare: rezervarea
    :return: clasa rezervarii date ca parametru
    """
    return rezervare[2]


def get_pret(rezervare):
    """
    Gett-er pentru pretul rezervarii
    :param rezervare: rezervarea
    :return: pretul rezervarii date ca parametru
    """
    return rezervare[3]


def get_checkin(rezervare):
    """
    Gett-er pentru checkin rezervarii
    :param rezervare: rezervarea
    :return: checkin-ul rezervarii date ca parametru
    """
    return rezervare[4]


def get_str(rezervare):
    """
    Functie de afisare
    :param rezervare: rezervarea
    :return: id-ul rezervarii date ca parametru
    """
    return f'Rezervarea cu id-ul: {get_id(rezervare)}, facuta de {get_nume(rezervare)}, pentru ' \
           f'clasa {get_clasa(rezervare)}, avand pretul {get_pret(rezervare)} si checkin: {get_checkin(rezervare)}'
