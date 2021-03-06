#
# Model a spiral galaxy   
#
# This code is derived (read shamelessly cribbed) from Heather Arneson's matlab
# 3D plot of a spiral galaxy
#

import sys, math, pygame, random

from star import star3D

def sign(x):
    if x < 0:
        return -1
    return 1    

class spiral:

    def __init__(self, r, alpha):

        self.r     = float(r)     # max radius of galaxy 
        self.alpha = float(alpha) # max angle of spiral

        # will be filled once stars are calculated
        self.numstars     = None
        self.starsizedist = None

        self.stars = [] 
    
    def calculate_stars(self, numstars = 1000, starsizedist = [1]):
        """ Calculate random locations for stars within the spiral """

        self.numstars     = numstars
        self.starsizedist = starsizedist

        for i in range(0, self.numstars):
            
            p = self.generate_random_star() 

            self.stars.append(p)

    # Note that this function should be stateless so that it can be
    # parallelized via standard monte-carlo approaches.  The galaxy class
    # should hold all of the needed parameters and distributions to allow
    # for random generation of a star 

    def generate_random_star(self):

        t = self.alpha * random.random()
        
        s = sign(t)
        t = abs(t)

        r = self.r * math.sqrt(t)
        x1 = s * r * math.cos(t)
        y1 = s * r * math.sin(t)
        # z1 = zeros(N,1);

        # create a sphere
        theta = random.random() * 360.
        phi   = random.random() * 360.

        rho = r
        x0 = rho * math.cos(theta) * math.sin(phi)
        y0 = rho * math.sin(theta) * math.sin(phi)
        z0 = rho * math.cos(phi);

        # combine spiral and sphere to create spiral galaxy
        # with dense cloud at center
        alpha   = (1. + math.cos(math.pi*r/(r)))/3.;
        alpha_z = (1. + math.cos(math.pi*r/(r)))/6.;

        x = alpha * x0 + (1.-alpha) * x1;
        y = alpha * y0 + (1.-alpha) * y1;
        z = alpha_z * z0;

        return star3D(x1,y1,z0)

    def displayXYZ(self, angleX, angleY, angleZ, viewer_x, viewer_y, distance,  screen):        
        """ Display to screen at rotation defined by XYZ """
        for star in self.stars:
            # Rotate the point around X axis, then around Y axis, and finally around Z axis.
            s = star.rotateX(angleX).rotateY(angleY).rotateZ(angleZ)
            # Transform the point from 3D to 2D
            p = s.project(screen.get_width(), screen.get_height(), 256,
                          viewer_x, viewer_y, distance)

            # draw to screen 
            pygame.draw.circle(screen, p.color,(int(p.x), int(p.y)), p.size)
