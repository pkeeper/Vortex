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
from ships import Ship,  PhysicsBody
import ode
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

ship = Ship(world, (1000, 0.4, 0.7, 0.7), (0.0, 3.0, 0.0))
ship2 = Ship(world, (1000, 0.4, 0.7, 0.7), (0.2, 0.0, 0.0))

right_wall = PhysicsBody(world, (99999, 0.5, 4, 1), (3.0, 2.0, 0.0))
left_wall = PhysicsBody(world, (99999, 0.5, 4, 1), (-3.0, 2.0, 0.0))
top_wall = PhysicsBody(world, (9999, 8, 0.5, 1), (0.0, 4.0, 0.0))

# Fixed joints for the walls
wall_joints = ode.JointGroup()
right_wall_joint = ode.FixedJoint(world.world, wall_joints)
right_wall_joint.attach(right_wall.body, ode.environment)
right_wall_joint.setFixed()

left_wall_joint = ode.FixedJoint(world.world, wall_joints)
left_wall_joint.attach(left_wall.body, ode.environment)
left_wall_joint.setFixed()

top_wall_joint = ode.FixedJoint(world.world, wall_joints)
top_wall_joint.attach(top_wall.body, ode.environment)
top_wall_joint.setFixed()

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