import tkinter as tk
from tkinter import messagebox
import random

window = tk.Tk()
window.title("Tic Tac Toe (You vs Smart Computer)")

current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = []

# Check for winner
def check_winner(player):
    for row in board:
        if all(cell == player for cell in row):  
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True  
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check for draw
def is_draw():
    return all(cell != "" for row in board for cell in row)

# AI picks winning move, blocking move, or random
def computer_move():
    global current_player

    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ""]

    # 1. Try to win
    for r, c in empty_cells:
        board[r][c] = "O"
        if check_winner("O"):
            update_button(r, c, "O")
            end_game("💻 Computer wins!")
            return
        board[r][c] = ""

    # 2. Block player
    for r, c in empty_cells:
        board[r][c] = "X"
        if check_winner("X"):
            board[r][c] = "O"
            update_button(r, c, "O")
            if check_winner("O"):
                end_game("💻 Computer wins!")
            else:
                current_player = "X"
            return
        board[r][c] = ""

    # 3. Pick random
    if empty_cells:
        r, c = random.choice(empty_cells)
        board[r][c] = "O"
        update_button(r, c, "O")
        if check_winner("O"):
            end_game("💻 Computer wins!")
        elif is_draw():
            end_game("🤝 It's a draw!")
        else:
            current_player = "X"

# Update button text
def update_button(r, c, text):
    buttons[r][c].config(text=text)

# Handle player click
def handle_click(r, c):
    global current_player

    if board[r][c] == "" and current_player == "X":
        board[r][c] = "X"
        update_button(r, c, "X")

        if check_winner("X"):
            end_game("🎉 You win!")
        elif is_draw():
            end_game("🤝 It's a draw!")
        else:
            current_player = "O"
            window.after(500, computer_move)

# End game and show reset option
def end_game(message):
    messagebox.showinfo("Game Over", message)
    reset_button.config(state="normal")

# Reset game
def reset_game():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(text="")
    reset_button.config(state="disabled")

# Build board
for r in range(3):
    row = []
    for c in range(3):
        btn = tk.Button(window, text="", font=("Helvetica", 24), width=5, height=2,
                        command=lambda r=r, c=c: handle_click(r, c))
        btn.grid(row=r, column=c)
        row.append(btn)
    buttons.append(row)

# Reset button
reset_button = tk.Button(window, text="Reset", font=("Helvetica", 14), state="disabled", command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, pady=10)

window.mainloop()
