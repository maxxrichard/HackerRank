# Enter your code here. Read input from STDIN. Print output to STDOUT

#importing libraries
import pandas as pd
import numpy as np 
import re

#initializing variables
n = int(input().strip())
col = list(input().split())
data = list()
missing = list()

#input data
for _ in range(n):
    row = list(input().split())
    data.append(row)
    
df = pd.DataFrame(data, columns = col)

#converting string to nan
df_tmax = df['tmax'].replace(to_replace = "^Missing",value = np.nan, regex = True)
df_tmin = df['tmin'].replace(to_replace = "^Missing",value = np.nan, regex = True)

#converting into float datatype
df_tmax_f = pd.DataFrame(df_tmax, dtype = 'float32')
df_tmin_f = pd.DataFrame(df_tmin, dtype = 'float32')

#applying spline interpolation
tmax = df_tmax_f.reset_index(drop=True).interpolate(method='spline', order=2)
tmin = df_tmin_f.reset_index(drop=True).interpolate(method='spline', order=2)

#checking for nan
a = pd.isna(df_tmax)
b = pd.isna(df_tmin)

#getting index for nan
for i in range(len(df_tmax)):
    if a[i] == True: missing.append(tmax['tmax'][i])
    elif b[i] == True: missing.append(tmin['tmin'][i])

#printing the output
for i in missing:
    print(round(i,1))
    
