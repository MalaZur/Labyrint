from levels import levels
from playground import root, canvas, walls, keys, doors, exits, players, secrets, final, create_level

current_level = 0
create_level(levels[current_level])


def playerMove(event):
    cur = current_level
    player = players[0]
    key = event.keysym
    c = 0
    x = 0
    y = 0
    change = 5
    if key == "Up":
        canvas.move(player, x, y-change)
        c = 1
    if key == "Down":
        canvas.move(player, x, y+change)
        c = 2
    if key == "Left":
        canvas.move(player, x-change, y)
        c = 3
    if key == "Right":
        canvas.move(player, x+change, y)
        c = 4
    for wall in walls:
        x1, y1, x2, y2 = canvas.coords(wall)
        if player in canvas.find_overlapping(x1,y1,x2,y2):
            if c == 1:
                canvas.move(player, x, change)
            if c == 2:
                canvas.move(player, x, -change)
            if c == 3:
                canvas.move(player, change, y)
            if c == 4:
                canvas.move(player, -change, y)
    for key in keys:
        x1,y1,x2,y2 = canvas.coords(key)
        if player in canvas.find_overlapping(x1,y1,x2,y2):
            canvas.delete(key)
            keys.remove(key)
    for door in doors:
        if canvas.itemcget(door, 'fill') == 'red':
            x1, y1, x2, y2 = canvas.coords(door)
            if player in canvas.find_overlapping(x1,y1,x2,y2):
                canvas.move(player, x, -change)
    if len(keys) == 0:
        for i in range(len(doors)):
            canvas.itemconfig(doors[i], fill='green', outline='green')
    for exit in exits:
        x1, y1, x2, y2 = canvas.coords(exit)
        if player in canvas.find_overlapping(x1,y1,x2,y2):
            canvas.delete('all')
            if cur < len(levels)-1:
                create_level(levels[cur+1])
                cur += 1
            if cur == len(levels):
                canvas.pack_forget()
                final()
                canvas.unbind_all('<key>')
                return



canvas.bind_all('<Key>', playerMove)
root.mainloop()