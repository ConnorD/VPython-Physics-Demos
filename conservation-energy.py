from visual import *
from visual.graph import *

window = display(autoscale = False, title="Conservation of Energy", width = 700, height = 700)
gdisplay(x=800, y=000, width=500, height=400, title='Position vs. Time', xtitle='t(s)', ytitle='h(m)')
pos_time = gcurve(color=color.cyan)	 # a graphics curve
gdisplay(x=800, y=400, title='Velocity vs. Time', xtitle='t(s)', ytitle='v(m/s)', width=500)
window.autoscale = True

init_pos_y = 5
ball = sphere(radius = 0.5, pos=(0, init_pos_y, 2))
ball.velocity = vector(0, 0, 0)
floor = box(pos = (0, -5, 0), length = 20, height = 0.5, width = 5)
#floor = sphere(radius = 5)

arrow = arrow(pos = ball.pos, shaftwidth = 0.2, axis = ball.velocity, color=color.red)

deltaT = 0.0005
t = 0

# pos_time = gcurve(display=graph1.display, color=color.cyan)    # a graphics curve
vel_time = gcurve(color=color.red)

bounceCount = 0

while(1):
    rate(2000)
    
    ball.velocity.y += (-9.8 * deltaT)
    
    if (ball.pos.y > init_pos_y):
        ball.pos.y = init_pos_y
        
    pos_time.plot(pos=(t, ball.pos.y + 5 - ball.radius - floor.height/2))	# plot
    vel_time.plot(pos=(t, ball.velocity.y))
    
    # check for collision
    if (ball.pos.y - ball.radius) <= (floor.pos.y + floor.height/2):
        ball.velocity.y = -ball.velocity.y
        bounceCount += 1
        
    arrow.axis = (ball.velocity.x * 0.2, ball.velocity.y * 0.2, ball.velocity.z * 0.2)
    ball.pos += ball.velocity * deltaT
    arrow.pos = ball.pos
    
    t += deltaT
