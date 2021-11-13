from Domain.rezervari import get_str, gestioneaza_rezervari
from Logic.crud import create, update, delete
from Logic.ieftinire import ieftinire_rezervari_cu_check_in
from Logic.trecere_rezervari import trecere_rezervari_la_o_clasa_superioara


def show_menu():
    print('Scrieti caracterul fiecarei comenzi pe care vreti sa o faceti')
    print('CRUD. Comenzi de CRUD:')
    print('  a. Adaugare: Dati in aceasta ordine: id_ul rezervarii, numele, clasa, pretul si checkin')
    print('  m. Modificare: Dati in aceasta ordine: id_ul rezervarii care se modifica, '
          'noul nume, noua clasa, noul pret, noul checkin')
    print('  d. Stergere: Dati id_ul rezervarii pe care vreti sa-l stergeti')
    print('  s. Afisare')
    print('trecere. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară: Dati numele')
    print('ieftinire. Ieftinirea rezervariilor cu check-in facut cu un procentaj citit: Dati procentul')
    print('x. Exit')


def run_ui2(rezervari):
    hmm = 'continua'
    lst = ['CRUD', 'trecere', 'ieftinire']
    lst2 = ['a', 'm', 'd', 's']
    while True and hmm == 'continua':
        show_menu()
        optiune = input('Scrieti ce vreti sa faceti, fiecare comanda fiind separata doar printr-un spatiu: ')
        reserve = optiune.split(' ')
        n = len(reserve)
        i = 0
        while i <= n-1:
            if reserve[i] == 'CRUD':
                i = i + 1
                try:
                    if reserve[i] == 'a':
                        try:
                            try:
                                id_ul = int(reserve[i + 1])
                                nume = reserve[i + 2]
                                clasa = reserve[i + 3]
                                pret = float(reserve[i + 4])
                                checkin = reserve[i + 5]
                                rezervari = create(rezervari, id_ul, nume, clasa, pret, checkin, [], [])
                                i = i + 5
                            except IndexError:
                                print(f'Nu exista destule elemente pentru adaugare')
                        except ValueError as ve:
                            print('Eroare:', ve)
                            i = i + 5
                    elif reserve[i] == 'm':
                        try:
                            try:
                                id_ul = int(reserve[i + 1])
                                nume = reserve[i + 2]
                                clasa = reserve[i + 3]
                                pret = float(reserve[i + 4])
                                checkin = reserve[i + 5]
                                rezervari = update(rezervari, gestioneaza_rezervari(id_ul, nume, clasa, pret, checkin),
                                                   [], [])
                                i = i + 5
                            except IndexError:
                                print(f'Nu exista destule elemente pentru modificare')
                        except ValueError as ve:
                            print('Eroare:', ve)
                            i = i + 5
                    elif reserve[i] == 'd':
                        try:
                            try:
                                id_ul = int(reserve[i + 1])
                                rezervari = delete(rezervari, id_ul, [], [])
                                i = i + 1
                            except IndexError:
                                print(f'Nu ati introdus un id pentru stergere')
                        except ValueError as ve:
                            print('Eroare', ve)
                            i = i + 1
                    elif reserve[i] == 's':
                        for rezervarea in rezervari:
                            print(get_str(rezervarea))
                except IndexError:
                    print('Nu ati adaugat a comanda dupa CRUD')
            elif reserve[i] == 'trecere':
                try:
                    try:
                        nume = reserve[i + 1]
                        aux = rezervari
                        rezervari = trecere_rezervari_la_o_clasa_superioara(rezervari, nume, [], [])
                        i = i + 1
                        if aux == rezervari:
                            print(f'Nu exista rezervari pe numele {nume}')
                    except IndexError:
                        print('Nu ati introdus nici un nume.')
                except ValueError as ve:
                    print('Eroare:', ve)
                    i = i + 1
            elif reserve[i] == 'ieftinire':
                try:
                    try:
                        procent = float(reserve[i + 1])
                        rezervari = ieftinire_rezervari_cu_check_in(rezervari, procent, [], [])
                        i = i + 1
                    except IndexError:
                        print('Nu ati introdus un procent')
                except ValueError as ve:
                    print(f'Eroare:', ve)
                    i = i + 1
            elif reserve[i] == 'x':
                hmm = 'inchide'
                break
            elif reserve[i] not in lst and reserve[i] not in lst2:
                print(f'{reserve[i]} nu este o comanda valida')
            elif reserve[i] in lst2:
                print(f'{reserve[i]} nu este o comanda valida daca nu scrii "CRUD" mai intai')
            i = i + 1
