import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, words):
        # Initialize the HangmanGame object with a list of words
        self.words = words
        # Create a Tkinter window
        self.window = tk.Tk()
        # Set the title of the window
        self.window.title("Hangman Game")
        # Create all the widgets for the game
        self.create_widgets()
        # Start a new game
        self.reset_game()

    def reset_game(self):
        # Reset the game state
        self.word_to_guess = random.choice(self.words)
        self.guessed_letters = []
        self.attempts = 6
        # Update the display to reflect the new game state
        self.update_display()

    def check_win(self):
        # Check if the player has won the game
        return all(letter in self.guessed_letters for letter in self.word_to_guess)

    def check_loss(self):
        # Check if the player has lost the game
        return self.attempts == 0

    def guess_letter(self):
        # Handle a letter guess from the player
        letter = self.letter_entry.get().lower()
        if letter.isalpha() and len(letter) == 1:
            if letter in self.guessed_letters:
                messagebox.showinfo("Hangman", f"You already guessed '{letter}'")
            elif letter in self.word_to_guess:
                self.guessed_letters.append(letter)
                self.update_display()
                if self.check_win():
                    messagebox.showinfo("Hangman", "Congratulations, you win!")
                    self.reset_game()
            else:
                self.guessed_letters.append(letter)
                self.attempts -= 1
                self.update_display()
                if self.check_loss():
                    messagebox.showinfo("Hangman", f"You lose! The word was '{self.word_to_guess}'")
                    self.reset_game()
            self.letter_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Hangman", "Please enter a single letter.")

    def update_display(self):
        # Update the display with the current game state
        display_word = ""
        for letter in self.word_to_guess:
            if letter in self.guessed_letters:
                display_word += letter
            else:
                display_word += "_"
            display_word += " "
        self.word_label.config(text=display_word)
        self.attempts_label.config(text=f"Attempts left: {self.attempts}")
        self.draw_hangman()

    def draw_hangman(self):
        # Draw the hangman figure based on the number of attempts left
        self.canvas.delete("hangman")
        if self.attempts < 6:
            self.canvas.create_oval(125, 125, 175, 175, width=4, tags="hangman")
        if self.attempts < 5:
            self.canvas.create_line(150, 175, 150, 225, width=4, tags="hangman")
        if self.attempts < 4:
            self.canvas.create_line(150, 200, 125, 175, width=4, tags="hangman")
        if self.attempts < 3:
            self.canvas.create_line(150, 200, 175, 175, width=4, tags="hangman")
        if self.attempts < 2:
            self.canvas.create_line(150, 225, 125, 250, width=4, tags="hangman")
        if self.attempts < 1:
            self.canvas.create_line(150, 225, 175, 250, width=4, tags="hangman")

    def create_widgets(self):
        # Create all the GUI widgets for the game
        self.word_label = tk.Label(self.window, text="", font=("Arial", 24))
        self.attempts_label = tk.Label(self.window, text="", font=("Arial", 16))
        self.letter_entry = tk.Entry(self.window, width=5, font=("Arial", 16))
        self.guess_button = tk.Button(self.window, text="Guess", command=self.guess_letter)
        self.reset_button = tk.Button(self.window, text="Reset", command=self.reset_game)
        self.canvas = tk.Canvas(self.window, width=300, height=300)
        self.canvas.create_line(50, 250, 250, 250, width=4)
        self.canvas.create_line(200, 250, 200, 100, width=4)
        self.canvas.create_line(100, 100, 200, 100, width=4)
        self.canvas.create_line(150, 100, 150, 120, width=4)

        # Pack the widgets into the window
        self.word_label.pack()
        self.attempts_label.pack()
        self.letter_entry.pack()
        self.guess_button.pack()
        self.reset_button.pack()
        self.canvas.pack()

# Define a list of words for the game
words = ["treasure", "island", "united states of america", "python", "metropol", "jupiter", "hanged man"]

# Create an instance of the HangmanGame class and start the Tkinter event loop
hangman_game = HangmanGame(words)
hangman_game.window.mainloop()