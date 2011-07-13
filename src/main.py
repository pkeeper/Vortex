#-*- coding: utf-8 -*-
'''
Created on 12 июля 2011

@author: keeper
'''
import pyglet
from pyglet.gl import *
#from OpenGL.GLUT import glutInit,glutSolidCube
from math import *
from phisics import protoworld
from ships import shipClass
#import ctypes
#import sys, time 

   
#Init batch for fast render
batch = pyglet.graphics.Batch()

label = pyglet.text.Label('Hello, world', 
                          font_name='Times New Roman', 
                          font_size=24,
                          x=320, y=240,
                          anchor_x='center', anchor_y='center')


world = protoworld()
world.create()

fps = 60
fps_display = pyglet.clock.ClockDisplay()
pyglet.clock.schedule_interval(world.simulate, 1.0/fps)

ship = shipClass(world)

ship2 = shipClass(world)
ship2.body.setPosition((0.2,0.0,0.0))

class controlClass():
    '''
    User-defined control class
    may be used to directly control ship or 
    to control some system that controls the ship or
    to control UI as user likes
    '''
    
    def up(self,set):
        ship.uptrust=set
    def down(self,set):
        ship.downrust=set
    def left(self,set):
        ship.lefttrust=set
    def right(self,set):
        ship.righttrust=set

control = controlClass()

        



##################################main
if __name__ == "__main__":
    from window import pygwindow
    window = pygwindow()
    pyglet.app.run()