from Logic.crud import create
from Tests.test_ieftinire import test_ieftinire_rezervari_cu_check_in
from Tests.tests_crud import test_crud
from UserInterface.console import run_ui
from Tests.test_trecere_rezervari import test_trecere_rezervari_la_o_clasa_superioara


def main():
    rezervari = []
    rezervari = create(rezervari, 1, "Vasile", "economy", 123.213, "da")
    rezervari = create(rezervari, 2, "Alex", "economy plus", 1234.213, "da")
    rezervari = create(rezervari, 3, "Ioana", "business", 123.3, "nu")
    rezervari = create(rezervari, 4, "Lorenzo", "economy plus", 34.213, "nu")
    rezervari = create(rezervari, 5, "Mihai", "economy", 1234, "da")
    rezervari = create(rezervari, 6, "Mario", "economy plus", 24.13, "nu")
    rezervari = create(rezervari, 7, "Luigi", "business", 14.1, "da")
    run_ui(rezervari)


if __name__ == '__main__':
    test_crud()
    test_trecere_rezervari_la_o_clasa_superioara()
    test_ieftinire_rezervari_cu_check_in()
    main()
