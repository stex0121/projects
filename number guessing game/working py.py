import random

top_of_range=input('Type a number : ')

if top_of_range.isdigit():
    top_of_range=int(top_of_range)

if top_of_range<=0:
    print('Please type a number, larger then 0 next time')
    quit()
else:
    print('Print number next time : ')
    
random_number=random.randint(0,top_of_range)
guesses=0
while True:
        guesses+=1
        user_guesses=input('Make a  guess : ')
        if user_guesses.isdigit():
            user_guesses=int(user_guesses)
        else:
            print('Please type a number next time : ')
        if user_guesses==random_number:
           print('You got it')
        elif user_guesses>random_number:
         
         print('You are above the number')
        
        else:
          print('You are below the number ')
          print('you got it', guesses,'guesses')  

