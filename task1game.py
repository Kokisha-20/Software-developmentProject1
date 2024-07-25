import tkinter as tk
from tkinter import messagebox
import random
class GuessingGame:
    def __init__(self,master):
        self.master = master
        master.title("GUESSING GAME")
        self.random_number = random.randint(1,100)
        self.attempts = 0
        self.label = tk.Label(master,text="Guess a number between 1 and 100:")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.guess_button = tk.Button(master,text="Guess",command=self.check_guess)
        self.guess_button.pack()
        self.result_label = tk.Label(master,text="")
        self.result_label.pack()
    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts+=1
            if guess < self.random_number:
                self.result_label.config(text="Guess is Too low! Try again")
            elif guess > self.random_number:
                self.result_label.config(text="Guess is Too high! Try again")
            else:
                self.result_label.config(text="Correct! You've guessed the number")
                messagebox.showinfo("Congratulations!",f"You've guessed the number in {self.attempts} attempts!")
                self.reset_game()
        except ValueError:
            self.result_label.config(text="Please enter a valid integer")
    def reset_game(self):
        self.random_number = random.randint(1,100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
root=tk.Tk()
guessing_game = GuessingGame(root)
root.mainloop()