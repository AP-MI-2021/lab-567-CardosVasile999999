from Domain.rezervari import get_pret


def sort_reservations_by_price_decesting(rezervari):
    """
    Ordonam descrescator in functie de pret rezervarile
    :param rezervari: lista de rezervari
    :return: lista de rezervari ordonate descrescator dupa pret
    """
    n = len(rezervari)
    preturi = []
    result = []
    for rezervare in rezervari:
        preturi.append(get_pret(rezervare))
    for i in range(0, n-1):
        for j in range(i+1, n):
            if preturi[i] < preturi[j]:
                aux = preturi[i]
                preturi[i] = preturi[j]
                preturi[j] = aux
    for pret in preturi:
        for rezervare in rezervari:
            if pret == get_pret(rezervare):
                result.append(rezervare)

    return result
