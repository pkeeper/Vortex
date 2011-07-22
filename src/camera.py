#-*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
#
#        
#
#Created on 22 июля 2011
#@author: keeper
# ----------------------------------------------------------------------------


import math
import pyglet
from pyglet.gl import *


class Obj3D:
    ''' 
    Base class for objects with dynamics
    '''

    def __init__(self):
        self.pos=[0,0,0]        # en m
        self.vel=[0,0,0]        # en m/s
        self.accel=[0,0,0]      # en m/s**2
        self.m=1                # en Kg
        
    def get_x(self):
        return self.pos[0]

    def set_x(self,nx):
        self.pos[0]=nx

    def get_y(self):
        return self.pos[1]

    def set_y(self,ny):
        self.pos[1]=ny

    def get_z(self):
        return self.pos[2]

    def set_z(self,nz):
        self.pos[2]=nz

    x=property(get_x,set_x)
    y=property(get_y,set_y)
    z=property(get_z,set_z)

class Camera(Obj3D):

    def __init__(self):
        Obj3D.__init__(self)
        
        self.ortho=True

        self.fov=6        
        self.lookAt=[0,0,0]
        self.upY=[0,0,1]
        
        self.persp_zlimits=[1,1500]
        
        self.ortho_limits=[[-30,30], [-30,30], [-30,30]]
                     
        self.zoom=10

    # angle in radians
    def orbitXY(self, angle):
        nx=self.x-self.lookAt[0]
        ny=self.y-self.lookAt[1]
        
        ro=math.sqrt(nx**2+ny**2)

        self.x=self.lookAt[0]+ro*math.cos(angle)
        self.y=self.lookAt[1]+ro*math.sin(angle)

    def orbitZ(self,angle):
        nx=self.x-self.lookAt[0]
        ny=self.y-self.lookAt[1]
        nz=self.z-self.lookAt[2]
        
        ro3=math.sqrt(nx**2+ny**2+nz**2)
        angleXY=math.atan2(ny,nx)
        
        self.x=self.lookAt[0]+ro3*math.cos(angleXY)*math.cos(angle)
        self.y=self.lookAt[1]+ro3*math.sin(angleXY)*math.cos(angle)
        self.z=self.lookAt[1]+ro3*math.sin(angle)

    def orbit(self,angle_xy,angle_z):
        nx=self.x-self.lookAt[0]
        ny=self.y-self.lookAt[1]
        nz=self.z-self.lookAt[2]
        
        ro3=math.sqrt(nx**2+ny**2+nz**2)
        
        self.x=self.lookAt[0]+ro3*math.cos(angle_xy)*math.cos(angle_z)
        self.y=self.lookAt[1]+ro3*math.sin(angle_xy)*math.cos(angle_z)
        self.z=self.lookAt[1]+ro3*math.sin(angle_z)


    def activate(self,width,height):
        if width>height:
            aspect=float(width)/float(height)
        else:
            aspect=float(height)/float(width)
    
        if self.ortho:
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()

            if width>height:
#                glOrtho(self.ortho_limits[0][0]*aspect, self.ortho_limits[0][1]*aspect, 
#                        self.ortho_limits[1][0], self.ortho_limits[1][1], 
#                        self.ortho_limits[2][0], self.ortho_limits[2][1])
                glOrtho(self.lookAt[0]-self.zoom,self.lookAt[0]+self.zoom,
                        self.lookAt[1]-self.zoom,self.lookAt[1]+self.zoom,
                        self.lookAt[2]-20,self.lookAt[2]+20)
            else:
                glOrtho(self.ortho_limits[0][0], self.ortho_limits[0][1], 
                        self.ortho_limits[1][0]*aspect, self.ortho_limits[1][1]*aspect, 
                        self.ortho_limits[2][0], self.ortho_limits[2][1])

            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()

        else:        
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            gluPerspective(self.fov*self.zoom, aspect, self.persp_zlimits[0], self.persp_zlimits[1])
            
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            gluLookAt(self.x,self.y,self.z, 
                      self.lookAt[0],self.lookAt[1],self.lookAt[2], 
                      self.upY[0],self.upY[1],self.upY[2])