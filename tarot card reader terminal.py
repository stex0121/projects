
import random

VELIKA_ARKANA=22
MALA_ARKANA=56

UKUPAN_BROJ_KARATA=VELIKA_ARKANA+MALA_ARKANA

GLAVNA=['Budala','Mag','Svestenik','Carica','Car']
GLAVNA+=['Hijerofant','Ljubavnici','Kocije','Snaga','Pustinjak']
GLAVNA+=['Tocak srece','Pravda','Obesen','Smrt','Umerenost']
GLAVNA+=['Svet']

def number_convert(myint):
    if not myint in range(1,11):
        raise ValueError('error')
    s=''
    if myint==1:
        s='As'
    elif myint==2:
     s='Dvojka'
    elif myint==3:
       s='Trojka'
    elif myint==4:
       s='Cetvorka'
    elif myint==5:
       s='petica'
    elif myint==6:
       s='Sestica'
    elif myint==7:
       s='Sedmica'
    elif myint==8:
       s='Osmica'
    elif myint==9:
       s='Devetka'
    elif myint==10:
       s='Desetka'
    return s

def get_element(suit):
    suit=suit.lower().strip()
    if suit == 'pehar': return 'voda'
    elif suit == 'stap': return 'vatra'
    elif suit == 'mac': return "vazduh"
    elif suit == 'pentakl': return 'zemlja'
    else:
       s='Ne prepoznajem ovo : {}'.format(suit)
       raise ValueError(s)
      
   
def mala_arcana_suit(my_adjusted_card,suit):
   if my_adjusted_card in list(range(1,11)):
      if my_adjusted_card==1:
         s='AS od {} | {}'.format(suit, get_element(suit))
         print(s)
      else:
         s='{} od {} | {}'.format( number_convert(my_adjusted_card) , suit , get_element(suit))
         print(s)
   else:
      face=''
      specific_element=''
      if my_adjusted_card==11:
         face='paz'
         specific_element='zemlje'
      elif my_adjusted_card==12:
         face='vitez'
         specific_element='vazduha'
      elif my_adjusted_card==13:
         face='kraljica'
         specific_element='vode'
      elif my_adjusted_card==14:
         face='kralj'
         specific_element='vatre'
         s='{} od {} | {} od {}'.format(face,suit,specific_element,get_element(suit))
         print(s)

def sort_mala_arcana(my_card):
    
    if my_card in list(range(22,36)):
      mala_arcana_suit(my_card-21,'stap')
    elif my_card in list(range(36,50)):
      mala_arcana_suit(my_card-35,'pehar')
    elif my_card in list(range(50,64)):
      mala_arcana_suit(my_card-49,'mac')
    elif my_card in list(range(64,78)):
      mala_arcana_suit(my_card-63,'pentakl')
    else:
     raise ValueError('error')
def random_selected_cards():
   print('')
   my_card=random.randint(0,UKUPAN_BROJ_KARATA-1)
   if my_card in list(range(22)):
      print("Glavna arkana: {} , {} ".format(my_card ,GLAVNA[my_card]))
      print(GLAVNA[my_card])
   elif my_card in list(range(22,78)):
      print("Mala Arkana: {}  ".format(my_card))
      sort_mala_arcana(my_card)
      print(my_card)
      
   else:
      raise ValueError('eror')
   print('')
def main():
   random_selected_cards()

if __name__=='__main__':
   main()
      

   
