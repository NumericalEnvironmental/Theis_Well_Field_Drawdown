##############################################################################################
#
# AEM - semi-analytical solution for steady-state groundwater flow
# in the presence of injectors (point or line sources) and semi-permeable
# fault segments
#
# injectors and faults inherit parameters and methods from generalized
# linear segment class
#
# by W. McNab
#
##############################################################################################

from numpy import *
from scipy.special import *
from scipy.spatial import distance


class Aquifer:              # container for aquifer properties (uniform)

    def __init__(self, K, Ss, b):
        self.K = K                  # hydraulic conductivity
        self.Ss = Ss                # specific storage
        self.b = b                  # aquifer thickness


class Well:

    def __init__(self, x, y, Q, aquifer):
        self.loc = array([[x, y]])          # well coordinates
        self.Q = Q                          # pumping rate
        self.aquifer = aquifer              # aquife robject

    def W(self, u):
        # exponential integral/well function
        return expn(1,u)

    def S(self, r, t):
        # change in hydraulic head from pumping
        u = (r**2)*self.aquifer.Ss*self.aquifer.b/(4.*self.aquifer.K*self.aquifer.b*t) 
        return self.Q*self.W(u)/(4.*pi*self.aquifer.K*self.aquifer.b)

    def Impact(self, pts, t):
        # calculate the hydraulic head impact from well to a 
        # n x 2 vector of (x, y) points, loc
        r = distance.cdist(self.loc, pts)[0]
        return self.S(r, t)

        
class Grid:

    def __init__(self, x0, y0, xf, yf, num_x, num_y):
        # create a uniform grid with supplied specs and 
        # convert to a n x 2 array
        x = linspace(x0, xf, num_x+1)
        y = linspace(y0, yf, num_y+1)
        X, Y = meshgrid(x,y)
        self.points = matrix([X.flatten(), Y.flatten()]).T
        self.S = zeros(len(self.points), float)

    def Calculate(self, well, t):
        
        # calculate net drawdown and write to output file
        for w in well:
            self.S += w.Impact(self.points, t)    
             
        # write results to output file        
        output_file = open('head_charge.csv','w')
        output_file.writelines(['x',',','y',',','dh','\n'])
        for (i, pt) in enumerate(self.points):
            output_file.writelines([str(pt[0, 0]),',',str(pt[0, 1]),
                ',', str(self.S[i]),'\n'])
        output_file.close()
        

def ReadParams():
    # read model parameters and assign to appropriate object
    param = []     
    input_file = open('params.txt','r')
    for line in input_file:
        line_input = line.split()
        param.append(line_input[1]) 
    input_file.close()
    K = float(param[0])         # hydraulic conductivity
    Ss = float(param[1])        # specific storage
    b = float(param[2])         # aquifer thickness
    x0 = float(param[3])        # grid margins, x-direction
    xf = float(param[4])
    y0 = float(param[5])        # grid margings, y-direction
    yf = float(param[6])
    num_x = int(param[7])       # grid discretization
    num_y = int(param[8])
    aquifer = Aquifer(K, Ss, b)
    grid = Grid(x0, y0, xf, yf, num_x, num_y)
    return aquifer, grid
    
    
def ReadWells(aquifer):
    # read well file and assign well objects
    well = []
    input_file = open('wells.txt')
    for (i, line) in enumerate(input_file):
        if i:
            line_input = line.split()
            well.append(Well(float(line_input[0]), float(line_input[1]),
                float(line_input[2]), aquifer))
    return well            

    
def TheisField(t):               ### main script; t = elapsed pumping time ###

    print 'Reading model parameters ...'
    aquifer, grid = ReadParams()

    print 'Reading well file ...'
    well = ReadWells(aquifer)

    print 'Calculating ...'
    grid.Calculate(well, t)

    print 'Done.'


### run script ###

t = 180.
TheisField(t)
