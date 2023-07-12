#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import networkx as nx ##Required 


# In[2]:


# Load the dataset
G = pd.read_csv("/Users/sonavaneonkar/Documents/Programming/Data Science/360digiTMG/Classes/9. Recomendation engine - 2 and Network_Analytics/Network_Analytics/routes.csv")
G = G.iloc[0:50, 1:10] ## taking first 50 datapoints and first 10 columns.
G.info()


# In[3]:


g = nx.Graph() # 'g' is a graph object.
g = nx.from_pandas_edgelist(G, source = 'Source Airport', target = 'Destination Airport')

print(nx.info(g))


# In[4]:


# Degree Centrality
d = nx.degree_centrality(g) ## This is the direct ties or connection distance between the two nodes
print(d) 


# In[5]:


# Update the decorator package to 5.0.7 to over come the 'random_state_index is incorrect' error
# pip install decorator==5.0.7

pos = nx.spring_layout(g)
nx.draw_networkx(g, pos, node_size = 15, node_color = 'red')


# In[6]:


# closeness centrality
closeness = nx.closeness_centrality(g)
print(closeness)


# In[7]:


## Betweeness Centrality 
b = nx.betweenness_centrality(g) # Betweeness_Centrality
print(b)


# In[8]:


## Eigen-Vector Centrality
evg = nx.eigenvector_centrality(g) # Eigen vector centrality
print(evg)


# In[9]:


# cluster coefficient ## Having more cluster coefficient in context of airport is not good...If Having cc 1, 
# it means every airport connected to a specific airport, then those all airports are connected to each other,
# that means it has cc 1
cluster_coeff = nx.clustering(g)
print(cluster_coeff)


# In[10]:


# Average clustering
cc = nx.average_clustering(g) 
print(cc)


# In[ ]:




