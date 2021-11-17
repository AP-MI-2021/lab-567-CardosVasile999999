from Logic.crud import create
from Tests.test_afisare_suma_pret_descrescator import test_show_sum_of_all_prices_by_name
from Tests.test_ieftinire import test_ieftinire_rezervari_cu_check_in
from Tests.test_ordonare_dupa_pret_descrescator import test_sort_reservations_by_price_decesting
from Tests.test_pret_maxim_clase import test_get_maximum_price_from_every_class
from Tests.test_undo_redo import test_undo_redo
from Tests.test_undo_redo_2 import test_undo_redo_2
from Tests.tests_crud import test_crud
from UserInterface.command_line_console import run_ui2
from UserInterface.console import run_ui
from Tests.test_trecere_rezervari import test_trecere_rezervari_la_o_clasa_superioara


def main():
    rezervari = []
    undo_list = []
    redo_list = []
    rezervari = create(rezervari, 1, "Vasile", "economy", 123.213, "da", undo_list, redo_list)
    rezervari = create(rezervari, 2, "Alex", "economy plus", 1234.213, "nu", undo_list, redo_list)
    rezervari = create(rezervari, 3, "Ioana", "business", 123.3, "da", undo_list, redo_list)
    #  rezervari = create(rezervari, 4, "Lorenzo", "economy plus", 34.213, "nu", undo_list, redo_list)
    #  rezervari = create(rezervari, 5, "Mihai", "economy", 1234, "da", undo_list, redo_list)
    #  rezervari = create(rezervari, 6, "Mario", "economy plus", 24.13, "da", undo_list, redo_list)
    #  rezervari = create(rezervari, 7, "Luigi", "business", 14.1, "nu", undo_list, redo_list)
    while True:
        alege = input('Alege ui1 sau ui2 (cea de acum doua saptamani) sau x pentru oprire: ')
        if alege == 'ui1':
            run_ui(rezervari, undo_list, redo_list)
        elif alege == 'ui2':
            run_ui2(rezervari)
        elif alege == 'x':
            break
        else:
            print('Optiune invalida')


if __name__ == '__main__':
    test_crud()
    test_trecere_rezervari_la_o_clasa_superioara()
    test_ieftinire_rezervari_cu_check_in()
    test_get_maximum_price_from_every_class()
    test_sort_reservations_by_price_decesting()
    test_show_sum_of_all_prices_by_name()
    test_undo_redo()
    test_undo_redo_2()
    main()
