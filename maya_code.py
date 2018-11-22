#import statments 
import maya.cmds as mc
import random

#set a random amount of shapes to create
r = random.randint(10,15)

#the main loop for crating the spheres
for spheres in range(r):
    new_sphere = mc.polySphere(r=random.randint(1,4))
    #create a random x, y, and z coordinates
    x = random.randint(-10,10)
    y = random.randint(-10,10)
    z = random.randint(-10,10)
    #move and animate the spheres to a random location
    mc.setKeyframe(t=['0sec'])
    mc.move(x,y,z,)
    mc.setKeyframe(t=['2sec'])
    #change the spheres to a random color
    maya.cmds.polyColorPerVertex(
    colorRGB=[random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)],
    colorDisplayOption=True);
    #create a new random location to move the spheres
    x = random.randint(-10,10)
    y = random.randint(-10,10)
    z = random.randint(-10,10)
    #animate the movement
    mc.move(x,y,z,)
    mc.setKeyframe(t=['5sec'])

#group the spheres, rotate them, then animate the motion
mc.select(all = True)
mc.group(n = 'spheres')
mc.setKeyframe(t=['5sec'])
mc.rotate(0,'180deg',0,'spheres',r=True,os=True,fo=True)
mc.setKeyframe(t=['7sec'])
mc.rotate('180deg',0,0,'spheres',r=True,os=True,fo=True)
mc.setKeyframe(t=['10sec'])
mc.group(em=True,n='cubes')

#the main loop for creating the cubes
for c in range(r):
    cubes = mc.polyCube(d=random.randint(1,5),h=random.randint(1,5),w=random.randint(1,5))
    #create a random x, y, and z coordinates
    x = random.randint(-10,10)
    y = random.randint(-10,10)
    z = random.randint(-10,10)
    #move and animate the cubes to a random location
    mc.setKeyframe(t=['0sec'])
    mc.move(x,y,z,)
    mc.setKeyframe(t=['10sec'])
    #change the cubes to a random color
    maya.cmds.polyColorPerVertex(
    colorRGB=[random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)],
    colorDisplayOption=True);
    mc.parent(cubes,'cubes')