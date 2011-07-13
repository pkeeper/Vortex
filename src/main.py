#-*- coding: utf-8 -*-
'''
Created on 12 июля 2011

@author: keeper
'''
import pyglet
from pyglet.window import key
from pyglet.gl import *
from OpenGL.GLUT import glutInit,glutSolidCube
from math import *
from phisics import protoworld
#import ctypes
#import sys, time 

   
#Init batch for fast render
batch = pyglet.graphics.Batch()

label = pyglet.text.Label('Hello, world', 
                          font_name='Times New Roman', 
                          font_size=24,
                          x=320, y=240,
                          anchor_x='center', anchor_y='center')


# Define a simple function to create ctypes arrays of floats:
def vec(*args):
    return (GLfloat * len(args))(*args)


square = (-1,1,  1,1,  1,-1,  -1,-1)
square = map(lambda x:x*10+20, square)


image = pyglet.resource.image('images/proto-1a.png')

world = protoworld()
world.create()

fps = 60
fps_display = pyglet.clock.ClockDisplay()

pyglet.clock.schedule_interval(world.simulate, 1.0/fps)

class shipClass():
    dx = 340
    dy = 0
    width = 70
    height = 40    
    def movex(self,vect):
        self.dx += vect
        if self.dx < 0 : self.dx = 0
        if self.dx+self.width > window.width : 
            self.dx=window.width-self.width
    def movey(self,vect):
        self.dy += vect
        if self.dy < 0 : self.dy = 0
        if self.dy+self.height > window.height : 
            self.dy=window.height-self.height
    # draw_body
    def draw_body(self):
        """Draw an ODE body.        """    
        x,y,z = self.body.getPosition()
        R = self.body.getRotation()
        rot = (GLdouble * 16)(R[0], R[3], R[6], 0.,
               R[1], R[4], R[7], 0.,
               R[2], R[5], R[8], 0.,
               x, y, z, 1.0)
        #rot_gl = (GLfloat * len(rot))(*rot)
        #glPushMatrix()
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
#        glPopMatrix()
        glLoadIdentity()
        glTranslatef(0.0,-1.0,-10.0)        # Move Right And Into The Screen
        #glRotatef(0.1,1.0,1.0,1.0)        # Rotate The Cube On X, Y & Z
        
        glMultMatrixd(rot)
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
        print self.body.getPosition()
        
    def calculate(self):
        #self.vertex_list
        pass
    def __init__(self):
        self.body, self.geom = world.create_box(1000, 1.0,0.2,0.2)
        self.body.setPosition((0.0,3.0,0.0))
        world.bodies.append(self.body)
        world.geoms.append(self.geom)
#        self.vertex_list = batch.add(4,pyglet.gl.GL_QUADS,None,
#                         ('v2i', square),
#                         ('c3B', (0, 0, 255,0, 0, 0, 255, 0, 255,0, 0, 255,)))
            
ship = shipClass()


def on_key_press(symbol, modifiers):
    if symbol == key.RIGHT:
        ship.movex(10)
    elif symbol == key.LEFT:
        ship.movex(-10)
    elif symbol == key.UP:
        ship.movey(10)
    elif symbol == key.DOWN:
        ship.movey(-10)

def draw():
    #window.clear()
#    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#    glLoadIdentity()
#    glTranslatef(0, 0, -4)
#    glRotatef(0, 0, 0, 1)
#    glRotatef(0, 0, 1, 0)
#    glRotatef(0, 1, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);    # Clear The Screen And The Depth Buffer
    glLoadIdentity();                    # Reset The View
    #glTranslatef(-1.5,0.0,-6.0)                # Move Left And Into The Screen
    #image.blit(ship.dx, ship.dy)
    ship.draw_body()
    #batch.draw()
    #label.draw()
    #fps_display.draw()

##################################Window setup
class pygwindow(pyglet.window.Window):
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self):
        config = Config(sample_buffers=1, samples=4,
                    depth_size=16, double_buffer=True,)
        try:
            super(pygwindow, self).__init__(resizable=True, config=config)
        except:
            super(pygwindow, self).__init__(resizable=True)
        self.setup()

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def setup(self):
        self.width = 640
        self.height = 480
        global rquad
        rquad = 0.0   #(was global)
        self.InitGL(self.width, self.height)
        pyglet.clock.schedule_interval(self.update, 1/30.0) # update at 60Hz

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def update(self,dt):
        draw()

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def on_draw(self):
        draw()

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def on_resize(self,w,h):
        self.ReSizeGLScene(w,h)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # A general OpenGL initialization function.  Sets all of the initial parameters.
    def InitGL(self,Width, Height):                # We call this right after our OpenGL window is created.
        glClearColor(0.0, 0.0, 0.0, 0.0)       # This Will Clear The Background Color To Black
        glClearDepth(1.0)                          # Enables Clearing Of The Depth Buffer
        glDepthFunc(GL_LESS)                      # The Type Of Depth Test To Do
        glEnable(GL_DEPTH_TEST)                    # Enables Depth Testing
        glShadeModel(GL_SMOOTH)                   # Enables Smooth Color Shading
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()                          # Reset The Projection Matrix
                                                        # Calculate The Aspect Ratio Of The Window
        #(pyglet initializes the screen so we ignore this call)
        #gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
    def ReSizeGLScene(self,Width, Height):
        if Height == 0:                              # Prevent A Divide By Zero If The Window Is Too Small
            Height = 1
        glViewport(0, 0, Width, Height)        # Reset The Current Viewport And Perspective Transformation
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            self.dispatch_event('on_close')

    
    


##################################main
if __name__ == "__main__":
    window = pygwindow()
    pyglet.app.run()