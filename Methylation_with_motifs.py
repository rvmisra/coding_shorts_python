#!/usr/bin/python
#Meths for which a motif is present, which basically pulls in just m6A as m4C has no motifs.

import sys
import numpy as np
import pandas as pd
from itertools import ifilter

filename = sys.argv[-1]
pd.set_option('display.max_rows',100000)
my_cols=['col1','col2','col3','col4','col5','col6','col7','col8','col9','col10','col11','col12','col13','col14','col15','col16','col17','col18','col19','col20','col21','col22','col23','col24','col25']

open('temp.txt','w').writelines(line for line in open(filename) if 'm6A' in line and 'motif' in line or 'm4C' in line and 'motif' in line)

df = pd.read_csv('temp.txt',sep='\t|=|;',skiprows=(1),header=None,names=my_cols, engine='python')
df.apply(pd.to_numeric, errors='ignore')
df=df.loc[df['col17'] > 1.7]
df.to_csv('np.txt', sep='\t')
#print df.col17
df= pd.read_csv('np.txt',sep='\t',skiprows=(1),header=None,names=my_cols, engine='python')
df=df.sort_values('col4')
#print df.col12
bins=np.arange(0,6000000,5000)
ind=np.digitize(df['col4'],bins)
print df.groupby(ind).size()
