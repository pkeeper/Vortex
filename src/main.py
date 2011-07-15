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
from graphics import prepareDraw

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
    interactives = []
    control = object
    
    def mainloop(self,dt):
        if debug: print "World mainloop"
        #calculate movements (forces) for each interactive object
        for iObject in self.interactives:
            iObject.calculate()
        #make simulation step
        self.physics.simulate(dt)
        
    def draw(self):
        #relocate it to graphics module
        if debug: print "World Event: On Draw"
        
        prepareDraw()
        
        for Object in self.interactives:
            Object.draw_body()
        for Object in self.statics:
            Object.draw_body()

    def init(self):
        if debug: print "Start Main.init"
        
        #set and init physics engine (now only ODE) and create world
        self.physics = ODEPhysicsWorld(gravity_vec,erp,cfm)    
        #set physics simulation on intervals
        app.schedule(self.mainloop, 1.0/fps)
        
        #set Draw handler (will redraw on every event, scheduled or input)
        app.window.on_draw = self.draw
        
        if debug: print "End Main.init"
        

        
world = GameWorld()

def LoadTestMap():
    #=========================================
    #Load map or smth like that
    #=========================================
    if debug: print "Start Main.LoadTestMap"
    global world
    world.ship = Ship(world.physics, (1000, 0.4, 0.7, 0.7), (0.0, 2.0, 0.0))
    world.control = controlClass(world.ship)
    
    world.statics.append(Ship(world.physics, (1000, 0.4, 0.7, 0.7), (0.2, 0.0, 0.0)))
    
    world.statics.append(Wall(world.physics, (99999, 0.5, 4, 1), (3.0, 2.0, 0.0)))
    #Left wall
    world.statics.append(Wall(world.physics, (99999, 0.5, 4, 1), (-3.0, 2.0, 0.0)))
    #Top Wall
    world.statics.append(Wall(world.physics, (9999, 8, 0.5, 1), (0.0, 4.25, 0.0)))
    if debug: print "End Main.LoadTestMap"

        
##################################main
if __name__ == "__main__":         
    #set and init multimedia engine (now only Pyglet)
    global app 
    app = PygletApp()
    #now we can init world
    world.init()
    #set up scene
    LoadTestMap()
    #start the game
    app.run(world)