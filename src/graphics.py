#-*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
#
#        All graphics code here (OpenGL abstraction)
#
#Created on 15 июля 2011
#@author: keeper
# ----------------------------------------------------------------------------
from pyglet.gl import *
debug = False


# Define a simple function to create ctypes arrays of floats:
def vec(*args):
    return (GLfloat * len(args))(*args)

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
    camerapos = (-1.5,0.0,-6.0)

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
            
            
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # A general OpenGL initialization function.  Sets all of the initial parameters.
    def __init__(self, Width, Height):                # We call this right after our OpenGL window is created.
        
        print glGetString(GL_VERSION)
        glClearColor(0.4,0.4,0.4,0)       # This Will Clear The Background Color To Black
        glClearDepth(1.0)                          # Enables Clearing Of The Depth Buffer
        glDepthFunc(GL_LESS)                      # The Type Of Depth Test To Do
        glEnable(GL_DEPTH_TEST)                    # Enables Depth Testing
        glShadeModel(GL_SMOOTH)                   # Enables Smooth Color Shading
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()                          # Reset The Projection Matrix
                                                        # Calculate The Aspect Ratio Of The Window
        # Light source
        glLightfv(GL_LIGHT0,GL_POSITION,vec(0,0,1,0))
        glLightfv(GL_LIGHT0,GL_DIFFUSE,vec(1,0,1,1))
        glLightfv(GL_LIGHT0,GL_SPECULAR,vec(1,1,1,1))
        glEnable(GL_LIGHT0)
        #(pyglet initializes the screen so we ignore this call)
        #gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # The function called when our window is resized (which shouldn't happen if you enable fullscreen)
    def ReSizeGLScene(self,Width, Height):
        if Height == 0:                              # Prevent A Divide By Zero If The Window Is Too Small
            Height = 1
        glViewport(0, 0, Width, Height)        # Reset The Current Viewport And Perspective Transformation
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(Width)/float(Height), 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)