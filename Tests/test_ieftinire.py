from Domain.rezervari import gestioneaza_rezervari, get_pret, get_id
from Logic.ieftinire import ieftinire_rezervari_cu_check_in


def get_data():
    return [
            gestioneaza_rezervari(1, 'David', 'economy', 7456, 'nu'),
            gestioneaza_rezervari(2, 'Vasile', 'economy plus', 750, 'da'),
            gestioneaza_rezervari(3, 'Mihai', 'business', 50065.412, 'nu'),
            gestioneaza_rezervari(4, 'Sergiu', 'economy', 20030, 'da'),
            gestioneaza_rezervari(5, 'Vasile', 'economy plus', 423.1243, 'nu'),
            gestioneaza_rezervari(6, 'Ana', 'business', 200432.413, 'da')
        ]


def test_ieftinire_rezervari_cu_check_in():
    rezervari = get_data()
    rezervari = ieftinire_rezervari_cu_check_in(rezervari, 10)
    for rezervare in rezervari:
        if get_id(rezervare) == 1:
            assert get_pret(rezervare) == 7456
        elif get_id(rezervare) == 2:
            assert get_pret(rezervare) == 675
        elif get_id(rezervare) == 3:
            assert get_pret(rezervare) == 50065.412
        elif get_id(rezervare) == 4:
            assert get_pret(rezervare) == 18027
        elif get_id(rezervare) == 5:
            assert get_pret(rezervare) == 423.1243
        elif get_id(rezervare) == 6:
            assert get_pret(rezervare) == 180389.1717
