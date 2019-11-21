# Dealing with data in HDF5 with pandas and pytables
import pandas as pd
import os
if os.getcwd()!="/Data/Dropbox/Workspace/Python":
    os.chdir('/Data/Dropbox/Workspace/Python')
# Read from csv
data=pd.read_csv("/Data/Copy/Data Sets/USD_JPY_Week1.csv",na_values=[" "])
print data.head();
data.describe()
data.plot()
# Set date index (check index with "data.index")
data.RateDateTime=pd.to_datetime(data.RateDateTime)
data=data.set_index(["RateDateTime"])
data=data.iloc[1:,3:5] # Select the third and fourth columns
data['2012-12-02 17:00'] # Select a minute

# Store in HDF5 format
data.to_hdf('test.h5','USD_JPY')
# Read an array from HDF5
data=pd.read_hdf('test.h5','USD_JPY')
# Attach an HDF5 file
disk=pd.HDFStore('test.h5')

# Create an average
data['RateMid']=(data['RateBid']+data['RateAsk'])/2
# Create Volume
data['Volume']=1
# Combine over time
tbars=data['Volume'].resample('1Min',how='sum')
