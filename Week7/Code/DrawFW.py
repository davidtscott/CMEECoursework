#!/usr/bin/env python3
# Date: Nov 2018

"""
Creates and plots a synthetic food web network
""" 

__appname__ = '[food web networks in python]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program" 

### modules imports 
import networkx as nx
import scipy as sc 
import matplotlib.pyplot as p 

def GenRdmAdjList(N = 2, C = 0.5): # C = connection probability 
    """ Generates a random adjacency list of N -species 
    food web with "connectance probability" C: the propability 
    of having a link between any pair of secies in the web. 
    """
    Ids = range(N) # list of given range (N)
    ALst = [] #creates list
    for i in Ids:  #loop for i in range N 
        if sc.random.uniform(0,1,1) < C: # 
            Lnk = sc.random.choice(Ids,2).tolist()
            if Lnk[0] != Lnk[1]: #avoid self (e.g., cannabilistic) loops
                ALst.append(Lnk)
    return ALst
 
# assign number of species and connectance 
MaxN = 30 #number of species
C = 0.75  # connectance

#adjacency list representign random food web
AdjL = sc.array(GenRdmAdjList (MaxN, C))
AdjL

#generate species node data
Sps = sc.unique(AdjL) # get species id 

# body sizes for species. uses log10 scale
#      body sizes log normally distributed 
SizRan = ([-10,10]) # log10 scale
Sizs = sc.random.uniform(SizRan[0],SizRan[1],MaxN)
Sizs 

## visualise distribution 
p.hist(Sizs) #log10 scale
p.show()

p.hist(10 ** Sizs) #raw scale
p.show()

p.close('all') #close all open plot objects

#plot network with node sizes proportional to body size (log)
# use circular configuration
pos = nx.circular_layout(Sps) # calculate the coordinates

# generates networkx graph object
G = nx.Graph()

# add nodes and links (edges)
G.add_nodes_from(Sps)
G.add_edges_from(tuple(AdjL)) # this function needs a tuple input 

#generate node sizes, proportional to log body sizes
NodSizs = 1000 * (Sizs - min(Sizs))/(max(Sizs)-min(Sizs))

# plot and save graph
f = p.figure()
nx.draw_networkx(G, pos, node_size = NodSizs)
p.show(f)
f.savefig("../Results/DrawFW.pdf")
