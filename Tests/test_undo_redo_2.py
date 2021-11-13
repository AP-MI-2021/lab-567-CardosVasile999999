from Logic.crud import create
from Logic.undo_redo import do_undo, do_redo


def test_undo_redo_2():
    rezervari = []  # Nr .1
    undo_list = []
    redo_list = []
    a1 = (1, 'Vasile', 'economy', 235, 'nu')
    rezervari = create(rezervari, *a1, undo_list, redo_list)  # Nr. 2
    o1 = {'id': 1, 'nume': 'Vasile', 'clasa': 'economy', 'pret': 235, 'checkin': 'nu'}
    a2 = (2, 'Ion', 'economy plus', 32432, 'da')
    rezervari = create(rezervari, *a2, undo_list, redo_list)  # Nr. 3
    o2 = {'id': 2, 'nume': 'Ion', 'clasa': 'economy plus', 'pret': 32432, 'checkin': 'da'}
    a3 = (3, 'Maria', 'business', 3453536.543, 'nu')
    rezervari = create(rezervari, *a3, undo_list, redo_list)  # Nr. 4
    rezervari = do_undo(undo_list, redo_list, rezervari)  # Nr. 5
    assert rezervari == [o1, o2]
    rezervari = do_undo(undo_list, redo_list, rezervari)  # Nr. 6
    assert rezervari == [o1]
    rezervari = do_undo(undo_list, redo_list, rezervari)  # Nr. 7
    assert rezervari == []
    try:
        rezervari = do_undo(undo_list, redo_list, rezervari)  # Nr. 8
    except IndexError:
        assert rezervari == []
    a1 = (1, 'Silvester', 'economy', 235, 'nu', undo_list, redo_list)
    rezervari = create(rezervari, *a1)  # Nr. 9
    o1 = {'id': 1, 'nume': 'Silvester', 'clasa': 'economy', 'pret': 235, 'checkin': 'nu'}
    a2 = (2, 'Iacob', 'economy plus', 25.65, 'da')
    rezervari = create(rezervari, *a2, undo_list, redo_list)  # Nr. 9
    o2 = {'id': 2, 'nume': 'Iacob', 'clasa': 'economy plus', 'pret': 25.65, 'checkin': 'da'}
    a3 = (3, 'Miranda', 'business', 567, 'nu')
    rezervari = create(rezervari, *a3, undo_list, redo_list)  # Nr. 9
    o3 = {'id': 3, 'nume': 'Miranda', 'clasa': 'business', 'pret': 567, 'checkin': 'nu'}
    redo_result = do_redo(undo_list, redo_list, rezervari)  # Nr. 10
    rezervari = redo_result
    assert rezervari == [o1, o2, o3]
    rezervari = do_undo(undo_list, redo_list, rezervari)  # Nr. 11
    rezervari = do_undo(undo_list, redo_list, rezervari)  # Nr. 11
    assert rezervari == [o1]
    rezervari = do_redo(undo_list, redo_list, rezervari)  # Nr. 12
    assert rezervari == [o1, o2]
    rezervari = do_redo(undo_list, redo_list, rezervari)  # Nr. 13
    assert rezervari == [o1, o2, o3]
    rezervari = do_undo(undo_list, redo_list, rezervari)  # Nr. 14
    rezervari = do_undo(undo_list, redo_list, rezervari)  # Nr. 14
    assert rezervari == [o1]
    a4 = (4, 'Claudiu', 'business', 43553, 'da')
    rezervari = create(rezervari, *a4, undo_list, redo_list)  # Nr. 15
    o4 = {'id': 4, 'nume': 'Claudiu', 'clasa': 'business', 'pret': 43553, 'checkin': 'da'}
    assert rezervari == [o1, o4]
    rezervari = do_redo(undo_list, redo_list, rezervari)  # Nr. 16
    assert rezervari == [o1, o4]
    rezervari = do_undo(undo_list, redo_list, rezervari)  # Nr. 17
    assert rezervari == [o1]
    rezervari = do_undo(undo_list, redo_list, rezervari)  # Nr. 18
    assert rezervari == []
    rezervari = do_redo(undo_list, redo_list, rezervari)  # Nr. 19
    rezervari = do_redo(undo_list, redo_list, rezervari)  # Nr. 19
    assert rezervari == [o1, o4]
    rezervari = do_redo(undo_list, redo_list, rezervari)  # Nr. 20
    assert rezervari == [o1, o4]
