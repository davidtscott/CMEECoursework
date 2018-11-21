#!/usr/bin/env python3
# Date: Nov 2018

"""
Lotka Volterra numerical integration model
"""

"""
Example of numerical integration using Lotka-Volterra model,
for predator prey relationship in two dimensional space.

Prints two graphs to the ../Results directory
""" 

__appname__ = '[numerical integration (L-V) in python]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program" 

# example of numerical integration using lotka-volterra model

# packages ###
import scipy as sc 
import scipy.integrate as integrate 
import matplotlib.pylab as p


def dCR_dt(pops, t=0): # t=0 is the default value, so can run without input
    """Lotka-Volterra pred-prey model"""
    R = pops[0]  # resource (prey)
    C = pops[1]  # Consumer (predator)
    dRdt = r * R - a * R * C 
    dCdt = -z * C + e * a * R * C

    return sc.array([dRdt, dCdt])

#type(dCR_dt)

r = 1.      # intrinsic (per capita) growth rate of prey pop (time ^-1)
a = 0.1     # search rate (per capita) for resource (area x time^-1)
z = 1.5     # mortality rate 
e = 0.75    # consumer efficiency in converting resource to consumer biomass

t = sc.linspace(0, 15, 1000) # 1000 point between 0 and 15
# 15 cn be anything. minutes, seconds, years etc 
# timescales matter in biology
# depend on parameters. e.g tree would differ from bacteria 

R0 = 10 # start point for R
C0 = 5  # start point for C
RC0 = sc.array([R0, C0])

pops, infodict = integrate.odeint(dCR_dt, RC0, t, full_output=True)
# odeint takes start vales, feeds to function 

#type(infodict)

infodict.keys()

infodict['message']

### PLOTS ###

f1 = p.figure() # open new plot

p.plot(t, pops[:,0], 'g-', label='Resource density') # plot time v resource (prey)
p.plot(t, pops[:,1] , 'b-', label='Consumer density') # plot time v consumer (pred)
p.grid() # grid lines
p.legend(loc='best')  # leged 
p.xlabel('Time')  # x axis label
p.ylabel('Population density') # y axis label
p.title('Consumer-Resource population dynamics') # plot title
#p.show() #displays figure

f1.savefig('../Results/LV_model.pdf') # save plot 

#####

f2 = p.figure() # open new plot 2

p.plot(pops[:,0], pops[:,1], 'r-') #plots resource (prey) v consumer (pred) density
p.grid()  #grid lines
p.xlabel('Resource density')  # x axis label
p.ylabel('Consumer density')  # y axis label
p.title('Consumer-Resource population dynamics') # plot title
#p.show() #displays figure

f2.savefig('../Results/LV_model2.pdf') # saves plot 2
