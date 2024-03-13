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
     else:
          print('You are lost')
     computerwins+=1
     
print("You won", userwins, "times.")
print("The computer won", computerwins, "times.")
print("Goodbye!")



