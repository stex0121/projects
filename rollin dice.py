import random

dice_art = {
    1: (
        "┌───────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└───────┘"
    ),
    2: (
        "┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘"
    ),
    3: (
        "┌───────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└───────┘"
    ),
    4: (
        "┌───────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└───────┘"
    ),
    5: (
        "┌───────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└───────┘"
    ),
    6: (
        "┌───────┐",
        "│ ●   ● │",
        "│ ●   ● │",
        "│ ●   ● │",
        "└───────┘"
    )
}

def play_game():
    dice = []
    total = 0
    num_of_dice = int(input('How many dice ? :'))

    for _ in range(num_of_dice):
        dice.append(random.randint(1, 6))

    for die in dice:
        if die in dice_art:
            for line in dice_art[die]:
                print(line)
        else:
            print("ASCII art not found for this dice face")

        total += die

    print(f'Total: {total}')

    play_again = input("Do you want to play again? (yes/no): ").lower()
    return play_again == "yes"


while True:
    if not play_game():
        print("Thank you for playing!")
        break
