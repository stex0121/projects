import random

VELIKA_ARKANA = 22
MALA_ARKANA = 56

UKUPAN_BROJ_KARATA = VELIKA_ARKANA + MALA_ARKANA

GLAVNA = ['Budala', 'Mag', 'Svestenik', 'Carica', 'Car', 'Hijerofant', 'Ljubavnici', 'Kocije', 'Snaga', 'Pustinjak',
          'Tocak srece', 'Pravda', 'Obesen', 'Smrt', 'Umerenost', 'Svet']

def number_convert(myint):
    if not myint in range(1, 11):
        raise ValueError('Error: Number out of range')
    numbers = ['AS', 'Dva', 'Tri', 'Cetri', 'Pet', 'Sest', 'Sedam', 'Osam', 'Devet', 'Deset']
    return numbers[myint - 1]

def get_element(suit):
    suit = suit.lower().strip()
    if suit == 'pehari':
        return 'Voda'
    elif suit == 'stapovi':
        return 'Vatra'
    elif suit == 'macevi':
        return 'Vazduh'
    elif suit == 'pentakli':
        return 'Zemlja'
    else:
        raise ValueError('Error: Suit not recognized')

def mala_arcana_suit(my_adjusted_card, suit):
    if my_adjusted_card in range(1, 11):
        if my_adjusted_card == 1:
            s = 'AS od {} | {}'.format(suit, get_element(suit))
        else:
            s = '{} od {} | {}'.format(number_convert(my_adjusted_card), suit, get_element(suit))
    else:
        if my_adjusted_card == 11:
            face = 'Paz'
            specific_element = 'Zemlje'
        elif my_adjusted_card == 12:
            face = 'Vitez'
            specific_element = 'Vazduha'
        elif my_adjusted_card == 13:
            face = 'Kraljica'
            specific_element = 'Vode'
        elif my_adjusted_card == 14:
            face = 'Kralj'
            specific_element = 'Vatre'
        s = '{} od {} | {} od {}'.format(face, suit, specific_element, get_element(suit))
    print(s)

def sort_minor_arcana(my_card):
    if my_card in range(22, 36):
        mala_arcana_suit(my_card - 21, 'Stapovi')
    elif my_card in range(36, 50):
        mala_arcana_suit(my_card - 35, 'Pehari')
    elif my_card in range(50, 64):
        mala_arcana_suit(my_card - 49, 'Macevi')
    elif my_card in range(64, 78):
        mala_arcana_suit(my_card - 63, 'Pentakli')
    else:
        raise ValueError('Error: Card number out of range')

def random_selected_cards():
    print('')
    my_card = random.randint(0, UKUPAN_BROJ_KARATA - 1)
    if my_card < 22:
        print("Glavna arkana: {}, {}".format(my_card, GLAVNA[my_card]))
    elif my_card < 78:
        sort_minor_arcana(my_card)
    else:
        raise ValueError('Error: Card number out of range')
    print('')

def main():
    random_selected_cards()

if __name__ == '__main__':
    main()