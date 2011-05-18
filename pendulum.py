tickrate = 13
ballsize = 0.07
speed = 1

#Modules
from visual import *
from math import *

#PHYSICS PARAMETERS
hinge = (0,0,0)
bpos = (1,-3,0)
g = vector(0,-9.8,0)
fac = 0.00001
g = g*fac

#Scene alignment
scene.center = (0,-1.5,0)
scene.fullscreen = 1
scene.scale = (0.4,0.4,0.4)
class framestop:
    def __init__(self,frames):
        self.frames = frames
        self.frame = 0
    def tick(self):
        self.frame += 1
        if self.frame == self.frames:
            self.frame = 0
            return 1
        return 0

#Cleanup
removal = []
init = 0

#Timeline control
while 1:
    if init == 0:
        #Visual objects
        ball = sphere(pos=(bpos),radius=ballsize)
        ball.L = vector(0,0,0)
        string = curve(pos=[ball.pos,hinge])
        init = 1
    if scene.mouse.clicked == 1:
        c = scene.mouse.getclick()
        init = 0
        removal.append(ball)
        removal.append(string)
        #Main loop
        vlist = []
        stopper = framestop(tickrate)
        while 1:
            rate(60)
            if ball.pos[0]<-1 or ball.pos[0]>1:
                print len(vlist)
                for e in vlist:
                    e.visible = 0
                vlist = []
            #if stopper.tick():
                #vlist.append(copy.copy(ball))
            r = ball.pos-hinge
            ball.L += cross(r,g)*speed
            ball.rotate(angle=(mag(ball.L)*speed), axis=ball.L,origin=hinge)
            string.pos=[ball.pos,hinge]
            if scene.mouse.clicked == 1:
                c = scene.mouse.getclick()
                for e in vlist:
                    e.visible = 0
                vlist = []
                for e in removal:
                    e.visible = 0
                break