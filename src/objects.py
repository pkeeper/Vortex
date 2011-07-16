#-*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
#
#  Game object classes
#
#Created on 13 июля 2011
#@author: keeper
# ----------------------------------------------------------------------------

debug = True


#    Components
#-----------------
class Engine(object):
    max_thrust  =   400    #Not Zero
    min_thrust  =   0       #May be negative value
    current_force      =   10
    vector      =   (0.0,1.0,0.0)   #Default force vector
    
    @property
    def thrust(self):
        print "thrust get" 
        print self.current_force
        return self.current_force/(self.max_thrust/100.0)
    
    @thrust.setter
    def thrust(self,output):
        
        print "thrust set"
        if output > 100: output = 100
        elif output <0 : output = 0
        self.current_force = self.min_thrust + output*((self.max_thrust - self.min_thrust)/100.0)
        
    def applyForce(self):
        if debug : print self.current_force
        force_vec = map(lambda x:x*self.current_force, self.vector)
        self.body.addForce(force_vec)
    
    def __init__(self,body,vector=(0.0,1.0,0.0)):
        self.body = body
        self.vector = vector
        
class GravityEngine(Engine):
    pass
        

class SimpleObject(object):
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
        
        



#    Custom and composite objects
#--------------------------------------

class Wall(SimpleObject):
    
    def __init__(self, *args, **kwargs):
        SimpleObject.__init__(self, *args, **kwargs)
        # Make fixed join for the wall
        self.pWorld.set_fixed(self.body)
    def calculate(self):
        #set no rotation
        self.rotation = (0, -1, 0, 1, 0, 0, 0, 0, 1)

class Ship(SimpleObject):
      
    def __init__(self, *args, **kwargs):
        SimpleObject.__init__(self, *args, **kwargs)
        self.gravity_engine = Engine(self.body,(0.0,1.0,0.0))
        self.nose_engine = Engine(self.body,(1.0,0.0,0.0))
        self.back_engine = Engine(self.body,(-1.0,0.0,0.0))
        
    def calculate(self):
        #apply engine forces
        self.gravity_engine.applyForce()
        self.nose_engine.applyForce()
        self.back_engine.applyForce()
        
        #set no rotation
        self.rotation = (0, -1, 0, 1, 0, 0, 0, 0, 1)
        