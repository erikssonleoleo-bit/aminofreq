from view import*
from model import*
from math import*

n = 20
particles = []
for i in range(n):
    theta = i*2*math.pi/n
    u = Vec(math.cos(theta),math.sin(theta))
    pos = 10 * u
    vel = -1 * u 
    particles.append(Particle(1,pos,vel,0.2))


def combined_walls(dt, particles):
    # Fjäderkonstanten k (hur "hårda" väggarna är) enligt instruktionerna
    k = 5  
    
    # 1. Golv (Bottenvägg)
    # Ankarpunkt på y = -10. Normalvektorn pekar UPPÅT (0, 1) in mot mitten.
    wall_force(dt, particles, k, Vec(0, 1), Vec(0, -10))
    
    # 2. Tak (Toppvägg)
    # Ankarpunkt på y = 10. Normalvektorn pekar NEDÅT (0, -1) in mot mitten.
    wall_force(dt, particles, k, Vec(0, -1), Vec(0, 10))
    
    # 3. Vänster vägg
    # Ankarpunkt på x = -10. Normalvektorn pekar åt HÖGER (1, 0) in mot mitten.
    wall_force(dt, particles, k, Vec(1, 0), Vec(-10, 0))
    
    # 4. Höger vägg
    # Ankarpunkt på x = 10. Normalvektorn pekar åt VÄNSTER (-1, 0) in mot mitten.
    wall_force(dt, particles, k, Vec(-1, 0), Vec(10, 0))

simulation_loop(combined_walls, 0.00005, particles)