#-*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
#
#        User modifable code
#
#Created on 22 июля 2011
#@author: keeper
# ----------------------------------------------------------------------------

#from objects import Ship

class DefaultShipController(object):  
    '''
    Standart ship controller
    ''' 
    def __init__(self,ship,inputstate):
        self.ship = ship
        self.state = inputstate
        
    def makestep(self):
        #set up engine thrusts
        if self.state.up: self.ship.gravity_engine.thrust = self.ship.gravity_engine.thrust+0.5
        if self.state.down : self.ship.gravity_engine.thrust = self.ship.gravity_engine.thrust-0.5
        if self.state.right: self.ship.nose_engine.thrust = self.ship.nose_engine.thrust+1
        else:   self.ship.nose_engine.thrust = 0
        if self.state.left:self.ship.back_engine.thrust = self.ship.back_engine.thrust+1
        else:   self.ship.back_engine.thrust = 0
        
class UIController(object):
    '''
    Standart User interface controller
    '''
    def __init__(self,inputstate):
        self.state = inputstate
        
class CameraController(object):
    # Default controller for camera linked to ship
    def __init__(self,camera,ship):
        self.camera = camera
        self.ship = ship
    def makestep(self):
        self.camera.lookAt = self.ship.position
        
        
class Controller(DefaultShipController):
    '''
    User-defined control class
    may be used to directly control ship or 
    to control some system that controls the ship or
    to control UI as user likes
    '''     
    pass


#FIXME: make default ships library
class Models(object):
    #here be custom ships
    def __init__(self):
        #self.shuttle_model = Ship()
        pass

    #   Ship params and other usefull data
    shuttle_model = {
                     'mass' : 100000,
                     'color':(0.0,1.0,0.0),
                     'dimensions' : (2.4, 0.45, 0.45),  
                     'max_thrust' : 1250004,                   
                     }
    proto_1a = {
                'mass':30000,
                'color':(0.0,0.0,0.5),
                'dimensions' : (0.4,0.7,0.7)}
    
        
models = Models()
