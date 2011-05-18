from __future__ import division
from visual import *
from visual.graph import *
from visual.controls import *
from math import *


#Parameters
obsloc = 0
tlen = 10
speed = 1.5
framerate = 35
tmax = 10

#Constants
t = 0
dt = 1/framerate

#Wave class
class wave:
    def __init__(self,function,xmin,xmax,step,pos):
        self.curve = []
        self.pos = pos
        self.function = function
        self.xmin = xmin
        self.xmax = xmax
        self.step = step
        for x in arange(xmin,xmax,step):
            exec("y="+function+"(x)")
            self.curve.append((x,y))
        lol = [(a[0]+pos[0],a[1]+pos[1]) for a in self.curve]
        lol.insert(0,(-tlen,0))
        lol.append((tlen,0))
        self.render = curve(pos=lol, radius=0.03)
    def update(self):
        lol = [(a[0]+self.pos[0],a[1]+self.pos[1]) for a in self.curve]
        lol.insert(0,(-tlen,0))
        lol.append((tlen,0))
        self.render.pos = lol
    def observe(self,pos):
        rel = pos-self.pos[0]
        if rel<self.xmax and rel>self.xmin:
            exec("y="+self.function+"(rel)")
            return y
        else:
            return 0

#Additional wave types
def triangle(x):
    if x<=-1 or x>=1:
        y = 0
    else:
        y = 1-abs(x)
    return y

def lopsided(x):
    if x<=-1 or x>=0.5:
        y = 0
    elif x >= 0:
        y = 2*(0.5-x)
    elif x<0:
        y = 1+x
    return y

def square(x):
    if x<=-1 or x>=1:
        y = 0
    else:
        y = 1
    return y

def sqsin(x):
    return (sin(x))**2

def sqtri(x):
    if x<-2:
        y = 0
    if x<0 and x>=-2:
        y = -1
    if x>=0 and x<2:
       y = -abs(-x+1)+1
    if x>=2:
        y = 0
    return y

#3d Scene
scene = display(title='Pulse',
     width=1024, height=300, x=0, y=300,
     center=(obsloc,0,0), background=(0,0,0))
scene.autoscale = 0
scene.userspin = 0
scene.range = (10,7,1)
obs = curve(pos=[(obsloc,1.5),(obsloc,-1.5)], color = color.yellow, radius=0.03)

#Graph Scene
graph1 = gdisplay(x=0, y=0, width=1024, height=300,
          title='Y-position vs. Time', xtitle='t', ytitle='y',
          xmax=tmax, xmin=0., ymax=1, ymin=-1,
          foreground=color.white, background=color.black)
graph = gcurve(color=color.white)
print dir(graph)

#Control functions
def togglego():
    if ss.go == 1:
        ss.go = 0
        ss.text = "Start"
    elif ss.go == 0:
        ss.go = 1
        ss.text = "Pause"

def wfcycle():
    if wf.text == "1/2 sin":
        wf.text = "triangle"
    elif wf.text == "triangle":
        wf.text = "square"
    elif wf.text == "square":
        wf.text = "lopsided"
    elif wf.text == "lopsided":
        wf.text = "sin"
    elif wf.text == "sin":
        wf.text = "sqsin"
    elif wf.text == "sqsin":
        wf.text = "sqtri"
    elif wf.text == "sqtri":
        wf.text = "1/2 sin"

def stop():
    stp.stp = 1

def autotoggle():
    if auto.text == "Auto":
        auto.text = "Manual"
        print "..."
    elif auto.text == "Manual":
        auto.text = "Auto"

#Control scene
c = controls(title='Controls',
     x=0, y=600, width=1024, height=150, range=50)
ss = button(pos=(-5,0), width=10, height=10,
              text='Start', action=lambda:togglego())
wf = button(pos=(-15,0), width=10, height=10,
              text='sin', action=lambda:wfcycle())
stp = button(pos=(5,0), width=10, height=10,
              text='Stop', action=lambda:stop())
auto = button(pos=(15,0), width=10, height=10,
              text='Auto', action=lambda:autotoggle())

#Main Loop:
while 1:
    ss.go = 0
    stp.stp = 0
    ss.text = "Start"
    c.interact()
    if ss.go == 1:
        t = 0
        try:
            newwave.render.visible = 0
            graph1.display.visible = 0
            del graph
        except:
            pass
        #New wave
        if wf.text == "1/2 sin":
            newwave = wave("sin",0,pi,0.01,(-7,0))
        else:
            newwave = wave(wf.text,-pi,pi,0.01,(-7,0))
        #Graph Scene
        graph1 = gdisplay(x=0, y=0, width=1024, height=300,
          title='Y-position vs. Time', xtitle='t', ytitle='y',
          xmax=tmax, xmin=0., ymax=1, ymin=-1,
          foreground=color.white, background=color.black)
        graph = gcurve(color=color.white)
        #Motion Loop
        while t<tmax:
            c.interact()
            if ss.go == 1:
                rate(framerate)
                t += dt
                newwave.pos = (newwave.pos[0]+speed*dt,newwave.pos[1])
                newwave.update()
                y = newwave.observe(obsloc)
                graph.plot(pos=(t,y))
            if auto.text == "Manual":
                ss.go = 0
                ss.text = "Start"
            if stp.stp == 1:
                t = tmax