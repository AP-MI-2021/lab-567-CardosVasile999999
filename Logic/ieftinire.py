from Domain.rezervari import get_nume, get_id, gestioneaza_rezervari, get_checkin, get_pret, get_clasa


def ieftinire_rezervari_cu_check_in(lst_rezervari, procentaj):
    """
    Reduce toate rezervariile cu un anumit procentaj citit
    :param lst_rezervari: lista tuturor rezervarilor
    :param procentaj: procentajul cu care se va reduce (intre 0 si 100)
    :return: lista cu preturi reduse acolo unde este check-in facut
    """
    result = []
    check_in = False
    for rezervare in lst_rezervari:
        if get_checkin(rezervare) == 'da':
            check_in = True
            new_pret = get_pret(rezervare) - (procentaj / 100) * get_pret(rezervare)
            result.append(gestioneaza_rezervari(
                get_id(rezervare),
                get_nume(rezervare),
                get_clasa(rezervare),
                new_pret,
                get_checkin(rezervare)
            ))
        else:
            result.append(rezervare)

    if check_in is False:
        return False

    return result
