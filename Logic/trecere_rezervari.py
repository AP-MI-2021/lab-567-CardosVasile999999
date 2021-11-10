from Domain.rezervari import get_nume, get_id, gestioneaza_rezervari, get_checkin, get_pret, get_clasa


def trecere_rezervari_la_o_clasa_superioara(lst_rezervari, nume, undo_list, redo_list):
    """
    trece toate rezervariile pe un nume citit la o clasa superioara
    :param redo_list: lista pentru redo
    :param undo_list: lista pentru undo
    :param lst_rezervari: lista de rezervari
    :param nume: numele pe care s-a facut rezervarea
    :return: lista actualizata cu clasa superioara
    """
    result = []
    for rezervare in lst_rezervari:
        if nume in get_nume(rezervare):
            if get_clasa(rezervare) == "economy":
                result.append(gestioneaza_rezervari(
                    get_id(rezervare),
                    get_nume(rezervare),
                    "economy plus",
                    get_pret(rezervare),
                    get_checkin(rezervare)
                ))
            elif get_clasa(rezervare) == "economy plus":
                result.append(gestioneaza_rezervari(
                    get_id(rezervare),
                    get_nume(rezervare),
                    "business",
                    get_pret(rezervare),
                    get_checkin(rezervare)
                ))
        else:
            result.append(rezervare)
    undo_list.append(lst_rezervari)
    redo_list.clear()
    return result
