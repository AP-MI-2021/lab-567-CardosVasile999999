from Domain.rezervari import get_str, gestioneaza_rezervari
from Logic.crud import create, update, delete
from Logic.trecere_rezervari import trecere_rezervari_la_o_clasa_superioara


def show_menu():
    print('1. CRUD')
    print('2. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară')
    print('x. Exit')


def handle_add(rezervari):
    try:
        id_rezervare = int(input('Dati id-ul rezervarii: '))
        nume = input('Dati numele persoanei care a facut rezervarea: ')
        clasa = input('Dati clasa cu care zburati, poate fi doar: economy, economy plus, business: ')
        pret = float(input('Pretul zborului: '))
        checkin = input('checkin: da sau nu: ')
        return create(rezervari, id_rezervare, nume, clasa, pret, checkin)
    except ValueError as ve:
        print('Eroare:', ve)

    return rezervari


def handle_show_all(rezervari):
    for rezervare in rezervari:
        print(get_str(rezervare))


def handle_update(rezervari):
    id_rezervare = int(input('Dati id-ul rezervarii care se actualizeaza: '))
    nume = input('Dati numele noii persoanei care face rezervarea(daca e cazul): ')
    clasa = input('Dati noua clasa cu care zburati, poate fi doar: economy, economy plus, business: ')
    pret = float(input('Pretul noului zborului: '))
    checkin = input('checkin: da sau nu: ')
    return update(rezervari, gestioneaza_rezervari(id_rezervare, nume, clasa, pret, checkin))


def handle_delete(rezervari):
    id_rezervare = int(input('Dati id-ul rezervarii care se va sterge: '))
    print('Stergerea a avut loc cu succes!')
    return delete(rezervari, id_rezervare)


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
    rezervari = trecere_rezervari_la_o_clasa_superioara(rezervari, nume)
    print('Rezervariile au fost actualizate cu succes !')
    return rezervari


def run_ui(rezervari):

    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            rezervari = handle_crud(rezervari)
        elif optiune == '2':
            rezervari = handle_trecere_rezervari(rezervari)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')

    return rezervari
