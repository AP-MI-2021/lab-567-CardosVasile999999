from Domain.rezervari import get_nume, get_id, gestioneaza_rezervari, get_checkin, get_pret, get_clasa


def ieftinire_rezervari_cu_check_in(lst_rezervari, procentaj, undo_list, redo_list):
    """
    Reduce toate rezervariile cu un anumit procentaj citit
    :param undo_list: lista pentru undo
    :param lst_rezervari: lista tuturor rezervarilor
    :param procentaj: procentajul cu care se va reduce (intre 0 si 100)
    :return: lista cu preturi reduse acolo unde este check-in facut
    """
    if procentaj <= 0 or procentaj >= 100:
        print(f'{procentaj} nu se afla intre 0 si 100')
        return lst_rezervari
    result = []
    for rezervare in lst_rezervari:
        if get_checkin(rezervare) == 'da':
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
    undo_list.append(lst_rezervari)
    redo_list.clear()
    return result
