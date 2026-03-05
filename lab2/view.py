from tkinter import *
from model import *
import time 
root = Tk()
canvas = Canvas(root, bg="white",width=800, height=600)
canvas.pack()
#o = canvas.create_oval(80, 30, 140, 150, fill="blue")

input()

# Task (8/12): Define a new function to_canvas_coords(canvas, x)

def to_canvas_coords(canvas, x):
    h = canvas.winfo_reqheight()
    w = canvas.winfo_reqwidth()
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
def create_oval(canvas, particle):
    o = canvas.create_oval(0,0,0,0, fill = "blue")
    u1, u2 = particle.bounding_box()
     # Pass u1 and u2 to move_oval (and remember move_oval returns None, so don't assign it to 'o')
    move_oval(o, u1, u2)
    return o


## Temporary test—remove for final submission! ##
for n in range(5):
    particle = Particle(0, Vec(n,n), Vec(0,0), 0.2)
    create_oval(canvas, partice)
    canvas.update()
    time.sleep(1)

# Task (12/12): Define a function simulation_loop(f, timestep, particles)
def simulation_loop(f, timestep, particles):
    # Set up one graphical object (oval) for each particle
    ovals = []
    for p in particles:
        ovals.append(create_oval(canvas, p))
        
    # Repeat the following steps in an infinite loop
    while True:
        # 1. call f(timestep, particles)
        f(timestep, particles)
        
        # 2 & 3. Move the particle and move the oval
        for i in range(len(particles)):
            p = particles[i]
            o = ovals[i]
            
            # 2. move the particle according to the inertial Newton law
            p.inertial_move(timestep)
            
            # 3. move each oval to the new position of the particle
            u1, u2 = p.bounding_box()
            move_oval(o, u1, u2)
            
        # At the end of step 3, update the canvas
        canvas.update()
        
        # (Optional) Add a slight delay so the animation runs smoothly 
        # time.sleep(timestep)