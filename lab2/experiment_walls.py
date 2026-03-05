from view import*
from model import*
from math import

n = 20
particles = []
for i in range(n)
    theta = i*2*math.pi/n
    u = Vec(math.cos(theta),math.sin(theta))
    pos = 10 * u
    vel = -1 * u 
    particles.append(Particle(1,pos,vel,0.2))


def combined_walls(dt, particles):
    k = 5 
    a_

simulation_loop(combined_walls, )