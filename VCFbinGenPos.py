#!/usr/bin/python

import sys
import numpy as np
import pandas as pd
#this sets the number of rows to display/print - otherwise tructates to 64 rows
pd.set_option('display.max_rows',10000)

#when splitting a table into columns, this sets the column names to be used a variables later
my_cols=['col1','col2','col3','col4','col5','col6','col7','col8','col9','col10','col1','col2','col13','col14','col15']

#take filename from command line
filename = sys.argv[-1]

#using the module panda split a table by the tab, readable by panda
#skiprows - skip lines (x) the data after gets dumped into an array - where x = number of rows to skip.
df = pd.read_csv(filename,sep='\t',skiprows=(34),header=None,names=my_cols)
df.apply(pd.to_numeric, errors='ignore')
#print df.col2
#sorts a column
df=df.sort_values('col2')
#using numpy, splits a column into bins of 5000, format=start,end,stepsize
bins=np.arange(0,5000000,2000)
#using numpy digitize, splits X column into each of the bins
ind=np.digitize(df['col2'],bins)
#panda groupby commnand, treats each bin as a distint unit and the size() command counts the number of rows. mean() calculates the mean etc..
print df.groupby(ind).size()
