import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("280x400")

current_player = "X"
buttons = []
game_over = False
score_x = 0
score_o = 0

# Метки для отображения счёта
score_label = tk.Label(window, text=f"Счет: Игрок X: {score_x}  Игрок O: {score_o}", font=("Arial", 14))
score_label.grid(row=4, column=0, columnspan=3)

def check_winner():
   for i in range(3):
       if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
           return True
       if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
           return True

   if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
       return True
   if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
       return True

   return False


def check_draw():
    for row in buttons:
        for button in row:
            if button["text"] == "":
                return False
    return True

def on_click(row, col):
   global current_player, game_over, score_x, score_o

   if buttons[row][col]['text'] != "":
       return

   buttons[row][col]['text'] = current_player

   # Изменяем цвет фона клетки в зависимости от игрока
   if current_player == "X":
       buttons[row][col].config(bg="blue")
   else:
       buttons[row][col].config(bg="red")

   if check_winner():
       messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
       if current_player == "X":
           score_x += 1
       else:
           score_o += 1
       score_label.config(text=f"Счет: Игрок X: {score_x}  Игрок O: {score_o}")

       if score_x >= 3 or score_o >= 3:
           messagebox.showinfo("Игра окончена", f"Игрок {current_player} выиграл игру до 3 побед!")
           reset_game()
       else:
           game_over = True
   elif check_draw():
       messagebox.showinfo("Игра окончена", "Ничья!")
       game_over = True
   else:
       current_player = "O" if current_player == "X" else "X"


for i in range(3):
   row = []
   for j in range(3):
       btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2, command=lambda row=i, col=j: on_click(row, col))
       btn.grid(row=i, column=j)
       row.append(btn)
   buttons.append(row)

def reset_game():
    global current_player, game_over
    current_player = 'X'
    game_over = False

    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text='')  # Очищаем текст кнопок
            buttons[i][j]['state'] = 'normal'  # Включаем кнопки
            buttons[i][j].config(bg='SystemButtonFace')  # Сбрасываем цвет фона

# Кнопка для сброса игры
reset_button = tk.Button(window, text='Очистить поле', font=('Arial', 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

# Функция для сброса счета
def reset_score():
    global score_x, score_o
    score_x = 0
    score_o = 0
    score_label.config(text=f"Счет: Игрок X: {score_x}  Игрок O: {score_o}")

# Кнопка для сброса счета
reset_score_button = tk.Button(window, text='Сбросить игру', font=('Arial', 14), command=reset_score)
reset_score_button.grid(row=5, column=0, columnspan=3)


window.mainloop()