#-*- coding: utf-8 -*-
#Created on 10 июля 2011
#
#@author: keeper

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
vec4 = GLfloat_4

rotx = roty = rotz=0.0
posx = posy = posz = 0.0
mainship = gear2 = gear3 = 0
angle = 0.0

def ship(color):
    glShadeModel(GL_FLAT) 
    
    #Draw front
#    glNormal3f(0.0, 0.0, 1.0)
#    glBegin(GL_QUAD_STRIP)
#    glVertex3f(-1.0,1.0,0.0)
#    glVertex3f(1.0,1.0,0.0)
#    glVertex3f(-1.0,-1.0,0.0)
#    glVertex3f(1.0,-1.0,0.0)
#    glVertex3f(1.0,1.0,-1.0)
#    glVertex3f(1.0,1.0,-1.0)
#    glEnd()
        # Draw a square (quadrilateral) rotated on the X axis.
    global rotz
    glRotatef(rotz, 0.0, 0.0, 1.0)        # Rotate 
    #glColor3f(0.3, 0.5, 1.0)            # Bluish shade
    glBegin(GL_QUADS)                   # Start drawing a 4 sided polygon
    glVertex3f(-1.0, 1.0, 0.0)          # Top Left
    glVertex3f(1.0, 1.0, 0.0)           # Top Right
    glVertex3f(1.0, -1.0, 0.0)          # Bottom Right
    glVertex3f(-1.0, -1.0, 0.0)         # Bottom Left
    glEnd()                             # We are done with the polygon


def InitGL(Width,Height):
    glClearColor(0.0,0.0,0.0,0.0) #Make screen black
    glClearDepth(1.0)               #Set depth
    glDepthFunc(GL_LESS)            
    glEnable(GL_DEPTH_TEST)
    
    #Light
    pos = vec4(5.0, 5.0, 10.0, 0.0)
    #glLightfv(GL_LIGHT0, GL_POSITION, pos)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    
    #material
    glEnable(GL_COLOR_MATERIAL)
    
    #displaying parameters
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 1000.0)
    glMatrixMode(GL_MODELVIEW)
    
    #render ship and other code
    global mainship
    red = vec4(0.8, 0.1, 0.0, 1.0)
    green = vec4(0.0, 0.8, 0.2, 1.0)
    blue = vec4(0.2, 0.2, 1.0, 1.0)
    
#    mainship = glGenLists(1)
#    glNewList(mainship, GL_COMPILE)
#    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, red)
#    ship(1)
#    glEndList()
    
    glEnable(GL_NORMALIZE)
    

def ReSizeGLScene(Width, Height):
    if Height == 0: Height = 1
    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    
def DrawGLScene():
    global rotation, posy
    #rotation = (rotation + 1) % 360 #increase angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # очищаем экран
    glLoadIdentity()  # восстанавливаем мировые координаты
    glTranslatef(0.0,posy,-10.0)
    #glRotatef(rotation,1.0,0.0,0.0)
    #glRotatef(rotation,0.0,1.0,0.0)
    #glRotatef(rotation,0.0,0.0,1.0)
    #glColor4f(0.0,0.7,0.1,1)
    #glutSolidCube(3)
    #glCallList(ship)
    global rotz
    glRotatef(rotz, 0.0, 0.0, 1.0)        # Rotate 
    glColor3f(0.3, 0.5, 1.0)            # Bluish shade
    glBegin(GL_QUADS)                   # Start drawing a 4 sided polygon
    glVertex3f(-2.0, 1.0, 0.0)          # Top Left
    glVertex3f(2.0, 1.0, 0.0)           # Top Right
    glVertex3f(2.0, -1.0, 0.0)          # Bottom Right
    glVertex3f(-2.0, -1.0, 0.0)         # Bottom Left
    glEnd() 
    glutSwapBuffers()
    
def KeyPressed(*args):
    global rotx,roty,rotz
    #exit on escape utton
    if args[0]=="\033": sys.exit()
    elif args[0]=='a':rotz -= 0.1

# react to control cays
def special(k, x, y):
    global rotx,roty,rotz,posx,posy,posz
    
    if k == GLUT_KEY_UP:
        posy += 0.3
    elif k == GLUT_KEY_DOWN:
        posy -= 0.3
    elif k == GLUT_KEY_LEFT:
        rotz -= 0.3
    elif k == GLUT_KEY_RIGHT:
        rotz += 0.3
    else:
        return
    glutPostRedisplay()
    
def idle():
    global posx,posy,posz
    if posy > 0.0: posy -= 0.01
    glutPostRedisplay()
    
def visible(vis):
    #stop animation on window hide
    if vis == GLUT_VISIBLE:
        glutIdleFunc(idle)
    else:
        glutIdleFunc(None)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(400, 300)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("GL experiments by keeper")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutKeyboardFunc(KeyPressed)
    glutSpecialFunc(special)
    glutVisibilityFunc(visible)
    InitGL(400, 300)
    glutMainLoop()

main()