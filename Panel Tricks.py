import pandas as pd
#### Load and Save Data #######################################################
path="P:/BitTorrent/"; year='2012'
data=pd.read_csv(path+'Panel_'+year+'.csv',parse_dates=True)
data.describe()
print data.head()
data.ix[0:4,0:4]; len(data.index)
data.to_csv(path+'Panel_'+year+'.csv',parse_dates=True)
#### Remove Duplicate Observations ############################################
data.drop_duplicates(cols=None,take_last=False,inplace=True)
#### Pivot Table ##############################################################
data=data.dropna(axis=0,how='all'); data=data.reset_index()
data=data.pivot(index='DateTime',columns='Ticker',values='VPIN')
#### Notes ####################################################################
path="/Data/Research/TAQ/"; year='2005'
data=pd.read_csv('/Data/Research/TAQ/PricePanel_'+year+'.csv',parse_dates=True)
prows=len(data['Ticker'].unique())
Tickers=pd.read_csv('/Data/Research/TAQ/Tickers'+year+'.csv',header=None,na_values='',keep_default_na=False)
trows=len(Tickers.index)
print prows
print trows
# 310898785 200904
data=pd.read_csv("/Data/Copy/Data Sets/Chinese TAQ/2003/LT_Strlargetrd.xls",skiprows=4,nrows=100,header=None)
data=pd.read_csv('/Data/201002.csv',nrows=1,header=None)
print data.ix[0:5,0:10]
data=pd.read_csv('/Data/201010.csv',nrows=5)
data.head()
data.tail()
#### Conditional Select ########################################################
data=data[data.Ticker!='ABX']