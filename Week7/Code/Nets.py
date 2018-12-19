#!/usr/bin/env python3

"""Network visualization of QMEE CDT collaboration network. Nodes are coloured by type of node""" 

__appname__ = '[Nets.py]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"

## imports ##
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

##  import data 
# read in edges (links) and nodes data as a pandas dataframes
edgesDF = pd.read_csv("../Data/QMEE_Net_Mat_edges.csv")
nodesDF = pd.read_csv("../Data/QMEE_Net_Mat_nodes.csv")

# convert nodes dataframe to categorical values 
nodesDF['Type']=pd.Categorical(nodesDF['Type'])
newNode = nodesDF['Type'].cat.codes

# convert edges dataframe to just values
edges_values = edgesDF.values

G = nx.from_numpy_matrix(np.array(edges_values)) 

# open empty figure
plt.figure()
# draw it. specify labels and colour by "type"
nx.draw(G, labels = nodesDF["id"], node_color=newNode, with_labels=True)
plt.show()
# save as svg
plt.savefig("../Results/Nets_py.svg", format = "svg")
