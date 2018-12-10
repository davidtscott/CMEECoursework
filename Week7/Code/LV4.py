#!/usr/bin/env python3
# Date: Nov 2018

"""
Discrete time version of L-V model with random gausian fluctuation
""" 

"""
Example of numerical integration using Lotka-Volterra model,
for predator prey relationship i two dimensional space.

Discrete time version

Edited so that it can take parameter values from command line.
sys.argv[1] = r, [2] = a, [3] = z, [4] = e. values converted to floats.

If five arguments are not given in command line (including script)
it uses default values: r = 1., a = 0.1, z = 1.5, e = 0.75

prints final non-zero value on screen.

Further edited with a random gaussian fluctuation in resources 
growth rate at each time step. 
""" 

__appname__ = '[LV4.py]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program" 

# example of numerical integration using lotka-volterra model

### Packages ###
import sys
import scipy as sc 
from scipy.stats import norm
import scipy.integrate as integrate
import matplotlib.pylab as p


def dCR_dt(pops): # t=0 is the default value, so can run without input
    """Lotka-Volterra pred-prey model"""
    R = pops[0] # resource (prey)
    C = pops[1] # Consumer (predator)
    K = 50
    E = norm.rvs(size = 1000)[0]   
    Rt = R * (1 + (r + E) * (1 - (R / K)) - a * C)
    Ct = C * (1 - z + e * a * R)
    Rt = max(Rt, 0) # sets bottom limit of 0, no upper limit. 
    Ct = max(Ct, 0) # 
 
    return sc.array([Rt, Ct])


## Define four LV model parameters
# give defaults and take arguments from command line
if len(sys.argv) != 5:   
    r = 1.      # intrinsic (per capita) growth rate of prey pop (time ^-1)
    a = 0.1     # search rate (per capita) for resource (area x time^-1)
    z = 1.5     # mortality rate 
    e = 0.75    # consumer efficiency in converting resource to consumer biomass
else: # takes arguements from command line and convert to floats
    r = float(sys.argv[1]) 
    a = float(sys.argv[2])
    z = float(sys.argv[3])
    e = float(sys.argv[4])
  
# K is the carry capacity 

### time interval
t = sc.linspace(0, 50, 1000) # 1000 point between 0 and 15
# 50 can be anything. minutes, seconds, years etc 
# timescales matter in biology
# depend on parameters. e.g tree would differ from bacteria 

# initiial R and C values
R0 = 10
C0 = 5
# RC0 = sc.array([R0, C0])

# data the feed into function 
listpop = sc.array([[R0,C0]]) # create array 
for i in t:     # for each time in t (defined above)  
    temppops = dCR_dt(listpop[-1]) # take last [R,C] from listpops, feed into dCR_dt
    print(temppops)
    if temppops[0] <= 0 or temppops[-1] <= 0:
        break   # if any value are 0 or below, stop. i.e 0 = extinct 
    listpop = sc.vstack((listpop,temppops)) # append output to listpop array

####
#print(temppops[-1])


### PLots ###

t = range(len(listpop)) # keeps length of to = len og listpop

f1 = p.figure() # open figure

p.plot(t, listpop[:,0], 'g-', label='Resource density') # plot time v resource (prey)
p.plot(t, listpop[:,1] , 'b-', label='Consumer density') # plot time v consumer (pred)
p.grid()    # add grid lines
p.legend(loc='best') # legend
p.text(1, 15, "r = %.2f, a = %.2f, z = %.2f, e = %.2f" % (r, a, z, e), fontsize = 15)
# add text line with parameter values r, a, z, e. 
#   format so they change depending on value given in command line
p.xlabel('Time') # add x axis label
p.ylabel('Population density') # add y axis label 
p.title('Consumer-Resource population dynamics') # add plot title
p.show() #displays figure

f1.savefig('../Results/LV4_model1.pdf') # save figure

#####

f2 = p.figure() # open figure

p.plot(listpop[:,0], listpop[:,1], 'r-') #plots resource against consumber density
p.grid() # plot grid lines
p.text(12, 4, "r = %.2f, a = %.2f, z = %.2f, e = %.2f" % (r, a, z, e), fontsize = 15)
# add text line with parameter values r, a, z, e. 
#   format so they change depending on value given in command line
p.xlabel('Resource density') # x axis label
p.ylabel('Consumer density')    # y axis label
p.title('Consumer-Resource population dynamics') # plot title 
p.show() #displays figure

f2.savefig('../Results/LV4_model2.pdf') #save figure
