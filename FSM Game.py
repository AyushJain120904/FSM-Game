import tkinter as tk
from tkinter import *

root = tk.Tk()

canvas = tk.Canvas(root, width=1900, height=1010)
label = Label(root, text="VIDEO GAME CHARACTER", background="red",font=("Arial", 20))
label.pack()

rect = canvas.create_rectangle((600,300,700,400), fill='red')

def reset():
    global rect
    canvas.delete(rect)
    rect = canvas.create_rectangle((600,300,700,400), fill='red')
    
    FW.config(state=tk.NORMAL)
    FR.config(state=tk.NORMAL)
    BW.config(state=tk.NORMAL)
    BR.config(state=tk.NORMAL)
    UP.config(state=tk.NORMAL)
    DOWN.config(state=tk.NORMAL)
    DEATH.config(state=tk.NORMAL)
    RESET.config(state=tk.NORMAL)
    STOP.config(state=tk.NORMAL)
    canvas.delete(a)
    
def Stop():
    root.after_cancel(coor)
    FW.config(state=tk.NORMAL)
    FR.config(state=tk.NORMAL)
    BW.config(state=tk.NORMAL)
    BR.config(state=tk.NORMAL)
    UP.config(state=tk.NORMAL)
    DOWN.config(state=tk.NORMAL)
    DEATH.config(state=tk.NORMAL)
    RESET.config(state=tk.DISABLED)
    
def forward_walk():
    FW.config(state=tk.DISABLED)
    FR.config(state=tk.DISABLED)
    BW.config(state=tk.DISABLED)
#    BR.config(state=tk.DISABLED)
    UP.config(state=tk.DISABLED)
    DOWN.config(state=tk.DISABLED)
    DEATH.config(state=tk.DISABLED)
    RESET.config(state=tk.DISABLED)

    global coor

    global rect
    coords = canvas.coords(rect)
    x,y,z,w = coords
    new_coords = (coords[0] + 5, coords[1], coords[2] + 5, coords[3])
    canvas.coords(rect, *new_coords)
    if coords[0] > 1900:
         canvas.delete(rect)
         rect = canvas.create_rectangle((0,y,100,w), fill='red')         
    coor = root.after(20, forward_walk)
    
def forward_run():
    FW.config(state=tk.DISABLED)
    FR.config(state=tk.DISABLED)
    BW.config(state=tk.DISABLED)
    BR.config(state=tk.DISABLED)
    UP.config(state=tk.DISABLED)
    DOWN.config(state=tk.DISABLED)
    DEATH.config(state=tk.DISABLED)
    RESET.config(state=tk.DISABLED)

    global coor

    global rect
    coords = canvas.coords(rect)
    x,y,z,w = coords
    new_coords = (coords[0] + 20, coords[1], coords[2] + 20, coords[3])
    canvas.coords(rect, *new_coords)
    if coords[0] > 1900:
        canvas.delete(rect)
        rect = canvas.create_rectangle((0,y,100,w), fill='red')
    coor = root.after(20, forward_run)
    
def backward_walk():
    FW.config(state=tk.DISABLED)
    FR.config(state=tk.DISABLED)
    BW.config(state=tk.DISABLED)
    BR.config(state=tk.DISABLED)
    UP.config(state=tk.DISABLED)
    DOWN.config(state=tk.DISABLED)
    DEATH.config(state=tk.DISABLED)
    RESET.config(state=tk.DISABLED)

    global coor
    global rect
    coords = canvas.coords(rect)
    x,y,z,w = coords
    new_coords = (coords[0] - 5, coords[1], coords[2] - 5, coords[3])
    canvas.coords(rect, *new_coords)
    if coords[2] < 0:
        canvas.delete(rect)
        rect = canvas.create_rectangle((1800,y,1900,w), fill='red')
    coor = root.after(20, backward_walk)
    
def backward_run():
    FW.config(state=tk.DISABLED)
    FR.config(state=tk.DISABLED)
    BW.config(state=tk.DISABLED)
    BR.config(state=tk.DISABLED)
    UP.config(state=tk.DISABLED)
    DOWN.config(state=tk.DISABLED)
    DEATH.config(state=tk.DISABLED)
    RESET.config(state=tk.DISABLED)
    global coor
    global rect
    coords = canvas.coords(rect)
    x,y,z,w = coords
    new_coords = (coords[0] - 20, coords[1], coords[2] - 20, coords[3])
    canvas.coords(rect, *new_coords)
    if coords[2] < 0:
        canvas.delete(rect)
        rect = canvas.create_rectangle((1800,y,1900,w), fill='red')
    coor = root.after(20, backward_run)
    
def Up():
    FW.config(state=tk.DISABLED)
    FR.config(state=tk.DISABLED)
    BW.config(state=tk.DISABLED)
    BR.config(state=tk.DISABLED)
    UP.config(state=tk.DISABLED)
    DOWN.config(state=tk.DISABLED)
    DEATH.config(state=tk.DISABLED)
    RESET.config(state=tk.DISABLED)
    global coor
    global rect
    coords = canvas.coords(rect)
    x,y,z,w = coords
    new_coords = (coords[0] , coords[1] - 10, coords[2] , coords[3] - 10)
    canvas.coords(rect, *new_coords)
    if coords[3] < 0:
        canvas.delete(rect)
        rect = canvas.create_rectangle((x,910,z,1010), fill='red')
    coor = root.after(20, Up)
    
def Down():
    FW.config(state=tk.DISABLED)
    FR.config(state=tk.DISABLED)
    BW.config(state=tk.DISABLED)
    BR.config(state=tk.DISABLED)
    UP.config(state=tk.DISABLED)
    DOWN.config(state=tk.DISABLED)
    DEATH.config(state=tk.DISABLED)
    RESET.config(state=tk.DISABLED)
    global coor
    global rect
    coords = canvas.coords(rect)
    x,y,z,w = coords
    new_coords = (coords[0] , coords[1] + 10, coords[2] , coords[3] + 10)
    canvas.coords(rect, *new_coords)
    if coords[1] > 1010 :
        canvas.delete(rect)
        rect = canvas.create_rectangle((x,0,z,100), fill='red')
    coor = root.after(20, Down)
def death():
    global a 
    a = canvas.create_text(700, 300, text="Dead!", font=("Arial", 200))    
    canvas.itemconfig(rect,fill='gray')
    FW.config(state=tk.DISABLED)
    FR.config(state=tk.DISABLED)
    BW.config(state=tk.DISABLED)
    BR.config(state=tk.DISABLED)
    UP.config(state=tk.DISABLED)
    DOWN.config(state=tk.DISABLED)
    STOP.config(state=tk.DISABLED)
    DEATH.config(state=tk.DISABLED)
    RESET.config(state=tk.NORMAL)

    
FW = tk.Button(root, text="ForwardWalk", command=forward_walk)
FW.place(x=1800,y=320)

FR = tk.Button(root, text="ForwardRun", command=forward_run)
FR.place(x=1800,y=40)

BW = tk.Button(root, text="BackwardWalk", command=backward_walk)
BW.place(x=1800,y=80)

BR = tk.Button(root, text="BackwardRun", command=backward_run)
BR.place(x=1800,y=120)

UP = tk.Button(root, text="Up", command=Up)
UP.place(x=1800,y=160)

DOWN = tk.Button(root, text="Down", command=Down)
DOWN.place(x=1800,y=200)

STOP = tk.Button(root, text="Stop", command=Stop)
STOP.place(x=1800,y=240)

DEATH = tk.Button(root,text='EndGame',comman=death)
DEATH.place(x=1800,y=280)

RESET = tk.Button(root, text="Restart", command=reset, state = tk.DISABLED)
RESET.place(x=1800,y=360)

canvas.pack()

root.mainloop()