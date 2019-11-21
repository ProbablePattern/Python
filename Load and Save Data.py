#Created on Sat Jan 12 11:08:24 2013
import pandas as pd
data=pd.read_csv("/Data/Copy/Data Sets/Data/VIX.csv",na_values=[" "])
data=pd.read_csv("/Data/Dropbox/Research/Qualifying Paper/Panel.csv",na_values=[" "])
model=pd.ols(y=data.lp, x=data.xcash1)
panel = pd.Panel(data,major_axis=['Date'],minor_axis=['CUSIP'])
panel = pd.data.set_index(['Date', 'CUSIP']).sortlevel(0).to_panel()
panel = data.to_panel()
fe_model = pd.ols(y=data.lp, x=data['xcash1'], entity_effects=True, intercept=False)
print data
print data["DATE"]
print data[data["VIXCLS"]>20]
print "Mean VIX close:", data["VIXCLS"].mean()
data.describe()
data.DATE.is_unique
data=data.set_index(["DATE"])


# Basics
import os
os.getcwd()

# Numpy stuff
import numpy as np

# Date conversion
test=datetime.strptime(data["DATE"],"%Y-%m-%d")
data.apply()

# Drop extreme obs
print data[data['MAT']<=30]
data=data[data['MAT']<=30]

# Econometrics
import statsmodels.api as sm
m1=sm.GLM(data.lp, data[['TERM','DEF','rf','VIX','Trading','MAT','DUR','xcash1']])
model=m1.fit()
print model.summary()

# SQLite
import sqlite3 as lite
import sys
con = lite.connect('test.db')
cur = con.cursor()    
cur.execute('SELECT SQLITE_VERSION()')
data = cur.fetchone()
print "SQLite version: %s" % data
if con:
        con.close()