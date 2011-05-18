from visual import *

floor = box(pos = (0, -1, 0), width = 5, length = 4, height = 0.05, color = color.blue)
ball1 = sphere(radius = 0.4, pos = (-1, 0, 0))
ball1.pos.y = floor.pos.y + floor.height/2 + ball1.radius
ball1.mass = 4
ball2 = sphere(radius = 0.1, pos = (1, 0, 0))
ball2.pos.y = floor.pos.y + floor.height/2 + ball2.radius
ball2.mass = 1

dt = 0.01
t = 0
collided = False

while(1):
    rate(50)
    
    if collided == False:
        ball1.velocity = vector(0.5, 0, 0)
        ball2.velocity = vector(-0.5, 0, 0)
    
    if mag(ball1.pos - ball2.pos) <= (ball1.radius + ball2.radius):
        ball1.velocity = -ball1.velocity
        ball2.velocity = -ball2.velocity
        collided = True
    
    ball1.pos += ball1.velocity * dt
    ball2.pos += ball2.velocity * dt
    t += dt