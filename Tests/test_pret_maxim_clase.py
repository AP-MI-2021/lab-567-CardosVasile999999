from Domain.rezervari import gestioneaza_rezervari
from Logic.pret_maxim_clase import get_maximum_price_from_every_class


def get_data1():
    return [
        gestioneaza_rezervari(1, 'Vlad', 'economy plus', 750, 'nu'),
        gestioneaza_rezervari(2, 'Vasile', 'economy', 234.32, 'da'),
        gestioneaza_rezervari(3, 'Cristi', 'economy plus', 50, 'nu'),
        gestioneaza_rezervari(4, 'Mario', 'business', 75, 'da'),
        gestioneaza_rezervari(5, 'Iulian', 'economy plus', 23750, 'nu'),
        gestioneaza_rezervari(6, 'Ioana', 'economy', 234.234, 'da'),
        gestioneaza_rezervari(7, 'Ana', 'business', 1, 'nu'),
        gestioneaza_rezervari(8, 'Steve', 'economy', 2434.243, 'da'),
        gestioneaza_rezervari(9, 'Luigi', 'business', 9804.2, 'nu'),
        gestioneaza_rezervari(10, 'Ronaldo', 'economy', 156, 'da'),
        gestioneaza_rezervari(11, 'Larry', 'economy plus', 342, 'nu'),
        gestioneaza_rezervari(12, 'Iggy', 'business', 50.423, 'da'),
    ]


def test_get_maximum_price_from_every_class():
    rezervari = get_data1()
    maxim = get_maximum_price_from_every_class(rezervari)
    assert maxim[0] == 2434.243
    assert maxim[1] == 23750
    assert maxim[2] == 9804.2
