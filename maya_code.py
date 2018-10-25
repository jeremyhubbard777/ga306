import maya.cmds as mc
import random
r = random.randint(10,15)
for spheres in range(r):
    new_sphere = mc.polySphere(r=random.randint(1,4))
    
    x = random.randint(-10,10)
    y = random.randint(-10,10)
    z = random.randint(-10,10)
    
    mc.setKeyframe(t=['0sec'])
    mc.move(x,y,z,)
    mc.setKeyframe(t=['2sec'])
    maya.cmds.polyColorPerVertex(
    colorRGB=[random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)],
    colorDisplayOption=True);
    
    x = random.randint(-10,10)
    y = random.randint(-10,10)
    z = random.randint(-10,10)
    mc.move(x,y,z,)
    mc.setKeyframe(t=['5sec'])
mc.select(all = True)
mc.group(n = 'spheres')
mc.setKeyframe(t=['5sec'])
mc.rotate(0,'180deg',0,'spheres',r=True,os=True,fo=True)
mc.setKeyframe(t=['7sec'])
mc.rotate('180deg',0,0,'spheres',r=True,os=True,fo=True)
mc.setKeyframe(t=['10sec'])
mc.group(em=True,n='cubes')
for c in range(r):
    cubes = mc.polyCube(d=random.randint(1,5),h=random.randint(1,5),w=random.randint(1,5))
   
    x = random.randint(-10,10)
    y = random.randint(-10,10)
    z = random.randint(-10,10)
    mc.setKeyframe(t=['0sec'])
    mc.move(x,y,z,)
    mc.setKeyframe(t=['10sec'])
    maya.cmds.polyColorPerVertex(
    colorRGB=[random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)],
    colorDisplayOption=True);
    mc.parent(cubes,'cubes')