import tkinter as tk
import random
from PIL import Image, ImageTk
import os

user_score = 0
computer_score = 0
total_turns = 10

choices = ["rock", "paper", "scissors"]


class AnimatedLabel(tk.Label):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.after_id = None


def update_result_label(result_label, result):
    
    colors = ["green", "blue", "red", "purple", "orange"]
    
    def change_color(index=0):
        result_label.config(fg=colors[index])
        result_label.after(500, change_color, (index + 1) % len(colors))
    
    
    if result_label.after_id:
        result_label.after_cancel(result_label.after_id)
    result_label.after_id = result_label.after(0, change_color)

    result_label.config(text=result)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice_label, computer_choice_label, result_label, character_label, score_label):
    global total_turns, user_score, computer_score
    if total_turns > 0:
        user_choice = user_choice_var.get()
        computer_choice = random.choice(choices)

        user_choice_image = Image.open(os.path.join("C:/Users/user/Pictures/PIL", f"{user_choice}.png"))
        computer_choice_image = Image.open(os.path.join("C:/Users/user/Pictures/PIL", f"{computer_choice}.png"))

        user_choice_image = ImageTk.PhotoImage(user_choice_image)
        computer_choice_image = ImageTk.PhotoImage(computer_choice_image)

        user_choice_label.config(image=user_choice_image)
        computer_choice_label.config(image=computer_choice_image)

        user_choice_label.image = user_choice_image
        computer_choice_label.image = computer_choice_image

        result = determine_winner(user_choice, computer_choice)
        update_result_label(result_label, result)

        if "You" in result:
            user_score += 1
        elif "Computer" in result:
            computer_score += 1

        total_turns -= 1

        turns_label.config(text=f"Turns left: {total_turns}")
        score_label.config(text=f"Your Score: {user_score} | Computer Score: {computer_score}")

        if total_turns == 0:
            if user_score > computer_score:
                character_label.config(text="Congratulations! You Win!", fg="green")
            elif user_score < computer_score:
                character_label.config(text="Computer Wins! Better luck next time.", fg="red")
            else:
                character_label.config(text="It's a tie game!", fg="blue")

def reset_game():
    global user_score, computer_score, total_turns
    user_score = 0
    computer_score = 0
    total_turns = int(turns_var.get())
    user_choice_var.set("rock")
    user_choice_label.config(image="")
    computer_choice_label.config(image="")
    result_label.config(text="")
    turns_label.config(text=f"Turns left: {total_turns}")
    score_label.config(text="Your Score: 0 | Computer Score: 0")
    character_label.config(text="")

def change_game_background_color(color):
    game_frame.config(bg=color)

def set_background_image():
    background_image = Image.open("C:/Users/user/Pictures/PIL/background.png")
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(main_frame, image=background_photo)
    background_label.image = background_photo
    background_label.place(relwidth=1, relheight=1)

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
game_frame = tk.Frame(root)
main_frame = tk.Frame(root, bg="sky blue")
main_frame.pack(fill="both", expand=True)

set_background_image()

main_label = tk.Label(main_frame, text="Welcome to Rock-Paper-Scissors Game!", font=("Arial", 20), bg="sky blue")
main_label.pack(pady=50)

enter_button = tk.Button(main_frame, text="Enter Game", command=lambda: enter_game(main_frame, game_frame), font=("Arial", 16))
enter_button.pack()

game_frame = tk.Frame(root, bg="white")

user_choice_var = tk.StringVar()
user_choice_var.set("rock")

rock_button = tk.Radiobutton(game_frame, text="Rock", variable=user_choice_var, value="rock", font=("Arial", 12))
paper_button = tk.Radiobutton(game_frame, text="Paper", variable=user_choice_var, value="paper", font=("Arial", 12))
scissors_button = tk.Radiobutton(game_frame, text="Scissors", variable=user_choice_var, value="scissors", font=("Arial", 12))

rock_button.grid(row=0, column=0, padx=20)
paper_button.grid(row=0, column=1, padx=20)
scissors_button.grid(row=0, column=2, padx=20)

play_button = tk.Button(game_frame, text="Play", command=lambda: play_game(user_choice_label, computer_choice_label, result_label, character_label, score_label), font=("Arial", 12))
play_button.grid(row=1, column=1, pady=20)

user_choice_label = AnimatedLabel(game_frame)
user_choice_label.grid(row=2, column=0, padx=20)
computer_choice_label = AnimatedLabel(game_frame)
computer_choice_label.grid(row=2, column=2, padx=20)

result_label = AnimatedLabel(game_frame, text="", font=("Arial", 14))
result_label.grid(row=3, column=1, pady=20)

turns_var = tk.StringVar()
turns_var.set("10")
turns_label = tk.Label(game_frame, text=f"Turns left: {total_turns}", font=("Arial", 12))
turns_label.grid(row=4, column=1, pady=20)

turns_dropdown = tk.OptionMenu(game_frame, turns_var, "10", "20", "30", "40")
turns_dropdown.grid(row=5, column=1, pady=10)

try_again_button = tk.Button(game_frame, text="Try Again", command=reset_game, font=("Arial", 12))
try_again_button.grid(row=6, column=1, pady=10)

background_color_label = tk.Label(game_frame, text="Choose Background Color:")
background_color_label.grid(row=7, column=0, padx=20)

background_color_var = tk.StringVar()
background_color_var.set("white")

background_color_dropdown = tk.OptionMenu(game_frame, background_color_var, "white", "black", "sky blue", "Gray")
background_color_dropdown.grid(row=7, column=1, padx=20)

apply_color_button = tk.Button(game_frame, text="Apply Color", command=lambda: change_game_background_color(background_color_var.get()), font=("Arial", 12))
apply_color_button.grid(row=7, column=2, padx=20)

score_label = tk.Label(game_frame, text="Your Score: 0 | Computer Score: 0", font=("Arial", 12))
score_label.grid(row=8, column=1, pady=10)

character_label = tk.Label(game_frame, text="", font=("Arial", 16))
character_label.grid(row=9, column=1, pady=20)

game_frame.pack_forget()

def enter_game(main_frame, game_frame):
    main_frame.pack_forget()
    game_frame.pack()

root.mainloop()
