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
