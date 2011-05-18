from visual import *

h = w = 500
scene.width = w
scene.height = h
scene.x = scene.y = 0
wide = 1.
scene.fov = 0.001
scene.range = wide
scene.userzoom = 0
scene.userspin = 0
ball = sphere(pos=(-0.9*wide,0,0), radius=wide/20, color=color.cyan)
ball.mass = 50.
ball.p = vector()
trail = curve(color=ball.color)
dt = 0.1
Foffset = vector(0,0,-ball.radius)
Fvec = arrow(pos=ball.pos+Foffset, axis=(0,0,0), shaftwidth=wide/30., color=color.green)
pvec = arrow(pos=ball.pos, axis=(0,0,0), shaftwidth=wide/30., color=color.red)
Fmouse = 1. # F mouse scale factor
Fview = 1. # F view scale factor
pview = 0.05 # p view scale factor

scene2 = display(x=w, y=0, width=w, height=h)
scene2.range = wide
scene2.userzoom = 0
scene2.userspin = 0
Fvec2 = arrow(display=scene2, axis=(0,0,0), shaftwidth=wide/30., color=color.green)
sphere(display=scene2, radius=Fvec2.shaftwidth/2., color=Fvec2.color)
scene.select()

drag = 0
F = vector(0,0,0)
while 1:
    rate(40)
    if scene2.mouse.events:
        m = scene2.mouse.getevent()
        if m.drag == 'left' or m.press == 'left':
            drag = 1
        elif m.drop == 'left':
            drag = 0
    if drag:
        F = Fmouse*scene2.mouse.pos
    Fvec2.axis = Fview*F
    ball.p = ball.p+F*dt
    ball.pos = ball.pos+(ball.p/ball.mass)*dt
    trail.append(pos=ball.pos)
    if not (-wide <= ball.x <= wide):
        trail.visible = 0
        trail = curve(color=ball.color)
        if ball.p.x > 0:
            ball.x = -wide
        else:
            ball.x = wide
    if not (-wide <= ball.y <= wide):
        trail.visible = 0
        trail = curve(color=ball.color)
        if ball.p.y > 0:
            ball.y = -wide
        else:
            ball.y = wide
    Fvec.pos = ball.pos+Foffset
    Fvec.axis = Fview*F
    pvec.pos = ball.pos
    pvec.axis = pview*ball.p