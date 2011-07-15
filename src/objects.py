#-*- coding: utf-8 -*-
'''
Created on 13 июля 2011

@author: keeper
'''
#import ode
debug = True

class PhysicsBody(object):
    """Abstract class for all physics bodies.
    """
             
    @property
    def position(self):
        return self.body.getPosition()
    @position.setter
    def position(self,Cordinats):
        self.body.setPosition(Cordinats)
        
    @property
    def rotation(self):
        return self.body.getRotation()
    @rotation.setter
    def rotation(self,RotMatrix):
        self.body.setRotation(RotMatrix)
        
    def __init__(self, PhysicsWorld, GraphicsEngine, density,dimensions, position):
        
        if debug: print "Init: Physics body object"
        
        #Add itself to given Physics world
        self.pWorld = PhysicsWorld
        self.body, self.geom = self.pWorld.create_box(density,dimensions)
        self.pWorld.bodies.append(self.body)
        self.pWorld.geoms.append(self.geom)
        
        #Add itself to graphix engine
        self.graphics = GraphicsEngine
        self.graphics.active.append(self)
        
        self.position = position
        self.dimensions = dimensions
        

class Wall(PhysicsBody):
    
    def __init__(self, *args, **kwargs):
        PhysicsBody.__init__(self, *args, **kwargs)
        # Make fixed join for the wall
        self.joint = self.pWorld.set_fixed(self.body)
    def calculate(self):
        #set no rotation
        self.rotation = (0, -1, 0, 1, 0, 0, 0, 0, 1)

class Ship(PhysicsBody):
  
    upthrust = False
    downthrust = False
    leftthrust = False
    rightthrust = False
    
#    def __init__(self, *args, **kwargs):
#        PhysicsBody.__init__(self, *args, **kwargs)
#        self.type = 'ship'
        
    def calculate(self):
        print self.position
        if self.upthrust: self.body.addForce((0,1900,0))
        if self.leftthrust: self.body.addForce((-300,0,0))
        if self.rightthrust: self.body.addForce((100,0,0))
        #set no rotation
        self.rotation = (0, -1, 0, 1, 0, 0, 0, 0, 1)
        