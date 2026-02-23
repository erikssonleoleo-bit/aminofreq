# Task 7/12

from tkinter import *
from model import *
import time 
root = Tk()
canvas = Canvas(root, bg="white",width=800, height=600)
canvas.pack()
o = canvas.create_oval(80, 30, 140, 150, fill="blue")

input()

# Task (8/12): Define a new function to_canvas_coords(canvas, x)

def to_canvas_coords(canvas, x):
    h = canvas.winfo_reqheight()
    w = canvas.winfo_reqwitfh()
    scale = h / 20
    can_x = w / 2 + x.x * scale
    can_y = h / 2 - x.y * scale
    return Vec(can_x, can_y)



# Task (10/12): Define a new function move_oval_to(o, u1, u2)

def move_oval(o, u1, u2):
    c1 = to_canvas_coords(canvas, u1)
    c2 = to_canvas_coords(canvas, u2)
    canvas.coords(o, c1.x, c1.y, c2.x, c2.y)
    canvas.update()
# Task (11/12): Define a new function create_oval(canvas, particle)

# Task (12/12): Define a function simulation_loop(f, timestep, particles