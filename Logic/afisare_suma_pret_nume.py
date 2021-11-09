from Domain.rezervari import get_nume, get_pret


def show_sum_of_all_prices_by_name(rezervari):
    """
    Afisarea sumelor preturilor fiecarui nume din lista
    :param rezervari: lista de rezervari
    :return: o lista cu suma preturilor fiecarui nume din lista si numele caruia ii corespunde
    """
    nume = []
    result = []
    for rezervare in rezervari:
        prenume = get_nume(rezervare)
        if prenume not in nume:
            nume.append(prenume)
    sume = [0] * len(nume)
    k = 0
    for prenume in nume:
        for rezervare in rezervari:
            name = get_nume(rezervare)
            if prenume == name:
                sume[k] += get_pret(rezervare)
        result.append(f'{nume[k]} are suma preturilor egala cu {sume[k]}')
        k += 1
    return result
