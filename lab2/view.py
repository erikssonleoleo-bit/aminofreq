from tkinter import *
from model import *
import time 
root = Tk()
canvas = Canvas(root, bg="white",width=800, height=600)
canvas.pack()



def to_canvas_coords(canvas, x):
    h = canvas.winfo_reqheight()
    w = canvas.winfo_reqwidth()
    scale = h / 20
    can_x = w / 2 + x.x * scale
    can_y = h / 2 - x.y * scale
    return Vec(can_x, can_y)


def move_oval(o, u1, u2):
    c1 = to_canvas_coords(canvas, u1)
    c2 = to_canvas_coords(canvas, u2)
    canvas.coords(o, c1.x, c1.y, c2.x, c2.y)
    canvas.update()


def create_oval(canvas, particle):
    o = canvas.create_oval(0,0,0,0, fill = "blue")
    u1, u2 = particle.bounding_box()
    move_oval(o, u1, u2)
    return o

def simulation_loop(f, timestep, particles):
    ovals = []
    for p in particles:
        ovals.append(create_oval(canvas, p))
    last_update = time.time()
    update_interval = 1.0 / 30.0 
    while True:
        f(timestep, particles)
        for p in particles:
            p.inertial_move(timestep)
        current_time = time.time()
        if current_time - last_update >= update_interval:
            for i in range(len(particles)):
                p = particles[i]
                o = ovals[i]
                u1, u2 = p.bounding_box()
                move_oval(o, u1, u2)
            canvas.update()
            last_update = current_time




