#-*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
#
#  Physics-related routines
#
#Created on 12 июля 2011
#@author: keeper
# ----------------------------------------------------------------------------
import ode

class ODEPhysicsWorld(object):
    # A list with ODE bodies
    bodies = []
    # The geoms for each of the bodies
    geoms = []
    # A joint group for the contact joints that are generated whenever
    # two bodies collide
    contactgroup = ode.JointGroup()
    
    # A joint list for static joints (walls, etc.)
    # no need to save joint that never change to object
    # but must be saved somewhere
    staticjoints = []
    
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
            c.setBounce(0.0)
            c.setMu(2000)
            j = ode.ContactJoint(world, contactgroup, c)
            j.attach(geom1.getBody(), geom2.getBody())
    
    def __init__(self,gravity_vec,erp,cfm):
        #create Dynamics world
        self.world = ode.World()
        self.world.setGravity(gravity_vec)
        self.world.setERP(erp)
        self.world.setCFM(cfm)
        #create Collision world
        self.space = ode.Space()
        # Create a plane geom which prevent the objects from falling forever
        self.floor = ode.GeomPlane(self.space, (0,1,0), 0)
        
    def makestep(self,dt):   
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
                    #body.setRotation((R[0], -1, 0, 1, R[4], 0, R[6], R[7], R[8]))
            
            
    def create_box_geom(self,box_dimensions):
        
        # Create a box geom for collision detection
        geom = ode.GeomBox(self.space, box_dimensions)
        return geom
    # create_box (temporary)
    def create_box(self, density,box_dimensions):
        """Create a box body and its corresponding geom."""
    
        # Create body
        lx, ly, lz = box_dimensions
        body = ode.Body(self.world)
        M = ode.Mass()
        M.setBox(density, lx, ly, lz)
        M.adjust(density)
        body.setMass(M)
    
        # Set parameters for drawing the body
        body.shape = "box"
        body.boxsize = (lx, ly, lz)
    
        # Create a box geom for collision detection
        geom = ode.GeomBox(self.space, lengths=body.boxsize)
        geom.setBody(body)
    
        return body, geom
    
    def set_fixed(self,body):
        # Make fixed join for the body
        joint = ode.FixedJoint(self.world)
        joint.attach(body, ode.environment)
        joint.setFixed()
        self.staticjoints.append(joint)