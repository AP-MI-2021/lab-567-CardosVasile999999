from Domain.rezervari import gestioneaza_rezervari
from Domain.rezervari import get_id
from Logic.crud import create
from Logic.crud import read
from Logic.crud import update
from Logic.crud import delete


def get_data():
    return [
            gestioneaza_rezervari(1, 'David', 1, 799, 'NU'),
            gestioneaza_rezervari(2, 'Leon', 2, 699, 'DA'),
            gestioneaza_rezervari(3, 'Matei', 3, 500, 'NU'),
            gestioneaza_rezervari(4, 'Cristi', 4, 200, 'DA'),
            gestioneaza_rezervari(6, 'Lorenzo', 4, 200, 'DA')
        ]


def test_create():
        rezervari = get_data()
        params = (8, 'Sebi', 3, 450, 'DA')
        r_new = gestioneaza_rezervari(*params)
        new_rezervare = create(rezervari, *params)
        assert r_new in new_rezervare


def test_read():
        rezervari = get_data()
        some_r = rezervari[2]
        assert read(rezervari, get_id(some_r)) == some_r
        assert read(rezervari, None) == rezervari


def test_update():
        rezervari = get_data()
        r_updated = gestioneaza_rezervari(1, 'Ionica', 2, 35, 'NU')
        updated = update(rezervari, r_updated)
        assert r_updated in updated
        assert r_updated not in rezervari
        assert len(updated) == len(rezervari)


def test_delete():
        rezervari = get_data()
        to_delete = 4
        r_delted = read(rezervari, to_delete)
        deleted = delete(rezervari, to_delete)
        assert r_delted not in deleted
        assert r_delted in rezervari
        assert len(deleted) == len(rezervari) - 1


def test_crud():
        test_create()
        test_read()
        test_update()
        test_delete()
