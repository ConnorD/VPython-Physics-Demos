from visual import *
from visual.graph import *

window = display(autoscale = False, title="Projectile", width = 1000, height = 800)
window.autoscale = True

ball = sphere(make_trail = True, radius = 0.5, pos=(-15, 1.0, 2), color = color.red)
ball.velocity = vector(10, 14, 0)
floor = box(pos = (0, 0, 0), length = 30, height = 0.5, width = 5, color=color.blue)
#floor = sphere(radius = 5)

res_arrow = arrow(pos = ball.pos, shaftwidth = 0.2, axis = ball.velocity)
vert_arrow = arrow(pos=ball.pos, shaftwidth = 0.2, axis=(0, ball.velocity.y, 0), color=color.green)
horiz_arrow = arrow(pos = ball.pos, shaftwidth = 0.2, axis=(ball.velocity.x, 0, 0), color=color.cyan)

deltaT = 0.01
t = 0

gdisplay(x=window.x + window.width, y=000, width=400, height=400, title='Height vs. Time', xtitle='t', ytitle='h')
height_t = gcurve(color=color.red)
gdisplay(x=window.x + window.width, y=400, title='Velocity vs. Time', xtitle='t', ytitle='v')
vel_t = gcurve(color=res_arrow.color)
horiz_vel_t = gcurve(color=horiz_arrow.color)
vert_vel_t = gcurve(color=vert_arrow.color)

shouldStop = False

while(shouldStop == False):
    rate(100)
    
    ball.velocity.y += (-9.8 * deltaT)
    
    # check for collision
    if (ball.pos.y - ball.radius) <= floor.height/2:
        shouldStop = True
        
    res_arrow.axis = (ball.velocity.x * 0.2, ball.velocity.y * 0.2, 0)
    vert_arrow.axis = (0, ball.velocity.y * 0.2, 0)
    horiz_arrow.axis = (ball.velocity.x * 0.2, 0, 0)
    ball.pos += ball.velocity * deltaT
    res_arrow.pos = ball.pos
    vert_arrow.pos = ball.pos
    horiz_arrow.pos = ball.pos
    
    height_t.plot(pos=(t, ball.pos.y - ball.radius - floor.height/2))
    vel_t.plot(pos=(t, mag(ball.velocity)))
    horiz_vel_t.plot(pos=(t, ball.velocity.x))
    vert_vel_t.plot(pos=(t, ball.velocity.y))
    
    t += deltaT