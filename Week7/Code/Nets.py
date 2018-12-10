#!/usr/bin/env python3

"""  """ 

__appname__ = '[Nets.py]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"

# packages
#import csv
#import networkx as nx
#import scipy as sc
import matplotlib.pyplot as p
import pandas as pd
import itertools
import copy 
import igraph

# import data 
#with open ("../Data/QMEE_Net_Mat_edges.csv", "r") as csv_links:
#    links = csv.reader(csv_links)

edges_list = pd.read_csv("../Data/QMEE_Net_Mat_edges.csv")
edges_list

#with open ("../Data/QMEE_Net_Mat_nodes.csv", "r") as csv_nodes:
#    nodes = csv.reader(csv_nodes)

nodes_list = pd.read_csv("../Data/QMEE_Net_Mat_nodes.csv")
nodes_list['id']

#####
####


A = edges_list.values

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
g = nx.Graph()


# Add links to graph


for i, llrow in links_list.iterrows():
    g.add_edge(llrow[0:],  attr_dict=llrow[2:].to_dict()))


# Add nodes to graph
for i, nlrow in nodes_list.iterrows():
    g.node[nlrow['id']] = nlrow[1:].to_dict()

print(nlrow)