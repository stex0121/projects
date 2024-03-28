import random

userwins=0
computerwins=0

options=['rock','paper','scissors']

while True:
     userinput=input('Scissors,Rock,Paper or to Quit (Q)').lower()
     if userinput== 'q' :
          break
     if userinput not in options:
         continue
     randomnumber=random.randint(0,2)
     computerpick=options[randomnumber]
     print('computer picked',computerpick + '.')
     if userinput=='rock' and computerpick=='scissors':
          print('You have got on me,winner! ')
          userwins+=1
     elif userinput=='paper' and computerpick=='rock':
          print('You trick me well, you are the winner! ')
          userwins+=1
     elif userinput=='scissors' and computerpick=='paper':
          print('You are good,you have one')
          userwins+=1
     elif userinput=='scissors' and computerpick=='scissors':
          print('It is even')
          userwins+=0
     elif userinput=='paper' and computerpick=='paper':
          print('It is even')
          userwins+=0
     elif userinput=='rock' and computerpick=='rock':
          print('It is even ')
          userwins+=0
     else:
          print('You are lost')
     computerwins+=0
     
print("You won", userwins, "times.")
print("The computer won", computerwins, "times.")
print("Goodbye!")



