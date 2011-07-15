#-*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
#
#        All graphics code here (OpenGL abstraction)
#
#Created on 15 июля 2011
#@author: keeper
# ----------------------------------------------------------------------------
from pyglet.gl import *
debug = True

def DrawBox(position,dimensions,rotation):
        """Draw simple box"""
        
        if debug: print "Body: Draw"
        x, y, z = position
        R = rotation
        #print R
        
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
        sx,sy,sz = dimensions
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

        glColor3f(0.0,1.0,0.0)            # Set The Color To green
        glVertex3f( 1.0, 1.0,-1.0)        # Top Right Of The Quad (Right)
        glVertex3f( 1.0, 1.0, 1.0)        # Top Left Of The Quad (Right)
        glVertex3f( 1.0,-1.0, 1.0)        # Bottom Left Of The Quad (Right)
        glVertex3f( 1.0,-1.0,-1.0)        # Bottom Right Of The Quad (Right)
        glEnd()                # Done Drawing The Quad
        glPopMatrix()
        #print self.body.getPosition()

class GraphicsEngine():
    static = []     #Static objects list 
    dynamic = []    #Objects that can change their position (not frequent)
    active = []     #Objects that can change their position every frame

    def makestep(self):
        #here goes the main draw loop
        
    #    glTranslatef(0, 0, -4)
    #    glRotatef(0, 0, 0, 1)
    #    glRotatef(0, 0, 1, 0)
    #    glRotatef(0, 1, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);    # Clear The Screen And The Depth Buffer
        glLoadIdentity();                    # Reset The View
        #glTranslatef(-1.5,0.0,-6.0)                # Move Left And Into The Screen
        
        #draw objects 
        for Object in self.active:
            DrawBox(Object.position,Object.dimensions,Object.rotation)
        for Object in self.static:
            DrawBox(Object.position,Object.dimensions,Object.rotation)