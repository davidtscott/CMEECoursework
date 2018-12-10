#!/usr/bin/env python3

"""  """ 

__appname__ = '[Nets.py]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"

# packages
#import csv
import networkx as nx
#import scipy as sc
import matplotlib.pyplot as plt
import pandas as pd
import itertools
import copy 
import igraph
import numpy as np

##  import data 
# read in edges (links) and nodes data as a pandas dataframes
edgesDF = pd.read_csv("../Data/QMEE_Net_Mat_edges.csv")
nodesDF = pd.read_csv("../Data/QMEE_Net_Mat_nodes.csv")

edgesDF
nodesDF
# convert edges dataframe to just values
edges_values = edgesDF.values
edges_values
# find the position of each value within the array 
A = np.where(edges_values)
A

# array of unique values as they occur other than 0. values are not repeated
weights = edges_values[A]
weights

# create list of tuples 
edge1 = list(A[0])
edge2 = list(A[1])

edge2

## convert index values to names 
def index_to_name(a):
    for n, i in enumerate(a):
        if i == 0:
            a[n] = "ICL"
        elif i == 1:
            a[n] = "UoR" 
        elif i == 2:
            a[n] = "CEH"
        elif i == 3:
            a[n] = "ZSL"         
        elif i == 4:
            a[n] = "CEFAS"
        elif i == 5:
            a[n] = "NonAc" 
    return a 

edge1 = index_to_name(edge1)
edge2 = index_to_name(edge2)
edge2

# zip list together with weights 
edges = list(zip(edge1, edge2, weights))
edges
# convert list to tuples to pandas dataframe
edDF = pd.DataFrame(edges)
edDF
#edDF.reset_index(drop=True)

# Create empty graph
g = nx.Graph()

# Add edges and edge attributes
for i, elrow in edDF.iterrows():
    g.add_edge(elrow[0], elrow[1], attr_dict=elrow[2:].to_dict())

# Add node attributes
for i, nlrow in nodesDF.iterrows():
    g.node[nlrow['id']].update(nlrow[1:].to_dict())

g.edges
g.nodes

# Define data structure (list) of edge colors for plotting
node_colors = [e[1]["Type"] for e in g.nodes(data=True)]
node_colors
g.nodes
plt.figure(figsize=(8, 6))
nx.draw(g, node_size=10, node_color= node_colors)
plt.title('Graph Representation of ', size=15)
plt.show()




#g.node[nlrow['id']] = nlrow[1:].to_dict()
##########

G = igraph.Graph(edges=edges, directed=True)


# assign node names and weights to be attributes of the vertices and edges
# respectively
node_names = nodes['id']
G.es['width'] = weights
G.vs['label'] = node_names
G.es['weight'] = weights

G.es['width'] = weights/10
# plot the graph
out = igraph.plot(G,'../Results/Netspy.pdf', layout="rt", labels=True, margin=80)
print 'Netspy.pdf saved to Results'


###############
g = igraph.Graph.Adjacency((A > 0).tolist())

# Add edge weights and node labels.
g.es['weight'] = A[A.nonzero()]
g.vs['label'] = nodes_list['id']  # or a.index/a.columns

df_from_g = pd.DataFrame(g.get_adjacency(attribute='weight').data, \
             columns=g.vs['label'], index=g.vs['label'])

(df_from_g == a).all().all()  # --> True

#df_from_g = df_from_g.values.tolist()
df_from_g = pd.Series.tolist(df_from_g)

df_from_g

net = igraph.Graph.Adjacency(df_from_g, mode='ADJ_DIRECTED')#"ADJ_DIRECTED")


# create graph 
g = nx.Graph()edges


# Add links to graph


for i, llrow in links_list.iterrows():
    g.add_edge(llrow[0:],  attr_dict=llrow[2:].to_dict()))


# Add nodes to graph
for i, nlrow in nodes_list.iterrows():
    g.node[nlrow['id']] = nlrow[1:].to_dict()

print(nlrow)