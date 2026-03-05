from tkinter import *
from model import *
import time 
root = Tk()
canvas = Canvas(root, bg="white",width=800, height=600)
canvas.pack()
#o = canvas.create_oval(80, 30, 140, 150, fill="blue")



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
    create_oval(canvas, particle)
    canvas.update()
    time.sleep(1)

# Task (12/12): Define a function simulation_loop(f, timestep, particles)
import time # (Kontrollera att denna finns med i toppen av filen)

import time

def simulation_loop(f, timestep, particles):
    # Skapa ett grafiskt objekt (oval) för varje partikel och spara i en lista
    ovals = []
    for p in particles:
        ovals.append(create_oval(canvas, p))
        
    # Spara tiden innan loopen startar och sätt intervallet till 1/30 sekund
    last_update = time.time()
    update_interval = 1.0 / 30.0 
        
    # Oändlig loop som driver hela simuleringen
    while True:
        # 1. Applicera krafter på alla partiklar
        f(timestep, particles)
        
        # 2. Flytta partiklarna enligt Newtons lagar (fysikuppdatering)
        for p in particles:
            p.inertial_move(timestep)
            
        # Kolla vad klockan är just nu
        current_time = time.time()
        
        # 3. Uppdatera grafiken endast om det har gått minst 1/30 sekund
        if current_time - last_update >= update_interval:
            
            # Gå igenom alla partiklar och deras motsvarande grafiska ovaler
            for i in range(len(particles)):
                p = particles[i]
                o = ovals[i]
                
                # Hämta den nya begränsningsboxen (bounding box) för partikeln
                u1, u2 = p.bounding_box()
                
                # Flytta ovalen på skärmen
                move_oval(o, u1, u2)
                
            # Rita om canvasen
            canvas.update()
            
            # Återställ klockan för att börja räkna ner till nästa bilduppdatering
            last_update = current_time