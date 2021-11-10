from Domain.rezervari import gestioneaza_rezervari, get_nume, get_clasa, get_id
from Logic.trecere_rezervari import trecere_rezervari_la_o_clasa_superioara


def get_data():
    return [
            gestioneaza_rezervari(1, 'Vasile', 'economy', 799, 'nu'),
            gestioneaza_rezervari(2, 'David', 'economy plus', 699, 'da'),
            gestioneaza_rezervari(3, 'Mihai', 'business', 500, 'nu'),
            gestioneaza_rezervari(4, 'Sergiu', 'economy', 200, 'da'),
            gestioneaza_rezervari(5, 'Vasile', 'economy plus', 423, 'da'),
            gestioneaza_rezervari(6, 'Ana', 'business', 200, 'da')
        ]


def test_trecere_rezervari_la_o_clasa_superioara():
    rezervari = get_data()
    rezervari = trecere_rezervari_la_o_clasa_superioara(rezervari, 'Vasile', [], [])
    for rezervare in rezervari:
        if get_nume(rezervare) == 'Vasile' and get_id(rezervare) == 1:
            assert get_clasa(rezervare) == 'economy plus'
        elif get_nume(rezervare) == 'David':
            assert get_clasa(rezervare) == 'economy plus'
        elif get_nume(rezervare) == 'Mihai':
            assert get_clasa(rezervare) == 'business'
        elif get_nume(rezervare) == 'Sergiu':
            assert get_clasa(rezervare) == 'economy'
        elif get_nume(rezervare) == 'Ana':
            assert get_clasa(rezervare) == 'business'
        elif get_nume(rezervare) == 'Vasile' and get_id(rezervare) == 5:
            assert get_clasa(rezervare) == 'business'
