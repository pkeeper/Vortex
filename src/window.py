#-*- coding: utf-8 -*-
'''
Created on 13 июля 2011

@author: keeper
'''
import pyglet
from pyglet.gl import *
from pyglet.window import key
from main import control,ship,ship2

# Define a simple function to create ctypes arrays of floats:
def vec(*args):
    return (GLfloat * len(args))(*args)

def draw():
    #window.clear()
#    glTranslatef(0, 0, -4)
#    glRotatef(0, 0, 0, 1)
#    glRotatef(0, 0, 1, 0)
#    glRotatef(0, 1, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);    # Clear The Screen And The Depth Buffer
    glLoadIdentity();                    # Reset The View
    #glTranslatef(-1.5,0.0,-6.0)                # Move Left And Into The Screen
    #image.blit(ship.dx, ship.dy)
    ship.calculate()
    ship.draw_body()
    ship2.draw_body()
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
        elif symbol == key.RIGHT:
            control.right(True)
        elif symbol == key.LEFT:
            control.left(True)
        elif symbol == key.UP:
            control.up(True)
        elif symbol == key.DOWN:
            control.down(True)
            
    def on_key_release(self,symbol, modifiers):
        if symbol == key.RIGHT:
            control.right(False)
        elif symbol == key.LEFT:
            control.left(False)
        elif symbol == key.UP:
            control.up(False)
        elif symbol == key.DOWN:
            control.down(False)

    