from visual import *

display(autoscale = False)
ball = sphere(radius = 0.2, pos = (-2, 0, 0))
ball.velocity = vector(-2, 1, 0)
radius = 2.

t = 0
dt = 0.01
while 1:
    rate(50)
    ball.accel = norm(ball.velocity)
    ball.velocity += ball.accel
    ball.pos += ball.velocity * dt
    t += dt