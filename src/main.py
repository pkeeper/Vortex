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
from objects import Ship, Wall
from multimedia import PygletApp
from graphics import GraphicsEngine

#some params
fps = 60

#Physics world params
gravity_vec = (0, -9.81, 0)
erp = 0.8
cfm = 1E-5

class DefaultController():
    '''
    User-defined control class
    may be used to directly control ship or 
    to control some system that controls the ship or
    to control UI as user likes
    '''
    def __init__(self,ship,controller):
        self.ship = ship
        self.state = controller
        
    def makestep(self):
        self.ship.upthrust  =   self.state.up
        self.ship.downthrust=   self.state.down
        self.ship.leftthrust=   self.state.left
        self.ship.rightthrust=  self.state.right

class GameWorld():
    # Static objects list
    statics = []
    
    # Interactive objects list
    interactives = []
    control = object
    
    def mainloop(self,dt):
        if debug: print "World mainloop"
        
        self.control.makestep()
        #calculate movements (forces) for each interactive object
        for iObject in self.interactives:
            iObject.calculate()
        #make simulation step
        self.physics.makestep(dt)
        
    def __init__(self):
        if debug: print "Start Main.init"
        
        #set and init physics engine (now only ODE) and create world
        self.physics = ODEPhysicsWorld(gravity_vec,erp,cfm)    
        #set physics simulation on intervals
        app.schedule(self.mainloop, 1.0/fps)
        
        #set and init graphix engine
        self.graphics = GraphicsEngine()
        
        #set Draw handler (will redraw on every event, scheduled or input)
        app.window.on_draw = self.graphics.makestep
        
        if debug: print "End Main.init"
        

def LoadTestMap():
    #=========================================
    #Load map or smth like that
    #=========================================
    if debug: print "Start Main.LoadTestMap"
    global world
    world.ship = Ship(world.physics, world.graphics, 100, (0.4, 0.7, 0.7), (-2.0, 0.1, 0.0))
    world.interactives.append(world.ship)
    
    #set up default controller
    world.control = DefaultController(world.ship,app.window.controller)
    
    world.interactives.append(Ship(world.physics, world.graphics, 1000, (0.4, 0.7, 0.7), (1.2, 2, 0.0)))
    
    world.statics.append(Wall(world.physics, world.graphics, 1, (0.5, 4, 2), (3.0, 2.0, 0.0)))
    #Left wall
    world.statics.append(Wall(world.physics, world.graphics, 1, (0.5, 4, 2), (-3.0, 2.0, 0.0)))
    #Top Wall
    world.statics.append(Wall(world.physics, world.graphics, 1, (8, 0.5, 2), (0.0, 4.3, 0.0)))
    if debug: print "End Main.LoadTestMap"

        
##################################main
if __name__ == "__main__":         
    #set and init multimedia engine (now only Pyglet)
    app = PygletApp()
    #now we can init game world
    world = GameWorld()
    #set up scene
    LoadTestMap()
    #start the game
    app.run(world)