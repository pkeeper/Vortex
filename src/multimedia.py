#-*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
#
#    Multimedia Library abstractions and routines
#
#Created on 13 июля 2011
#@author: keeper
# ----------------------------------------------------------------------------
import pyglet
from pyglet.window import key
debug = True


class InputStateClass():
    '''
    Basic controller state class
    '''    
    up = False
    down = False
    left = False
    right = False
        
  

##################################Window setup
class pygwindow(pyglet.window.Window):
    inputstate = InputStateClass()
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self):
        from pyglet.gl import Config
        config = Config(sample_buffers=1, samples=4,
                    depth_size=16, double_buffer=True,)
        try:
            super(pygwindow, self).__init__(resizable=True, config=config)
        except:
            super(pygwindow, self).__init__(resizable=True)

        self.width = 640
        self.height = 480
                  
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
        pass

 
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            self.dispatch_event('on_close')
        elif symbol == key.RIGHT:
            self.inputstate.right = True
        elif symbol == key.LEFT:
            self.inputstate.left = True
        elif symbol == key.UP:
            self.inputstate.up =True
        elif symbol == key.DOWN:
            self.inputstate.down = True
            
    def on_key_release(self,symbol, modifiers):
        if symbol == key.RIGHT:
            self.inputstate.right = False
        elif symbol == key.LEFT:
            self.inputstate.left = False
        elif symbol == key.UP:
            self.inputstate.up = False
        elif symbol == key.DOWN:
            self.inputstate.down = False

   
class PygletApp():    
    '''Unified interface to application through PyGlet
    other libs will import and use only object of this class 
    or class to other library with same interface
    '''
     
    
    def schedule(self,func,dt):
        pyglet.clock.schedule_interval(func,dt)
        
    def __init__(self):
        self.window = pygwindow()
        
    def run(self):    
        pyglet.app.run()
