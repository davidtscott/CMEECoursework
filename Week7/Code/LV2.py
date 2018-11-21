#!/usr/bin/env python3
# Date: Nov 2018

"""
L-V model, takes parameter values from command line 
"""

"""
Second example of numerical integration using Lotka-Volterra model,
for predator prey relationship in two dimensional space.

Edited so that it can take parameter values from command line.
sys.argv[1] = r, [2] = a, [3] = z, [4] = e. values converted to floats.

If five arguments are not given in command line (including script)
it uses default values: r = 1., a = 0.1, z = 1.5, e = 0.75

parameter values altered so that predator and prey persist with prey 
density dependence. 

prints final non-zero value on screen.
""" 

__appname__ = '[numerical integration in python]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program" 

# example of numerical integration using lotka-volterra model

### Packages ###
import scipy as sc 
import sys
import scipy.integrate as integrate
import matplotlib.pylab as p


def dCR_dt(pops, t=0): # t=0 is the default value, so can run without input
    """Lotka-Volterra pred-prey model"""
    R = pops[0] # resource (prey)
    C = pops[1] # Consumer (predator)
    K = 50
    dRdt = (r * R) * (1 - (R / K)) - a * R * C 
    dCdt = -z * C + e * a * R * C

    return sc.array([dRdt, dCdt])

type(dCR_dt)

## Define four LV model parameters
# give defaults and take arguments from command line
if len(sys.argv) != 5:   
    r = 1.      # intrinsic (per capita) growth rate of prey pop (time ^-1)
    a = 0.1     # search rate (per capita) for resource (area x time^-1)
    z = 2.     # mortality rate 
    e = .75    # consumer efficiency in converting resource to consumer biomass
else: # takes arguements from command line and convert to floats
    r = float(sys.argv[1]) 
    a = float(sys.argv[2])
    z = float(sys.argv[3])
    e = float(sys.argv[4])
  
# K is the carry capacity 

t = sc.linspace(0, 50, 1000) # 1000 point between 0 and 15
# 15 cn be anything. minutes, seconds, years etc 
# timescales matter in biology
# depend on parameters. e.g tree would differ from bacteria 

R0 = 10
C0 = 5
RC0 = sc.array([R0, C0])

pops, infodict = integrate.odeint(dCR_dt, RC0, t, full_output=True)
# odeint takes start vales, feeds to function 

type(infodict)

infodict.keys()

infodict['message']

### PLots ###

f1 = p.figure() # open figure

p.plot(t, pops[:,0], 'g-', label='Resource density') # plot time v resource (prey)
p.plot(t, pops[:,1] , 'b-', label='Consumer density') # plot time v consumer (pred)
p.grid()    # add grid lines
p.legend(loc='best') # legend
p.text(5, 15, "r = %.2f, a = %.2f, z = %.2f, e = %.2f" % (r, a, z, e), fontsize = 15)
# add text line with parameter values r, a, z, e. 
#   format so they change depending on value given in command line
p.xlabel('Time') # add x axis label
p.ylabel('Population density') # add y axis label 
p.title('Consumer-Resource population dynamics') # add plot title
# p.show() #displays figure

f1.savefig('../Results/LV2_model.pdf') # save figure

#####

f2 = p.figure() # open figure

p.plot(pops[:,0], pops[:,1], 'r-') #plots resource against consumber density
p.grid() # plot grid lines
p.text(12, 4, "r = %.2f, a = %.2f, z = %.2f, e = %.2f" % (r, a, z, e), fontsize = 15)
# add text line with parameter values r, a, z, e. 
#   format so they change depending on value given in command line
p.xlabel('Resource density') # x axis label
p.ylabel('Consumer density')    # y axis label
p.title('Consumer-Resource population dynamics') # plot title 
# p.show() #displays figure

f2.savefig('../Results/LV2_model2.pdf') #save figure
