#-*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
#
#        
#
#Created on 22 июля 2011
#@author: keeper
# ----------------------------------------------------------------------------
from objects import Ship, Wall,SimpleObject

debug = True

testmap1={'color':(0.0,0.5,0.0),
          'start_pos':(2.5,2,0),
          'geoms':(
                   ((2,20,2),(-1,10,0)),
                   ((20,2,2),(10,5,0)),
                   ((20.5,4.8,2),(17.5,8.5,0)),
                   ((4,0.7,2),(24,0.5,0)),
                   ((2,2,2),(28,5,0)),
                   
                   ((2,4,2),(36,2,0)),
                   ((5,2,2),(35.5,5,0)),
                   ((2,12,2),(38.7,10.8,0)),
                   ((4.9,2,2),(30.5,11,0)),
                   ((40,2,2),(20,18,0)),
                   
                   ((4,4,2),(2,15,0))),
          }

def LoadMapData(world,data):
    for box in data['geoms']:
        world.statics.append(Wall(world.physics, world.graphics, 0, box[0], box[1],data['color']))
    

def LoadTestMap(world):
    #=========================================
    #Load map or smth like that
    #=========================================
    if debug: print "Start Main.LoadTestMap"
    from user import Controller, CameraController, models
    
    world.ship = Ship(world.physics, world.graphics, 
                      models.proto_1a['mass'],models.proto_1a['dimensions'] , 
                      testmap1['start_pos'],models.proto_1a['color'])
    world.interactives.append(world.ship)
    
    from camera import Camera
    world.graphics.camera = Camera()
    #world.graphics.camera.ortho = False
        
    world.graphics.camera.x=0
    world.graphics.camera.y=-1
    world.graphics.camera.z=8
    #world.interactives.append(world.camera)
    world.controllers.append(CameraController(world.graphics.camera,world.ship))
    
    #set up default user input controller
    world.controllers.append(Controller(world.ship,world.inputstate))
    
#    world.statics.append(SimpleObject(world.physics, world.graphics, 10, (0.4, 0.7, 0.7), (1.2, 2, 0.0)))
#    world.statics.append(SimpleObject(world.physics, world.graphics, 1, (3.0, 0.3, 0.7), (0.0, 2, 0.0)))
#    world.statics.append(SimpleObject(world.physics, world.graphics, 1, (1.4, 0.7, 0.7), (1.2, 2, 0.0)))
#    world.statics.append(SimpleObject(world.physics, world.graphics, 1, (0.4, 2.0, 0.7), (1.2, 2, 0.0)))
#    
    LoadMapData(world, testmap1)
    if debug: print "End Main.LoadTestMap"