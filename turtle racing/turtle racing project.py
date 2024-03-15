import turtle
import time
import random
#constants cannot be changed.
WIDTH= 700
HEIGHT=600

COLORS=['red','blue','purple','green','yellow','black','orange','purple','pink','cyan']

def get_number_of_racers():
    #Inside of here,we are asking a user how much racers do we want to race.
    #We are using a while loop to ask a user for valid number of racers 
    #if user input invalid number,loop asks him again for valid digits.
    racers=0
    # I putted racers=0 beacuse i dont know how much turtles we will have in a race and 
    #in next statement we are using while loop.
    #To know how much turtles we will have in race.
    while True:
        racers=input('Get number of racers 2 to 10 : ') #This is the input of number of racers we want to race.
        if racers.isdigit(): # We are using isdigit method to return digits//int type or...
            racers=int(racers)
        else:
            print('Input is not Numerical,please try again:')#... or false Exponents
            continue #Then we are using continue statement that we  used to skip the remaining code inside a loop. 
        if 2<=racers<=10: #we are using continue for the next if statement that will be happen,and iin this statement racers are number.
            return racers #return statement ends the execution of a function, and returns control to the calling function
        else:
            print('Number is not between 2 and 10,please enter number between 2 to 10 :') 
            #If the numbers are not between 2 and 10 we have else statement,who prints to enter numbers and we have loop.


def race(colors):
    turtles=create_turtle(colors) #This function creates a turtles
    while True: #We are using while loop for turtles to go on top on screen.
        for racer in turtles:
            distance=random.randrange(1 , 20) #Everytime we want to turtle move on screen between 1 to 20 pixels
            racer.forward(distance) #Moving forwad of distance that we selected from function create_turtle

        x,y=racer.pos() #This state is giving us a racer position
        if y >= HEIGHT // 2-10: # if the turtle passes a finish line we have a winer
             return colors[turtles.index(racer)] # adn this statement returns a winner.

def create_turtle(colors):
    turtles=[]
    spacingx=WIDTH//(len(colors)+1) #In this statement we are dividing width with by the len of colors  + colors of turtles which repsresents 1
    for i,color in enumerate (colors): #enamurate statement give as index and value  looping throw color list and turtle list ['red','blue','green']=[0,1,2]
        racer=turtle.Turtle() #This variable is moving turtles on canvas
        racer.color(color) #This is the color of turtles who races
        racer.shape('turtle') #This is the shape of  turtles of Turtle module
        racer.left(90) # This is a movement throw canvas of turtle,we have optons forward,backward,left,right and in bracket () we have a degrees of movement.
        racer.penup() #It will ensure the turtle draws when it's moving with your commands
        racer.setpos(-WIDTH//2+(i+1)*spacingx,-HEIGHT//2+20) #In this statement we are setting a posstion of racers.
        racer.pendown() #It will ensure the turtle draws when it's moving with your commands
        turtles.append(racer) #The append() method appends an element to the end of the list
    return turtles #The Python return statement is 
#   a special statement that you can use inside a function or method to send 
#the function's result back to the caller

def init_turtle():
    screen=turtle.Screen()#In this function we are deffining a screen canvas of turtle racing
    screen.setup(WIDTH,HEIGHT) # We are using a constants beacuse is easier to acces to them then a height or width
    screen.title('turtle racing')#This is the title of project in python.
   
racers = get_number_of_racers()
init_turtle()
 #The init method in Python is a fundamental component of object-oriented programming,
# serving as the constructor that initializes object attributes upon instantiation

random.shuffle(COLORS) # We are using random module which Returns a random element from the given sequence 
#Shuffle means a shuffling a list of objects which means changing the position of the elements of the sequence using Python.
colors = COLORS[:racers]#This statement will always select unique colors of turtles

winner = race(colors)
print("The winner is the turtle with color:", winner)
time.sleep(5)#Python time sleep function is used to add delay in the execution of a program. 




