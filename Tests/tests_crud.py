from Domain.rezervari import gestioneaza_rezervari


def get_data():
    return [gestioneaza_rezervari(1, 'Cat', 34, 354, 'DA'),
            gestioneaza_rezervari(1, 'Cat', 34, 354, 'DA'),
            gestioneaza_rezervari(1, 'Cat', 34, 354, 'DA'),
            gestioneaza_rezervari(1, 'Cat', 34, 354, 'DA'),
            gestioneaza_rezervari(1, 'Cat', 34, 354, 'DA')
            ]
