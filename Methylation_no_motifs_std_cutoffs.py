#!/usr/bin/python
#Methylation events identified for which a motif is NOT present

import sys
import numpy as np
import pandas as pd
from itertools import ifilter

filename = sys.argv[-1]

pd.set_option('display.max_rows',100000)

my_cols=['col1','col2','col3','col4','col5','col6','col7','col8','col9','col10','col11','col12','col13','col14','col15','col16','col17','col18','col19','col20','col21','col22','col23','col24','col25']

open('temp.txt','w').writelines(line for line in open(filename) if 'modified_base' not in line and 'motif' not in line)

df = pd.read_csv('temp.txt',sep='\t|=|;',skiprows=(4),header=None,names=my_cols, engine='python')
df.apply(pd.to_numeric, errors='ignore')
df=df.loc[df['col14'] > 1.7]

df.to_csv('np.txt', sep='\t')

df= pd.read_csv('np.txt',sep='\t',skiprows=(1),header=None,names=my_cols, engine='python')

df=df.sort_values('col4')
bins=np.arange(0,6000000,2000)

ind=np.digitize(df['col4'],bins)

df=df.groupby(ind).size()

df.to_csv(filename+'Meth_NO_motifs_2000grt1_7.txt', sep='\t')

#Below selects rows from output above, based on counts of modificaitons per bin.  Seclection criteria: <>2 St.devs

df = pd.read_csv(filename+'Meth_NO_motifs_2000grt1_7.txt',sep='\t',skiprows=(0),header=None,names=my_cols, engine='python')
print df
df = df.astype(float)

#calc std and mean
std=(df['col2'].std())
mean=(df['col2'].mean())

#calc 2xstd plus/minus
std2xplus=mean+std*2
std2xminus=mean-std*2
print "STD:",std,"MEAN:",mean,"STDx2+:",std2xplus,"STDx2-:",std2xminus

df=df[(df['col2'] >= [std2xplus]) | (df['col2'] <= [std2xminus])]
print df.col2

