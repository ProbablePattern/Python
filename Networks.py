import os
if os.getcwd()!="/Data/Dropbox/Workspace/Python":
    os.chdir('/Data/Dropbox/Workspace/Python')
import pandas as pd
import networkx as nx

data=pd.read_csv("/Data/Copy/Data Sets/Returns 1990-2009.csv",skiprows=1)
data=data.set_index(['Date'])
print data.head(); # Check it