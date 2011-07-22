#-*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
#
#  Game object classes
#
#Created on 13 июля 2011
#@author: keeper
# ----------------------------------------------------------------------------

debug = True
ZERO_ROTATION = (0, -1, 0, 1, 0, 0, 0, 0, 1)


#    Components
#-----------------
class Engine(object):
    # If engine is On FIXME: not implemented yet
    enabled = False
    
    @property
    def thrust(self):
        return (self.current_force - self.min_thrust)/((self.max_thrust-self.min_thrust)/100.0)
    
    @thrust.setter
    def thrust(self,output):
        if output > 100: output = 100
        elif output <0 : output = 0
        self.current_force = self.min_thrust + output*((self.max_thrust - self.min_thrust)/100.0)
        
    def applyForce(self):
        if debug : print self.current_force
        force_vec = map(lambda x:x*self.current_force, self.vector)
        self.body.addForce(force_vec)
    
    def __init__(self,body,vector=(0.0,1.0,0.0),max_thrust = 1,min_thrust = 0):
        self.body = body
        self.vector = vector
        self.max_thrust = max_thrust    #Not Zero
        self.min_thrust = min_thrust    #May be negative value
        self.current_force = 0
        
class GravityEngine(Engine):
    pass
        

class SimpleObject(object):
    """Abstract class for all physics bodies.
    """
             
    @property
    def position(self):
        if self.mass:
            return self.body.getPosition()
        else:
            return self.geom.getPosition()
        
    @position.setter
    def position(self,Cordinats):
        if self.mass:
            # Check if object hase phisics body with mass
            self.body.setPosition(Cordinats)
        else:
            self.geom.setPosition(Cordinats)
        
    @property
    def rotation(self):
        if self.mass:
            return self.body.getRotation()
        else:
            return self.geom.getRotation()
        
    @rotation.setter
    def rotation(self,RotMatrix):
        if self.mass:
            self.body.setRotation(RotMatrix)
        else:
            self.geom.setRotation(RotMatrix)
        
    def __init__(self, PhysicsWorld, GraphicsEngine, mass,dimensions, position):
        
        if debug: print "Init: Physics body object"
        
        #Add itself to given Physics world
        self.pWorld = PhysicsWorld
        if mass :
            # create body with mass
            self.body, self.geom = self.pWorld.create_box(mass,dimensions)
            self.pWorld.bodies.append(self.body)
        else:
            # create only a geom
            self.geom = self.pWorld.create_box_geom(dimensions)
            
        self.pWorld.geoms.append(self.geom)
        
        #Add itself to graphix engine
        self.graphics = GraphicsEngine
        self.graphics.active.append(self)
        
        self.mass = mass
        self.position = position
        self.dimensions = dimensions
        
        



#    Custom and composite objects
#--------------------------------------

class Wall(SimpleObject):

    def calculate(self):
        #set no rotation
        self.rotation = ZERO_ROTATION

class Ship(SimpleObject):
    #FIXME: refactor this 
    def __init__(self, *args, **kwargs):
        SimpleObject.__init__(self, *args, **kwargs)
        self.gravity_engine = Engine(self.body,(0.0,1.0,0.0),max_thrust = 1500000,min_thrust = 0)
        self.nose_engine = Engine(self.body,(1.0,0.0,0.0),max_thrust = 100000,min_thrust = 0)
        self.back_engine = Engine(self.body,(-1.0,0.0,0.0),max_thrust = 100000,min_thrust = 0)
        
    def calculate(self):
        #apply engine forces
        self.gravity_engine.applyForce()
        self.nose_engine.applyForce()
        self.back_engine.applyForce()
        
        #set no rotation
        self.rotation = ZERO_ROTATION
        