#-*- coding: utf-8 -*-
'''
Created on 12 июля 2011

@author: keeper
'''
import ode

class protoworld(object):
    # A list with ODE bodies
    bodies = []
    # The geoms for each of the bodies
    geoms = []
    # A joint group for the contact joints that are generated whenever
    # two bodies collide
    contactgroup = ode.JointGroup()
    
    flat = True     #try to prevent any Z-axis movement
    
    # Collision callback
    def near_callback(self,args, geom1, geom2):
        """Callback function for the collide() method.
    
        This function checks if the given geoms do collide and
        creates contact joints if they do.
        """
    
        # Check if the objects do collide
        contacts = ode.collide(geom1, geom2)
    
        # Create contact joints
        world, contactgroup = args
        for c in contacts:
            #c.setBounce(0.1)
            #c.setMu(5000)
            j = ode.ContactJoint(world, contactgroup, c)
            j.attach(geom1.getBody(), geom2.getBody())
    
    def create(self):
        #create Dynamics world
        self.world = ode.World()
        self.world.setGravity((0, -9.81, 0))
        self.world.setERP(0.8)
        self.world.setCFM(1E-5)
        #create Collision world
        self.space = ode.Space()
        # Create a plane geom which prevent the objects from falling forever
        self.floor = ode.GeomPlane(self.space, (0,1,0), 0)
        
    def simulate(self,dt):   
        # Simulate
        n = 2
    
        for i in range(n):
            # Detect collisions and create contact joints
            self.space.collide((self.world,self.contactgroup), self.near_callback)
    
            # Simulation step
            self.world.step(dt/n)
    
            # Remove all contact joints
            self.contactgroup.empty()
            if self.flat:
                for body in self.bodies:
                    x, y, z = body.getPosition()
                    body.setPosition((x, y, 0.0))
                    R = body.getRotation()
                    body.setRotation((R[0], R[1], 0, R[3], R[4], 0, R[6], R[7], R[8]))
            
            
    # create_box (temporary)
    def create_box(self, box_params):
        """Create a box body and its corresponding geom."""
    
        # Create body
        density, lx, ly, lz = box_params
        body = ode.Body(self.world)
        M = ode.Mass()
        M.setBox(density, lx, ly, lz)
        body.setMass(M)
    
        # Set parameters for drawing the body
        body.shape = "box"
        body.boxsize = (lx, ly, lz)
    
        # Create a box geom for collision detection
        geom = ode.GeomBox(self.space, lengths=body.boxsize)
        geom.setBody(body)
    
        return body, geom