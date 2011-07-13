#-*- coding: utf-8 -*-
'''
Created on 13 июля 2011

@author: keeper
'''
from pyglet.gl import *
import ode

class PhysicsBody(object):
    """Abstract class for all physics bodies.
    """
    
    def __init__(self, world, box_params, position):
        self.position = position
        self.world = world
        self.box_params = box_params
        self.body, self.geom = world.create_box(box_params)
        self.body.setPosition(position)
        world.bodies.append(self.body)
        world.geoms.append(self.geom)

    def draw_body(self):
        """Draw an ODE body."""
        x, y, z = self.body.getPosition()
        R = self.body.getRotation()
        print R
        #set no rotation
        self.body.setRotation((0, -1, 0, 1, 0, 0, 0, 0, 1))
        rot = (GLdouble * 16)(R[0], R[3], R[6], 0.,
               R[1], R[4], R[7], 0.,
               R[2], R[5], R[8], 0.,
               x, y, z, 0.4)
        #rot_gl = (GLfloat * len(rot))(*rot)
        glPushMatrix()
#        if self.body.shape=="box":
#            sx,sy,sz = self.body.boxsize
#            glScalef(sx, sy, sz)
#            glutSolidCube(60)
#            glColor3f(0.3, 0.5, 1.0)
#            glBegin(GL_QUADS)                   # Start drawing a 4 sided polygon
#            glVertex3f(-1.0, 1.0, 0.0)          # Top Left
#            glVertex3f(1.0, 1.0, 0.0)           # Top Right
#            glVertex3f(1.0, -1.0, 0.0)          # Bottom Right
#            glVertex3f(-1.0, -1.0, 0.0)         # Bottom Left
#            glEnd()                             # We are done with the polygon
#        
        #glLoadIdentity()
        glTranslatef(0.0,-2.0,-20.0)        # Move  Screen
        #glRotatef(0.1,1.0,1.0,1.0)        # Rotate The Cube On X, Y & Z
        
        glMultMatrixd(rot)
        sx,sy,sz = self.body.boxsize
        glScalef(sx/2, sy/2, sz/2)
        glBegin(GL_QUADS)            # Start Drawing The Cube

        glColor3f(0.0,1.0,0.0)            # Set The Color To Blue
        glVertex3f( 1.0, 1.0,-1.0)        # Top Right Of The Quad (Top)
        glVertex3f(-1.0, 1.0,-1.0)        # Top Left Of The Quad (Top)
        glVertex3f(-1.0, 1.0, 1.0)        # Bottom Left Of The Quad (Top)
        glVertex3f( 1.0, 1.0, 1.0)        # Bottom Right Of The Quad (Top)

        glColor3f(1.0,0.5,0.0)            # Set The Color To Orange
        glVertex3f( 1.0,-1.0, 1.0)        # Top Right Of The Quad (Bottom)
        glVertex3f(-1.0,-1.0, 1.0)        # Top Left Of The Quad (Bottom)
        glVertex3f(-1.0,-1.0,-1.0)        # Bottom Left Of The Quad (Bottom)
        glVertex3f( 1.0,-1.0,-1.0)        # Bottom Right Of The Quad (Bottom)

        glColor3f(1.0,0.0,0.0)            # Set The Color To Red
        glVertex3f( 1.0, 1.0, 1.0)        # Top Right Of The Quad (Front)
        glVertex3f(-1.0, 1.0, 1.0)        # Top Left Of The Quad (Front)
        glVertex3f(-1.0,-1.0, 1.0)        # Bottom Left Of The Quad (Front)
        glVertex3f( 1.0,-1.0, 1.0)        # Bottom Right Of The Quad (Front)

        glColor3f(1.0,1.0,0.0)            # Set The Color To Yellow
        glVertex3f( 1.0,-1.0,-1.0)        # Bottom Left Of The Quad (Back)
        glVertex3f(-1.0,-1.0,-1.0)        # Bottom Right Of The Quad (Back)
        glVertex3f(-1.0, 1.0,-1.0)        # Top Right Of The Quad (Back)
        glVertex3f( 1.0, 1.0,-1.0)        # Top Left Of The Quad (Back)

        glColor3f(0.0,0.0,1.0)            # Set The Color To Blue
        glVertex3f(-1.0, 1.0, 1.0)        # Top Right Of The Quad (Left)
        glVertex3f(-1.0, 1.0,-1.0)        # Top Left Of The Quad (Left)
        glVertex3f(-1.0,-1.0,-1.0)        # Bottom Left Of The Quad (Left)
        glVertex3f(-1.0,-1.0, 1.0)        # Bottom Right Of The Quad (Left)

        glColor3f(1.0,0.0,1.0)            # Set The Color To Violet
        glVertex3f( 1.0, 1.0,-1.0)        # Top Right Of The Quad (Right)
        glVertex3f( 1.0, 1.0, 1.0)        # Top Left Of The Quad (Right)
        glVertex3f( 1.0,-1.0, 1.0)        # Bottom Left Of The Quad (Right)
        glVertex3f( 1.0,-1.0,-1.0)        # Bottom Right Of The Quad (Right)
        glEnd()                # Done Drawing The Quad
        glPopMatrix()
        #print self.body.getPosition()

class Wall(PhysicsBody):
    
    def __init__(self, *args, **kwargs):
        PhysicsBody.__init__(self, *args, **kwargs)
        # Make fixed join for the wall
        self.joint = ode.FixedJoint(self.world.world)
        self.joint.attach(self.body, ode.environment)
        self.joint.setFixed()
    
    def draw_body(self):
        """Draw an ODE body."""
        
        # Wall must always stay in static position
        x, y, z = self.position
        R = self.body.getRotation()
        rot = (GLdouble * 16)(R[0], R[3], R[6], 0.,
               R[1], R[4], R[7], 0.,
               R[2], R[5], R[8], 0.,
               x, y, z, 0.4)
        #rot_gl = (GLfloat * len(rot))(*rot)
        glPushMatrix()
#        if self.body.shape=="box":
#            sx,sy,sz = self.body.boxsize
#            glScalef(sx, sy, sz)
#            glutSolidCube(60)
#            glColor3f(0.3, 0.5, 1.0)
#            glBegin(GL_QUADS)                   # Start drawing a 4 sided polygon
#            glVertex3f(-1.0, 1.0, 0.0)          # Top Left
#            glVertex3f(1.0, 1.0, 0.0)           # Top Right
#            glVertex3f(1.0, -1.0, 0.0)          # Bottom Right
#            glVertex3f(-1.0, -1.0, 0.0)         # Bottom Left
#            glEnd()                             # We are done with the polygon
#        
        #glLoadIdentity()
        glTranslatef(0.0,-2.0,-20.0)        # Move  Screen
        #glRotatef(0.1,1.0,1.0,1.0)        # Rotate The Cube On X, Y & Z
        
        glMultMatrixd(rot)
        sx,sy,sz = self.body.boxsize
        glScalef(sx/2, sy/2, sz/2)
        glBegin(GL_QUADS)            # Start Drawing The Cube

        glColor3f(0.0,1.0,0.0)            # Set The Color To Blue
        glVertex3f( 1.0, 1.0,-1.0)        # Top Right Of The Quad (Top)
        glVertex3f(-1.0, 1.0,-1.0)        # Top Left Of The Quad (Top)
        glVertex3f(-1.0, 1.0, 1.0)        # Bottom Left Of The Quad (Top)
        glVertex3f( 1.0, 1.0, 1.0)        # Bottom Right Of The Quad (Top)

        glColor3f(1.0,0.5,0.0)            # Set The Color To Orange
        glVertex3f( 1.0,-1.0, 1.0)        # Top Right Of The Quad (Bottom)
        glVertex3f(-1.0,-1.0, 1.0)        # Top Left Of The Quad (Bottom)
        glVertex3f(-1.0,-1.0,-1.0)        # Bottom Left Of The Quad (Bottom)
        glVertex3f( 1.0,-1.0,-1.0)        # Bottom Right Of The Quad (Bottom)

        glColor3f(1.0,0.0,0.0)            # Set The Color To Red
        glVertex3f( 1.0, 1.0, 1.0)        # Top Right Of The Quad (Front)
        glVertex3f(-1.0, 1.0, 1.0)        # Top Left Of The Quad (Front)
        glVertex3f(-1.0,-1.0, 1.0)        # Bottom Left Of The Quad (Front)
        glVertex3f( 1.0,-1.0, 1.0)        # Bottom Right Of The Quad (Front)

        glColor3f(1.0,1.0,0.0)            # Set The Color To Yellow
        glVertex3f( 1.0,-1.0,-1.0)        # Bottom Left Of The Quad (Back)
        glVertex3f(-1.0,-1.0,-1.0)        # Bottom Right Of The Quad (Back)
        glVertex3f(-1.0, 1.0,-1.0)        # Top Right Of The Quad (Back)
        glVertex3f( 1.0, 1.0,-1.0)        # Top Left Of The Quad (Back)

        glColor3f(0.0,0.0,1.0)            # Set The Color To Blue
        glVertex3f(-1.0, 1.0, 1.0)        # Top Right Of The Quad (Left)
        glVertex3f(-1.0, 1.0,-1.0)        # Top Left Of The Quad (Left)
        glVertex3f(-1.0,-1.0,-1.0)        # Bottom Left Of The Quad (Left)
        glVertex3f(-1.0,-1.0, 1.0)        # Bottom Right Of The Quad (Left)

        glColor3f(1.0,0.0,1.0)            # Set The Color To Violet
        glVertex3f( 1.0, 1.0,-1.0)        # Top Right Of The Quad (Right)
        glVertex3f( 1.0, 1.0, 1.0)        # Top Left Of The Quad (Right)
        glVertex3f( 1.0,-1.0, 1.0)        # Bottom Left Of The Quad (Right)
        glVertex3f( 1.0,-1.0,-1.0)        # Bottom Right Of The Quad (Right)
        glEnd()                # Done Drawing The Quad
        glPopMatrix()
        #print self.body.getPosition()

class Ship(PhysicsBody):
  
    uptrust = False
    downtrust = False
    lefttrust = False
    righttrust = False
    
#    def __init__(self, *args, **kwargs):
#        PhysicsBody.__init__(self, *args, **kwargs)
#        self.type = 'ship'
        
    def calculate(self):
        if self.uptrust: self.body.addForce((0,1900,0))
        if self.lefttrust: self.body.addForce((-300,0,0))
        if self.righttrust: self.body.addForce((100,0,0))
        R = self.body.getRotation()
        self.body.setRotation((R[0], R[1], 0, R[3], 0, 0,R[6], R[7], R[8]))
        