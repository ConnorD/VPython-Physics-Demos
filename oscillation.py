from __future__ import division
from visual import *

## Ruth Chabay 2003-03-18
## Semi-classical visualization of quantum oscillator.

scene.x = scene.y = 0
scene.width = scene.height = 600
scene.background = color.white
scene.foreground = color.black
scene.title="quantum oscillator"

print """Click on an energy level to put the
oscillator into that state.
"""

class helix:
    def __init__(self, pos=vector(), axis=vector(1,0,0), radius=0.2, coils=5,
               thickness=None, color=None):
        self.frame = frame(pos=vector(pos), axis=norm(axis))
        self.pos = vector(pos)
        self.axis = vector(axis)
        self.length = mag(axis)
        self.radius = radius
        self.coils = coils
        if thickness == None:
            thickness = radius/20.
        k = self.coils*(2.*pi/self.length)
        dx = (self.length/self.coils)/12.
        xx=arange(0,self.length+dx,dx)
        self.helix = curve(frame = self.frame, radius=thickness/2.,
                           color=color, x=xx, y=radius*sin(k*xx),
                           z=radius*cos(k*xx))
            
    def modify(self, pos=None, axis=None, length=None):
        oldlength = self.length
        if pos <> None:
            self.frame.pos = vector(pos)
            self.pos = vector(pos)
        if axis <> None:
            self.axis = vector(axis)
            self.frame.axis = vector(axis)
            self.length = mag(axis)
        if length <> None:
            self.length = length
        k = self.coils*(2.*pi/self.length)
        dx = (self.length/self.coils)/12.
        x = 0.
        lindex = len(self.helix.pos)
        for index in range(lindex):
            self.helix.pos[index][0] = self.helix.pos[index][0]*self.length/oldlength
            x = x+dx


def U(s):
    global ks
    Us = 0.5*ks*s**2
    return Us

showguides = 0
L0 = 10
U0 = -10
dU = 2
m1 = sphere(pos=(-L0,0.5*5**2,0), radius=0.5, color=color.red)
m2 = sphere(pos=(0,0.5*5**2,0), radius=0.5, color=color.cyan)
m1.mass = 0.025     ## 14*1.7e-27
m2.mass = 0.025     ## 14*1.7e-27
ks = 1.2        ## 200
omega = sqrt(ks/m2.mass)
##print omega
spring = helix(pos=m1.pos, axis=(m2.pos-m1.pos), radius=0.40, coils=10,
               thickness=0.2, color=(.7,.5,0))
eqpos = cylinder(pos=(0,U0,0), axis=(0,18,0), radius=0.05, color=(.6,.6,.6))
xx = arange(-5.8, 5.3, 0.1)
well=curve(radius=0.2, x=xx, y=.5*ks*xx**2+U0, z=0, color=(.7,.7,.7))
well.append(pos=(8,.5*ks*5.2**2+U0,0))
vline1=cylinder(pos=(-5,U0,0), axis=(0,15,0), radius=0.05, color=(.6,.6,.6),
                visible=showguides)
vline2=cylinder(pos=(5,U0,0), axis=(0,15,0), radius=0.05, color=(.6,.6,.6),
                visible=showguides)
scene.autoscale = 0
levels = []
for Ux in arange(0.5*dU, 7.51*dU, dU):
    s = sqrt(2*Ux/ks)
    l1 = cylinder(radius=0.2, pos=(-s, Ux+U0, 0), axis = vector(2*s,0,0),
                  color=color.white)
    levels.append(l1)
t = 0.0
dt = 0.003
oldlvl = None
lvl = None
RUN = 0
while 1:
    if (not scene.mouse.clicked) and RUN:
        rate(200)
        m2.pos = vector(Ampl*cos(omega*t),m2.pos.y, m2.pos.z)
        spring.modify(axis = m2.pos - m1.pos)
        t = t+dt
    else:
        scene.mouse.getclick()
        a = scene.mouse.pick
        if a in levels:
            oldlvl = lvl
            lvl = a
            lvl.color=color.red
            if oldlvl is not None:
                oldlvl.color = color.white
            Ampl = abs(lvl.pos.x)
            vline1.pos = lvl.pos
            vline2.pos = lvl.pos+lvl.axis
            RUN = 1
        elif scene.mouse.pos.y > .5*ks*5.2**2+U0:
            RUN = 0
            if lvl is not None:
                lvl.color = color.white
            while m2.pos.x < 2*L0:
                rate(200)
                m2.pos.x += L0/100
            continue
        else:
            continue