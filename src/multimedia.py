#-*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
#
#    Multimedia Library abstractions and routines
#
#Created on 13 июля 2011
#@author: keeper
# ----------------------------------------------------------------------------
import pyglet
from pyglet.gl import *
from pyglet.window import key
debug = True


# Define a simple function to create ctypes arrays of floats:
def vec(*args):
    return (GLfloat * len(args))(*args)

class DefaultController():
    '''
    Basic controller state class
    '''    
    up = False
    down = False
    left = False
    right = False
        
  

##################################Window setup
class pygwindow(pyglet.window.Window):
    controller = DefaultController()
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self):
        config = Config(sample_buffers=1, samples=4,
                    depth_size=16, double_buffer=True,)
        try:
            super(pygwindow, self).__init__(resizable=True, config=config)
        except:
            super(pygwindow, self).__init__(resizable=True)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def setup(self,world):
        self.width = 640
        self.height = 480
        self.world = world
        global rquad
        rquad = 0.0   #(was global)
        self.InitGL(self.width, self.height)
          
        #Init batch for fast render
        self.batch = pyglet.graphics.Batch()
        
        self.label = pyglet.text.Label('Hello, world', 
                                  font_name='Times New Roman', 
                                  font_size=24,
                                  x=320, y=240,
                                  anchor_x='center', anchor_y='center')
        self.fps_display = pyglet.clock.ClockDisplay()

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def on_draw(self):
        if debug: print "Event: On Draw"
        pass

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
            self.controller.right = True
        elif symbol == key.LEFT:
            self.controller.left = True
        elif symbol == key.UP:
            self.controller.up =True
        elif symbol == key.DOWN:
            self.controller.down = True
            
    def on_key_release(self,symbol, modifiers):
        if symbol == key.RIGHT:
            self.controller.right = False
        elif symbol == key.LEFT:
            self.controller.left = False
        elif symbol == key.UP:
            self.controller.up = False
        elif symbol == key.DOWN:
            self.controller.down = False

   
class PygletApp():    
    '''Unified interface to application through PyGlet
    other libs will import and use only object of this class 
    or class to other library with same interface
    '''
     
    
    def schedule(self,func,dt):
        pyglet.clock.schedule_interval(func,dt)
        
    def __init__(self):
        self.window = pygwindow()
        
    def run(self,world):    
        self.window.setup(world)
        pyglet.app.run()
