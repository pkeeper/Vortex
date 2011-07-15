#-*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
#
#        
#
#Created on 15 июля 2011
#@author: keeper
# ----------------------------------------------------------------------------
from pyglet.gl import *

def prepareDraw():
    
#    glTranslatef(0, 0, -4)
#    glRotatef(0, 0, 0, 1)
#    glRotatef(0, 0, 1, 0)
#    glRotatef(0, 1, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);    # Clear The Screen And The Depth Buffer
    glLoadIdentity();                    # Reset The View
    #glTranslatef(-1.5,0.0,-6.0)                # Move Left And Into The Screen