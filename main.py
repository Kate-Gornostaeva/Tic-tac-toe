import tkinter as tk
from tkinter import messagebox

# Инициализация основной переменной
current_player = 'X'
game_over = False
board = [['' for _ in range(3)] for _ in range(3)]


def reset_game():
    global current_player, game_over, board
    current_player = 'X'
    game_over = False
    board = [['' for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text='')  # Очищаем текст кнопок
            buttons[i][j]['state'] = 'normal'  # Включаем кнопки


def make_move(row, col):
    global current_player, game_over

    if board[row][col] == '' and not game_over:
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)

        if check_winner():
            messagebox.showinfo("Игра окончена", f"Игрок {current_player} выиграл!")
            game_over = True
        elif all(board[i][j] != '' for i in range(3) for j in range(3)):
            messagebox.showinfo("Игра окончена", "Ничья!")
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'


def check_winner():
    # Проверка по строкам и столбцам
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return True
        if board[0][i] == board[1][i] == board[2][i] != '':
            return True
    # Проверка по диагоналям
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        return True
    return False

# Создание основного окна
root = tk.Tk()
root.title("Крестики-Нолики")

# Создание кнопок
buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text='', font=('Arial', 24), width=5, height=2,command=lambda row=i, col=j: make_move(row, col))
        buttons[i][j].grid(row=i, column=j)

# Кнопка для сброса игры
reset_button = tk.Button(root, text='Сбросить игру', font=('Arial', 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

root.mainloop()