
import argparse
import math

import Vec3d

opts_full = \
{
    "gauss-stars" : 1, # use gaussian attenuation for stars
                       # this has a major performance impact so
                       # not good for real time viewing with high
                       # numbers of stars
    "star-field" : 1,  # create a starfield outside of the galaxy(s)

    "scale-stars" : 0, #scale star size with distance
    "scale-max-distance" : 1000, # distance at which a star is at the
                                 # smallest size

    "star-size-dist" : \
        [2,2,3,3,4,4,5,5,8,8,12,12,14,14,16,16,18,18,20,20],


    "spiral-numstars" : 10000, # number of stars used to make up the
                              # spiral galaxy
    "spiral-fuzz" : 0.2,  # entropy to throw at spiral galaxy 
    "spiral-diameter" : 200, # 

    "obj-axis-show" : 0, # show 3D axis with object

    "obj-auto-rotate" : 0, # rotate the object 

    "viewer-x": 0,  # x position of the user 
    "viewer-y": 0,  # y position of the user
    "viewer-z" : 400,

    "viewer-dir" : Vec3d.Vec3d(1,0,0),


    "obj-angle-x" : 0,
    "obj-angle-y" : 0,
    "obj-angle-z" : 0,
}

opts_realtime = \
{
    "gauss-stars" : 0, # use gaussian attenuation for stars
                       # this has a major performance impact so
                       # not good for real time viewing with high
                       # numbers of stars
    "star-field" : 0,  # create a starfield outside of the galaxy(s)

    "star-size-dist" : [0,0,0,0,0,0,1,1,1,2,2,2,3,3,4,4,5],

    "scale-stars" : 1, #scale star size with distance
    "scale-max-distance" : 100, # distance at which a star is at the
                                 # smallest size

    "spiral-numstars" : 4000, # number of stars used to make up the
                              # spiral galaxy
    "spiral-fuzz" : 0.2,  # entropy to throw at spiral galaxy 
    "spiral-diameter" : 40, # 

    "obj-auto-rotate" : 0, # rotate the object 

    "obj-axis-show" : 1, # show 3D axis with object

    "viewer-x": 0,  # x position of the viewer 
    "viewer-y": 0,  # y position of the viewer
    "viewer-z" : 50,

    "viewer-dir" : Vec3d.Vec3d(1,0,0),

    "obj-angle-x" : 0,
    "obj-angle-y" : 0,
    "obj-angle-z" : 0,
}

cla_parser = argparse.ArgumentParser(description='Galaxy creation and viewing')
cla_parser.add_argument('-r','--realtime', action='store_true', help='configurations to allow for real time viewing')

args = cla_parser.parse_args()

if args.realtime:
    opts = opts_realtime
else:
    opts = opts_full
