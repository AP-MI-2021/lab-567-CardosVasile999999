from Domain.rezervari import gestioneaza_rezervari, get_pret, get_id, get_nume, get_clasa, get_checkin
from Logic.ordonare_dupa_pret_descrescator import sort_reservations_by_price_decesting


def get_data():
    return [
        gestioneaza_rezervari(1, 'Vasile', 'economy', 8712, 'nu'),
        gestioneaza_rezervari(2, 'Lorenzo', 'economy plus', 2192, 'da'),
        gestioneaza_rezervari(3, 'Ion', 'business', 1762, 'da'),
        gestioneaza_rezervari(4, 'Anabella', 'economy plus', 8162, 'nu'),
        gestioneaza_rezervari(5, 'Sergiu', 'economy', 1982, 'da'),
        gestioneaza_rezervari(6, 'Luis', 'business', 1826, 'da'),
        gestioneaza_rezervari(7, 'Cristi', 'economy plus', 1245, 'nu'),
        gestioneaza_rezervari(8, 'Ioana', 'economy', 12143, 'da'),
        gestioneaza_rezervari(9, 'Alex', 'economy plus', 232, 'nu'),
        gestioneaza_rezervari(10, 'Mario', 'economy', 1225.45, 'da'),
        gestioneaza_rezervari(11, 'Luigi', 'economy plus', 12, 'da')
    ]


def test_sort_reservations_by_price_decesting():
    rezervari = get_data()
    rezervari = sort_reservations_by_price_decesting(rezervari)
    assert get_pret(rezervari[0]) == 12143
    assert get_id(rezervari[1]) == 1
    assert get_nume(rezervari[2]) == 'Anabella'
    assert get_clasa(rezervari[3]) == 'economy plus'
    assert get_checkin(rezervari[4]) == 'da'
    assert get_pret(rezervari[5]) == 1826
    assert get_pret(rezervari[6]) == 1762
    assert get_pret(rezervari[7]) == 1245
    assert get_pret(rezervari[8]) == 1225.45
    assert get_pret(rezervari[9]) == 232
    assert get_pret(rezervari[10]) == 12
