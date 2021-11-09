from Domain.rezervari import gestioneaza_rezervari
from Logic.afisare_suma_pret_nume import show_sum_of_all_prices_by_name


def get_data():
    return[
        gestioneaza_rezervari(1, 'Vasile', 'economy', 8712, 'nu'),
        gestioneaza_rezervari(2, 'Alex', 'economy plus', 2192, 'da'),
        gestioneaza_rezervari(3, 'Ion', 'business', 1762, 'da'),
        gestioneaza_rezervari(4, 'Vasile', 'economy plus', 8162, 'nu'),
        gestioneaza_rezervari(5, 'Ion', 'economy', 1982, 'da'),
        gestioneaza_rezervari(6, 'Ioana', 'business', 1826, 'da'),
        gestioneaza_rezervari(7, 'Vasile', 'economy plus', 1245, 'nu'),
        gestioneaza_rezervari(8, 'Ioana', 'economy', 12143, 'da'),
        gestioneaza_rezervari(9, 'Alex', 'economy plus', 232, 'nu'),
        gestioneaza_rezervari(10, 'Ion', 'economy', 1225.45, 'da'),
        gestioneaza_rezervari(11, 'Alex', 'economy plus', 12, 'da')
    ]


def test_show_sum_of_all_prices_by_name():
    rezervari = get_data()
    preturi = show_sum_of_all_prices_by_name(rezervari)
    assert preturi[0] == 'Vasile are suma preturilor egala cu 18119'
    assert preturi[1] == 'Alex are suma preturilor egala cu 2436'
    assert preturi[2] == 'Ion are suma preturilor egala cu 4969.45'
    assert preturi[3] == 'Ioana are suma preturilor egala cu 13969'
