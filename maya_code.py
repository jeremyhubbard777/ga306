import maya.cmds as mc
import random
r = random.randint(5,10)
for cubes in range(r):
    new_sphere = mc.polySphere(r=random.randint(1,4))
    
    x = random.randint(-10,10)
    y = random.randint(-10,10)
    z = random.randint(-10,10)
    
    mc.setKeyframe(t=['0sec'],at='tx')
    mc.setKeyframe(t=['0sec'],at='ty')
    mc.setKeyframe(t=['0sec'],at='tz')
    mc.move(x,y,z,)
    mc.setKeyframe(t=['5sec'],at='tx')
    mc.setKeyframe(t=['5sec'],at='ty')
    mc.setKeyframe(t=['5sec'],at='tz')
        
    maya.cmds.polyColorPerVertex(
    colorRGB=[random.randint(0,1),random.randint(0,1),random.randint(0,1)],
    colorDisplayOption=True);

for cubes in range(r):
    mc.polyCube(d=random.randint(1,5),h=random.randint(1,5),w=random.randint(1,5))
    x = random.randint(-15,15)
    y = random.randint(-15,15)
    z = random.randint(-15,15)
    mc.setKeyframe(t=['0sec'],at='tx')
    mc.setKeyframe(t=['0sec'],at='ty')
    mc.setKeyframe(t=['0sec'],at='tz')
    mc.move(x,y,z,)
    mc.setKeyframe(t=['5sec'],at='tx')
    mc.setKeyframe(t=['5sec'],at='ty')
    mc.setKeyframe(t=['5sec'],at='tz')
    maya.cmds.polyColorPerVertex(
    colorRGB=[random.randint(0,1),random.randint(0,1),random.randint(0,1)],
    colorDisplayOption=True);