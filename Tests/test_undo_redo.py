from Domain.rezervari import gestioneaza_rezervari
from Logic.crud import delete
from Logic.undo_redo import do_undo, do_redo


def get_date():
    return[
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


def test_undo_redo():
    rezervari = get_date()
    undo_list = []
    redo_list = []
    rezervari = delete(rezervari, 10, undo_list, redo_list)
    undo_result = do_undo(undo_list, redo_list, rezervari)
    assert undo_result == get_date()
    redo_result = do_redo(undo_list, redo_list, rezervari)
    assert redo_result == rezervari