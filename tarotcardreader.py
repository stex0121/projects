
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
        s='AS'
    elif myint==2:
     s='Dva'
    elif myint==3:
       s='Tri'
    elif myint==4:
       s='Cetri'
    elif myint==5:
       s='Pet'
    elif myint==6:
       s='Sest'
    elif myint==7:
       s='Sedam'
    elif myint==8:
       s='Osam'
    elif myint==9:
       s='Devet'
    elif myint==10:
       s='Deset'
    return s

def get_element(suit):
   suit=suit.lower().strip()
   if suit== 'Pehari': return 'Voda'
   elif suit=='Stapovi': return 'Vatra'
   elif suit=='Macevi': return "Vazduh"
   elif suit=='Pentakli': return 'Zemlja'
   else:
      s='Ne prepoznajem ovo : {}'.format(suit)
      raise ValueError(s)
   
def mala_arcana_suit(my_adjusted_card,suit):
   if my_adjusted_card in list(range(1,11)):
      if my_adjusted_card==1:
         s='AS od {} | {}'.format(suit,get_element(suit))
         print(s)
      else:
         s='{} od {} | {}'.format(number_convert(my_adjusted_card),suit,get_element(suit))
         print(s)
   else:
      face=''
      specific_element=''
      if my_adjusted_card==11:
         face='Paz'
         specific_element='Zemlja'
      elif my_adjusted_card==12:
         face='Vitez'
         specific_element='Vazduh'
      elif my_adjusted_card==13:
         face='Kraljica'
         specific_element='Voda'
      elif my_adjusted_card==14:
         face='Kralj'
         specific_element='Fire'
         s='{} od {} | {} od {}'.format(face,suit,specific_element,get_element(suit))
         print(s)

def sort_minor_arcana(my_card):
    
    if my_card in list(range(22,36)):
      mala_arcana_suit(my_card-21,'STapovi')
    elif my_card in list(range(36,50)):
      mala_arcana_suit(my_card-35,'Pehari')
    elif my_card in list(range(50,64)):
      mala_arcana_suit(my_card-49,'Macevi')
    elif my_card in list(range(64,78)):
      mala_arcana_suit(my_card-63,'Pentakli')
    else:
     raise ValueError('error')
def random_selected_cards():
   print('')
   my_card=random.randint(0,UKUPAN_BROJ_KARATA-1)
   if my_card in list(range(22)):
      print("Glavna arkana: {}, {}".format(my_card,GLAVNA[my_card]))
   elif my_card in list(range(22,78)):
      print("Mala Arkana: {}".format(my_card))
   else:
      raise ValueError('eror')
   print('')
def main():
   random_selected_cards()
if __name__=='__main__':
   main()
      

   
