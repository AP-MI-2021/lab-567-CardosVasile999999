from Domain.rezervari import get_str, gestioneaza_rezervari
from Logic.afisare_suma_pret_nume import show_sum_of_all_prices_by_name
from Logic.crud import create, update, delete
from Logic.ieftinire import ieftinire_rezervari_cu_check_in
from Logic.ordonare_dupa_pret_descrescator import sort_reservations_by_price_decesting
from Logic.pret_maxim_clase import get_maximum_price_from_every_class
from Logic.trecere_rezervari import trecere_rezervari_la_o_clasa_superioara
from Logic.undo_redo import do_undo, do_redo


def show_menu():
    print('1. CRUD')
    print('2. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară')
    print('3. Ieftinirea rezervariilor cu check-in facut cu un procentaj citit')
    print('4. Determinarea pretului maxim pentru fiecare clasa')
    print('5. Ordonarea rezervarilor descrescator dupa pret')
    print('6. Afisarea sumelor preturilor pentru fiecare nume')
    print('u. Undo ultima comanda')
    print('r. Redo ultima comanda')
    print('x. Exit')


def handle_add(rezervari, undo_list, redo_list):
    aux = rezervari
    try:
        id_rezervare = int(input('Dati id-ul rezervarii: '))
        nume = input('Dati numele persoanei care a facut rezervarea: ')
        clasa = input('Dati clasa cu care zburati, poate fi doar: economy, economy plus, business: ')
        pret = float(input('Pretul zborului: '))
        checkin = input('checkin: da sau nu: ')
        rezervari = create(rezervari, id_rezervare, nume, clasa, pret, checkin, undo_list, redo_list)
        if aux != rezervari:
            print('Rezervarea a fost facuta cu succes!')
        return rezervari
    except ValueError as ve:
        print('Eroare:', ve)
    return rezervari


def handle_show_all(rezervari):
    if rezervari is not None:
        for rezervare in rezervari:
            print(get_str(rezervare))
    else:
        print('Nu exista rezervari in lista')


def handle_update(rezervari, undo_list, redo_list):
    try:
        id_rezervare = int(input('Dati id-ul rezervarii care se actualizeaza: '))
        nume = input('Dati numele noii persoanei care face rezervarea(daca e cazul): ')
        clasa = input('Dati noua clasa cu care zburati, poate fi doar: economy, economy plus, business: ')
        pret = float(input('Pretul noului zborului: '))
        checkin = input('checkin: da sau nu: ')
        return update(rezervari, gestioneaza_rezervari(id_rezervare, nume, clasa, pret, checkin), undo_list, redo_list)
    except ValueError as ve:
        print('Eroare', ve)


def handle_delete(rezervari, undo_list, redo_list):
    aux = rezervari
    try:
        id_rezervare = int(input('Dati id-ul rezervarii care se va sterge: '))
        rezervari = delete(rezervari, id_rezervare, undo_list, redo_list)
        if aux != rezervari:
            print('Stergerea a avut loc cu succes!')
        return rezervari
    except ValueError as ve:
        print('Eroare:', ve)


def handle_crud(rezervari, undo_list, redo_list):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('b. revenire')
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            rezervari = handle_add(rezervari, undo_list, redo_list)
        elif optiune == '2':
            rezervari = handle_update(rezervari, undo_list, redo_list)
        elif optiune == '3':
            rezervari = handle_delete(rezervari, undo_list, redo_list)
        elif optiune == 'a':
            handle_show_all(rezervari)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida')

    return rezervari


def handle_trecere_rezervari(rezervari, undo_list, redo_list):
    nume = input('Dati numele la care e facuta rezervarea pe care o doriti sa o treceti la o clasa superioara: ')
    aux = rezervari
    rezervari = trecere_rezervari_la_o_clasa_superioara(rezervari, nume, undo_list, redo_list)
    if rezervari == aux:
        print(f'Nu exista rezervari pe numele {nume}')
        return rezervari
    else:
        print('Rezervariile au fost actualizate cu succes !')
        return rezervari


def handle_ieftinire_rezervari(rezervari, undo_list, redo_list):
    procent = float(input('Dati procentul cu care vreti sa se reduca rezervarile (intre 0 si 100): '))
    aux = rezervari
    rezervari = ieftinire_rezervari_cu_check_in(rezervari, procent, undo_list, redo_list)
    if procent < 0 or procent > 100:
        return rezervari
    if rezervari == aux:
        print('Nu exista rezervare cu check-in in lista.')
        return rezervari
    else:
        print('Rezervarile au fost reduse cu succes !')
        return rezervari


def handle_maximum_price_by_class(rezervari):
    clasa = ['economy', 'economy plus', 'business']
    maxim = get_maximum_price_from_every_class(rezervari)
    for i in range(0, 3):
        if maxim[i] != -1:
            print(f'{clasa[i]} are ca pret maxim: {maxim[i]}')
        else:
            print(f'Nu exista nici o rezervare cu clasa {clasa[i]}')


def handle_ordonare_rezervari(rezervari, undo_list, redo_list):
    rezervari = sort_reservations_by_price_decesting(rezervari, undo_list, redo_list)
    print('Ordonarea a avut loc cu succes !')
    return rezervari


def handle_afisare_suma_pret_nume(rezervari):
    preturi = show_sum_of_all_prices_by_name(rezervari)
    for pret in preturi:
        print(pret)


def handle_undo(rezervari, undo_list, redo_list):
    try:
        undo_result = do_undo(undo_list, redo_list, rezervari)
        if undo_result is not None:
            return undo_result
        return rezervari
    except IndexError:
        print("Eroare: Nu exista elemente pentru undo")


def handle_redo(rezervari, undo_list, redo_list):
    redo_result = do_redo(undo_list, redo_list, rezervari)
    if redo_result is not None:
        return redo_result
    return rezervari


def run_ui(rezervari, undo_list, redo_list):

    while True:
        handle_show_all(rezervari)
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            rezervari = handle_crud(rezervari, undo_list, redo_list)
        elif optiune == '2':
            rezervari = handle_trecere_rezervari(rezervari, undo_list, redo_list)
        elif optiune == '3':
            rezervari = handle_ieftinire_rezervari(rezervari, undo_list, redo_list)
        elif optiune == '4':
            handle_maximum_price_by_class(rezervari)
        elif optiune == '5':
            rezervari = handle_ordonare_rezervari(rezervari, undo_list, redo_list)
        elif optiune == '6':
            handle_afisare_suma_pret_nume(rezervari)
        elif optiune == 'u':
            rezervari = handle_undo(rezervari, undo_list, redo_list)
        elif optiune == 'r':
            rezervari = handle_redo(rezervari, undo_list, redo_list)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')
