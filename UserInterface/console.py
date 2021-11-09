from Domain.rezervari import get_str, gestioneaza_rezervari
from Logic.afisare_suma_pret_nume import show_sum_of_all_prices_by_name
from Logic.crud import create, update, delete
from Logic.ieftinire import ieftinire_rezervari_cu_check_in
from Logic.ordonare_dupa_pret_descrescator import sort_reservations_by_price_decesting
from Logic.pret_maxim_clase import get_maximum_price_from_every_class
from Logic.trecere_rezervari import trecere_rezervari_la_o_clasa_superioara


def show_menu():
    print('1. CRUD')
    print('2. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară')
    print('3. Ieftinirea rezervariilor cu check-in facut cu un procentaj citit')
    print('4. Determinarea pretului maxim pentru fiecare clasa')
    print('5. Ordonarea rezervarilor descrescator dupa pret')
    print('6. Afisarea sumelor preturilor pentru fiecare nume')
    print('x. Exit')


def handle_add(rezervari):
    aux = rezervari
    try:
        id_rezervare = int(input('Dati id-ul rezervarii: '))
        nume = input('Dati numele persoanei care a facut rezervarea: ')
        clasa = input('Dati clasa cu care zburati, poate fi doar: economy, economy plus, business: ')
        pret = float(input('Pretul zborului: '))
        checkin = input('checkin: da sau nu: ')
        rezervari = create(rezervari, id_rezervare, nume, clasa, pret, checkin)
        if aux != rezervari:
            print('Rezervarea a fost facuta cu succes!')
        return rezervari
    except ValueError as ve:
        print('Eroare:', ve)
    return rezervari


def handle_show_all(rezervari):
    for rezervare in rezervari:
        print(get_str(rezervare))


def handle_update(rezervari):
    try:
        id_rezervare = int(input('Dati id-ul rezervarii care se actualizeaza: '))
        nume = input('Dati numele noii persoanei care face rezervarea(daca e cazul): ')
        clasa = input('Dati noua clasa cu care zburati, poate fi doar: economy, economy plus, business: ')
        pret = float(input('Pretul noului zborului: '))
        checkin = input('checkin: da sau nu: ')
        return update(rezervari, gestioneaza_rezervari(id_rezervare, nume, clasa, pret, checkin))
    except ValueError as ve:
        print('Eroare', ve)


def handle_delete(rezervari):
    aux = rezervari
    try:
        id_rezervare = int(input('Dati id-ul rezervarii care se va sterge: '))
        rezervari = delete(rezervari, id_rezervare)
        if aux != rezervari:
            print('Stergerea a avut loc cu succes!')
        return rezervari
    except ValueError as ve:
        print('Eroare:', ve)


def handle_crud(rezervari):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('b. revenire')
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            rezervari = handle_add(rezervari)
        elif optiune == '2':
            rezervari = handle_update(rezervari)
        elif optiune == '3':
            rezervari = handle_delete(rezervari)
        elif optiune == 'a':
            handle_show_all(rezervari)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida')

    return rezervari


def handle_trecere_rezervari(rezervari):
    nume = input('Dati numele la care e facuta rezervarea pe care o doriti sa o treceti la o clasa superioara: ')
    aux = rezervari
    rezervari = trecere_rezervari_la_o_clasa_superioara(rezervari, nume)
    if rezervari == aux:
        print(f'Nu exista rezervari pe numele {nume}')
        return rezervari
    else:
        print('Rezervariile au fost actualizate cu succes !')
        return rezervari


def handle_ieftinire_rezervari(rezervari):
    procent = float(input('Dati procentul cu care vreti sa se reduca rezervarile (intre 0 si 100): '))
    aux = rezervari
    rezervari = ieftinire_rezervari_cu_check_in(rezervari, procent)
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


def handle_ordonare_rezervari(rezervari):
    rezervari = sort_reservations_by_price_decesting(rezervari)
    print('Ordonarea a avut loc cu succes !')
    return rezervari


def handle_afisare_suma_pret_nume(rezervari):
    preturi = show_sum_of_all_prices_by_name(rezervari)
    for pret in preturi:
        print(pret)


def run_ui(rezervari):

    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            rezervari = handle_crud(rezervari)
        elif optiune == '2':
            rezervari = handle_trecere_rezervari(rezervari)
        elif optiune == '3':
            rezervari = handle_ieftinire_rezervari(rezervari)
        elif optiune == '4':
            handle_maximum_price_by_class(rezervari)
        elif optiune == '5':
            rezervari = handle_ordonare_rezervari(rezervari)
        elif optiune == '6':
            handle_afisare_suma_pret_nume(rezervari)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')
