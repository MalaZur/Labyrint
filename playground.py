from tkinter import * 
from random import *
import levels
# Настройки окна
root = Tk() 
root.geometry('470x470')
root.title('Лабиринт')
root.resizable(False, False)

# Функции


def final():
    title = Label(text="You won!", bg='green')
    title.pack(side=TOP, pady=220)

canvas = Canvas(width=450, height=450, bg='white', relief=SOLID)
canvas.pack(side=TOP, pady=10)



side = 25


walls = []
doors = []
keys = []
exits = []
secrets = []
players = []



def create_level(level):
    walls.clear()
    doors.clear()
    keys.clear()
    exits.clear()
    players.clear()
    x = 0
    y = -25
    for line in level:
        x = 0
        y += side
        for block in line:
            if block == 'S':
                secret = canvas.create_rectangle(x,y,x + side, y + side, fill='black', outline='black')
                secrets.append(secret)                
            elif block == 'W':
                wall = canvas.create_rectangle(x,y,x + side, y + side, fill='black', outline='black')
                walls.append(wall)
            elif block == 'K':
                key = canvas.create_rectangle(x,y,x + side, y + side, fill='yellow', outline='black')
                keys.append(key)
            elif block == 'D':
                door = canvas.create_rectangle(x,y,x + side, y + side, fill='red', outline='black')
                doors.append(door)    
            elif block == 'E':
                exit = canvas.create_rectangle(x,y,x + side, y + side, fill='orange', outline='orange')
                exits.append(exit)
            elif block == 'P':
                player = canvas.create_rectangle(x+1,y+1,x + side - 1, y + side - 1, fill='blue', outline='blue')
                players.append(player)
            x += side





# Конец программы
if __name__ == "__main__":
    create_level(levels.level1)
    root.mainloop()