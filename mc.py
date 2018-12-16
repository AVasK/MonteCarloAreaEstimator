### Monte-Carlo method for area-estimation ###

import random
import numpy as np
import matplotlib.pyplot as plt

# Object consisits of vertices <=> [(x,y)]

#====================================
# Auxiliary, yet very important code

def close_path(v : []):
    v = v[:]
    v.append(tuple(v[0]))
    return v

# First, we need to solve the inside-outside problem:
def is_inside(vertices : [()], pt : tuple, verbose = False):
    
    """ For a closed shape tells if pt lies inside object, """
    """ Where object is defined by its vertices.           """

    #v.append(tuple(vertices[0]))    
    vertices = close_path(vertices)
    edges = [(vertices[i], vertices[i+1]) for i in range(len(vertices) - 1)]
    pt_x, pt_y = pt
    crossings = 0
    
    # Debugging output (if verbose = True)
    if verbose : 
        print(vertices)
        for edge in edges:
            print("edge: ", edge)
    
    
    # Checking properties for all edges 
    # (can be parallelized easily if needed)
    for edge in edges:
        (a_x, a_y), (b_x, b_y) = edge # edge = ((a_x, a_y), (b_x, b_y))
        
        """
        # Checking cases:
        # 1. both to the left:
        if a_x < pt_x and b_x < pt_x:
            pass # doing nothing
        # 2. both to the right
        if a_x > pt_x and b_x > pt_x:
            pass # doing nothing
        # 3. both endpoints of the edge are below testpoint:
        if a_y < pt_y and b_y < pt_y:
            pass
        """
        
        # 4. if they are above, then:
        if a_y > pt_y and b_y > pt_y:
            # 4.1 if testpoints are to diff sides from testpoint
            if (a_x - pt_x) * (b_x - pt_x) <= 0: # non-strict equality recognizes on-the-boundary case.
                crossings += 1
                
        # 5. edge's bounding box encloses point:
        if (a_x - pt_x) * (b_x - pt_x) <= 0 and (a_y - pt_y)*(b_y - pt_y) <= 0:
            if a_x < b_x:
                y_l = a_y
                x_l = a_x
                y_r = b_y
                x_r = b_x
            else:
                y_l = b_y
                x_l = b_x
                y_r = a_y
                x_r = a_x
            
            y_cross = y_l + ((y_r - y_l)/(x_r - x_l))*(pt_x - x_l)
            
            if y_cross > pt_y:
                crossings += 1 # the ray crosses the edge
            
    if verbose:
        print("Crossings: ", crossings)
        
    return not crossings % 2 == 0

#============================================
# Building bounding box (just in case)
    
#print(is_inside([(1,1), (3,1), (3,3), (1,3)], (2,0)))

def bound_coord(vertices : [()]):
    # Using None type to elude 
    # premature initialization
    max_x, min_x = None, None
    max_y, min_y = None, None
    
    for x, y in vertices:
        if not max_x:
            max_x = x
        if not min_x:
            min_x = x
        if not max_y:
            max_y = y
        if not min_y:
            min_y = y
            
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
    
    return min_x, max_x, min_y, max_y

def bb_area(vertices : [()]):
    x_min, x_max, y_min, y_max = bound_coord(vertices)
    return (x_max - x_min)*(y_max - y_min)

def build_bounding_box(vertices : [()]):
    x_min, x_max, y_min, y_max = bound_coord(vertices)
    return ((x_min, y_min), (x_max, y_min), (x_max, y_max), (x_min, y_max))


#==========================================
# Sampling functions:

# Random sampler for MC
def sample(_min, _max):
    return random.random() * (_max - _min) + _min

# Subrandom sampler for QMC.
# Those other types of samplers are used to
# get lower discrepancy.
# not the most honest subrandom sampler, actually
# still yields better results mean-wise.
def subsample(_min, _max):
    s = (subsample.prev + 0.5 * random.random()) % 1
    subsample.prev = s
    return s * (_max - _min) + _min
subsample.prev = 0


#==========================================
# Monte Carlo method:

def MC(vertices, iters, visualize = False, s_type = "rand"):
    """ Calculating area using Monte-Carlo method """
    x_min, x_max, y_min, y_max = bound_coord(vertices)
    inside = 0
    sampler = {}
    sampler["rand"] = sample
    sampler["subrand"] = subsample
    
    if visualize:
        # Plotting the bounding box:
        bb_xy = close_path(list(build_bounding_box(vertices)))
        bb_x, bb_y = zip(*bb_xy) # unzipping coordinates
        plt.plot(bb_x, bb_y, c = 'y')
        # Plotting the figure:
        f_xy = close_path(vertices)
        f_x, f_y = zip(*f_xy)
        plt.fill(f_x, f_y, c = 'b', alpha = 0.5)
    
    for _ in range(iters):    
        (rx, ry) = sampler[s_type](x_min, x_max), sample(y_min, y_max)
        clr = 'r'
        mrk = 'x'
        if is_inside(vertices, (rx, ry)):
            inside += 1
            clr = 'g'
            mrk = 'o'
            
        if visualize:
            plt.scatter(rx, ry, marker = mrk, c = clr, s = 15)
            
    if visualize:
        plt.show()
            
    return bb_area(vertices) * inside/iters
        
        
        
#==========================================
# Calculating mean:

def area(vertices, iters, mean_iters, s_type = "rand"):
    return np.array([MC(vertices, iters, s_type) for _ in range(mean_iters)]).mean()