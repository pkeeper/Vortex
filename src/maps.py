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


def LoadTestMap(world):
    #=========================================
    #Load map or smth like that
    #=========================================
    if debug: print "Start Main.LoadTestMap"
    from user import Controller, models
    
    world.ship = Ship(world.physics, world.graphics, models.shuttle_model['mass'],models.shuttle_model['dimensions'] , (-2.0, 1, 0.0))
    world.interactives.append(world.ship)
    
    #set up default user input controller
    world.controllers.append(Controller(world.ship,world.inputstate))
    
#    world.statics.append(SimpleObject(world.physics, world.graphics, 10, (0.4, 0.7, 0.7), (1.2, 2, 0.0)))
#    world.statics.append(SimpleObject(world.physics, world.graphics, 1, (3.0, 0.3, 0.7), (0.0, 2, 0.0)))
#    world.statics.append(SimpleObject(world.physics, world.graphics, 1, (1.4, 0.7, 0.7), (1.2, 2, 0.0)))
#    world.statics.append(SimpleObject(world.physics, world.graphics, 1, (0.4, 2.0, 0.7), (1.2, 2, 0.0)))
#    
    world.statics.append(Wall(world.physics, world.graphics, 0, (0.5, 4, 2), (3.0, 2.0, 0.0)))
    #Left wall
    world.statics.append(Wall(world.physics, world.graphics, 0, (0.5, 4, 2), (-3.0, 2.0, 0.0)))
    #Top Wall
    world.statics.append(Wall(world.physics, world.graphics, 0, (8, 0.5, 2), (0.0, 4.3, 0.0)))
    if debug: print "End Main.LoadTestMap"