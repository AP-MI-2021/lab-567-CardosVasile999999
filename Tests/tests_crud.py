from Domain.rezervari import gestioneaza_rezervari
from Domain.rezervari import get_id
from Logic.crud import create, read, update, delete


def get_data():
    return [
            gestioneaza_rezervari(1, 'David', 'economy', 799, 'nu'),
            gestioneaza_rezervari(2, 'Leon', 'economy plus', 699, 'da'),
            gestioneaza_rezervari(3, 'Matei', 'business', 500, 'nu'),
            gestioneaza_rezervari(4, 'Cristi', 'economy', 200, 'da'),
            gestioneaza_rezervari(6, 'Lorenzo', 'business', 200, 'da')
        ]


def test_create():
        rezervari = get_data()
        params = (8, 'Sebi', 'economy', 450, 'da', [], [])
        r_new = gestioneaza_rezervari(*params[:-2])
        new_rezervare = create(rezervari, *params)
        assert r_new in new_rezervare
        params2 = (8, 'David', 'economy plus', 543, 'nu', [], [])
        try:
                _ = create(new_rezervare, *params2)
                assert False
        except ValueError:
                assert True


def test_read():
        rezervari = get_data()
        some_r = rezervari[2]
        assert read(rezervari, get_id(some_r)) == some_r
        assert read(rezervari, None) == rezervari


def test_update():
        rezervari = get_data()
        r_updated = gestioneaza_rezervari(1, 'Ionica', 'business', 35, 'nu')
        updated = update(rezervari, r_updated, [], [])
        assert r_updated in updated
        assert r_updated not in rezervari
        assert len(updated) == len(rezervari)


def test_delete():
        rezervari = get_data()
        to_delete = 4
        r_delted = read(rezervari, to_delete)
        deleted = delete(rezervari, to_delete, [], [])
        assert r_delted not in deleted
        assert r_delted in rezervari
        assert len(deleted) == len(rezervari) - 1


def test_crud():
        test_create()
        test_read()
        test_update()
        test_delete()
