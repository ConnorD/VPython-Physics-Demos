# written by Connor Denman, Sandia High School

from visual import *

scene.fullscreen = 1

slopeangle = radians(30.)
slope = box(pos=(0,0,0),axis=(cos(slopeangle),sin(slopeangle),0),length=6,width=0.4,height=0.1)
ball = sphere(pos=(0.5*slope.length*cos(slopeangle)-0.1*sin(slopeangle),
                   0.5*slope.length*sin(slopeangle)+0.1*cos(slopeangle),0),radius=0.1)
ball.velocity = vector(0, 0, 0)
accelerationx = 9.8 * sin(slopeangle) * cos(slopeangle)
accelerationy = 9.8 * sin(slopeangle) * sin(slopeangle)
arrow = arrow(pos = ball.pos, axis=ball.velocity)
scene.autoscale = 0
scene.scale = (0.22,0.22,0.22)

t = 0
dt = 0.01

while 1:
    rate(50)
    
    ball.velocity += vector(-slope.axis.x - accelerationx, -slope.axis.y - accelerationy, 0) * dt
    ball.pos += ball.velocity * dt