#-*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
#
#  Main file of Vortex game
#
#Created on 12 июля 2011
#@author: keeper
# ----------------------------------------------------------------------------
debug = True

from phisics import ODEPhysicsWorld
from ships import Ship, Wall
from multimedia import MultimediaInit, Run, schedule

#some params
fps = 60

#Physics world params
gravity_vec = (0, -9.81, 0)
erp = 0.8
cfm = 1E-5

class controlClass():
    '''
    User-defined control class
    may be used to directly control ship or 
    to control some system that controls the ship or
    to control UI as user likes
    '''
    def __init__(self,object):
        self.ship = object
    
    def up(self,set):
        self.ship.upthrust=set
    def down(self,set):
        self.ship.downthrust=set
    def left(self,set):
        self.ship.leftthrust=set
    def right(self,set):
        self.ship.rightthrust=set

class GameWorld():
    statics = []
    ship = object
    control = object
        
world = GameWorld()

def init():
    if debug: print "Start Main.init"
    #init multimedia engine
    MultimediaInit()
    
    #set physics engine and create world
    global pWorld
    pWorld = ODEPhysicsWorld(gravity_vec,erp,cfm)    
    #set physics simulation on intervals
    schedule(pWorld.simulate, 1.0/fps)
    if debug: print "End Main.LoadTestMap"


def LoadTestMap():
    #=========================================
    #Load map or smth like that
    #=========================================
    if debug: print "Start Main.LoadTestMap"
    global world
    world.ship = Ship(pWorld, (1000, 0.4, 0.7, 0.7), (0.0, 3.0, 0.0))
    world.control = controlClass(world.ship)
    #тоже ship2 = Ship(world, (1000, 0.4, 0.7, 0.7), (0.2, 0.0, 0.0))
    
    world.statics.append(Wall(pWorld, (99999, 0.5, 4, 1), (3.0, 2.0, 0.0)))
    #Left wall
    world.statics.append(Wall(pWorld, (99999, 0.5, 4, 1), (-3.0, 2.0, 0.0)))
    #Top Wall
    world.statics.append(Wall(pWorld, (9999, 8, 0.5, 1), (0.0, 4.25, 0.0)))
    if debug: print "End Main.LoadTestMap"

        
##################################main
if __name__ == "__main__":
    init()
    LoadTestMap()
    Run(world)