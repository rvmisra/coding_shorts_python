#!/usr/bin/python
#Methylation events identified for which a motif is NOT present

import sys
import numpy as np
import pandas as pd
from itertools import ifilter
#reads input filename from command line
filename = sys.argv[-1]
#this sets the number of rows to display/print - otherwise tructates to 64 rows
pd.set_option('display.max_rows',100000)
#column variable names
my_cols=['col1','col2','col3','col4','col5','col6','col7','col8','col9','col10','col11','col12','col13','col14','col15','col16','col17','col18','col19','col20','col21','col22','col23','col24','col25']
#creates a temp file. The input file is filtered based on the if statement, output is written to temp file
open('temp.txt','w').writelines(line for line in open(filename) if 'modified_base' not in line and 'motif' not in line)
#using pandas - the temp file is read, split by the delimeters into column variables at the top and the first row skipped
df = pd.read_csv('temp.txt',sep='\t|=|;',skiprows=(1),header=None,names=my_cols, engine='python')
#all columns are changed to numeric - any errors are ignored e.g. column only has strings
df.apply(pd.to_numeric, errors='ignore')
#goes to column 16 = IPD ratio values and filters by the set value
df=df.loc[df['col16'] > 1.7]
#output from IPD ratio filter is written to another temp file called np.txt
df.to_csv('np.txt', sep='\t')
#temp file is read, split by tab into column variables at the top, first row skipped
df= pd.read_csv('np.txt',sep='\t',skiprows=(1),header=None,names=my_cols, engine='python')
#sorts column 4 = modification start position
df=df.sort_values('col4')
#print df.col12
#creates bins
bins=np.arange(0,6000000,5000)
#numpy used to split col4 into the bins
ind=np.digitize(df['col4'],bins)
#counts number of rows per bin
print df.groupby(ind).size()
