
import random

symbols=['Cherry','Orange','Apple','Bars','Diamond','Seven','Watermellon','Bell']
player_score=100

def spin_slot_machine():
    global player_score
    bet_amount=int(input('Enter your amount for bet: '))
    
    if bet_amount > player_score:
        print('Not enough money, please enter a valid bet amount.')
        return
    
    reel1=random.choice(symbols)
    reel2=random.choice(symbols)
    reel3=random.choice(symbols)
    reel4=random.choice(symbols)
    reel5=random.choice(symbols)
    reel6=random.choice(symbols)
    reel7=random.choice(symbols)
    reel8=random.choice(symbols)
    reel9=random.choice(symbols)
    
    
    print(f'{reel1} | {reel2} | {reel3}\n-------------------------------------\n{reel4} | {reel5} | {reel6}\n-----------------------------------\n{reel7} | {reel8} | {reel9}')
    
    if reel1==reel2==reel3 :
     winnings=bet_amount*2
     print(f'Congratulations! You win the Jackpot. Your winnings: {winnings}')
     player_score+=winnings
    elif reel1==reel5==reel9 :
        winnings=bet_amount*5
        print(f'Congratulations! You win the Jackpot. Your winnings: {winnings}')
        player_score+=winnings

    elif reel3==reel5==reel7:
        winnings=bet_amount*5
        print(f'Congratulations! You win the Jackpot. Your winnings: {winnings}')
        player_score+=winnings 
    elif reel4==reel5==reel6:
        winnings=bet_amount*2
        print(f'Congratulations! You win the Jackpot. Your winnings: {winnings}')
        player_score+=winnings
    elif reel7==reel8==reel9:
        winnings=bet_amount*2
        print(f'Congratulations! You win the Jackpot. Your winnings: {winnings}')
        player_score+=winnings
    else:
        print('Sorry, try again!')
        player_score-=bet_amount
    
    print(f'Your current score: {player_score}')
    
    play_again=input('Do you want to play again? ')
    if play_again.lower() == 'yes':
        spin_slot_machine()
    else:
        print('Thank you for playing!')

spin_slot_machine()