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
from multimedia import PygletApp
from graphics import GraphicsEngine

#some params
fps = 60

#Physics world params
gravity_vec = (0, -6, 0)
erp = 0.8
cfm = 1E-5

        
class GameWorld():
    # Static objects list
    statics = []
    
    # Interactive objects list
    interactives = []
    
    # Controllers
    controllers = []
    
    def mainloop(self,dt):
        if debug: print "GameWorld mainloop"
        
        # process controllers
        for controller in self.controllers:
            controller.makestep()
            
        # calculate movements (forces) for each interactive object
        for iObject in self.interactives:
            iObject.calculate()
            
        #make simulation step
        self.physics.makestep(dt)
        
    def __init__(self):
        if debug: print "Start GameWorld.init"
        #set up user controller state (keyboard and mouse)
        self.inputstate = app.window.inputstate
        
        #set and init physics engine (now only ODE) and create world
        self.physics = ODEPhysicsWorld(gravity_vec,erp,cfm)    
        #set physics simulation on intervals
        app.schedule(self.mainloop, 1.0/fps)
        
        #set and init graphix engine
        self.graphics = GraphicsEngine(app.window.width, app.window.height)
        
        #set Draw handler (will redraw on every event, scheduled or input)
        app.window.on_draw = self.graphics.makestep
        
        #set window resize handler
        app.window.on_resize = self.graphics.ReSizeGLScene
        
        if debug: print "End GameWorld.init"
        

        
##################################main
if __name__ == "__main__":         
    #set and init multimedia engine (now only Pyglet)
    app = PygletApp()
    #now we can init game world
    world = GameWorld()
    #set up scene
    from maps import LoadTestMap
    LoadTestMap(world)
    #start the game
    app.run()