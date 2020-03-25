#prediction of mental ability - using formula

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

def correlationcoeff(x,y,n):
    xsum=0
    ysum=0
    xysum=0
    xsquaresum=0
    ysquaresum=0
    i=0
    while i<n:
        xsum=xsum+x[i]
        ysum=ysum+y[i]
        xysum=xysum+x[i]*y[i]
        xsquaresum=xsquaresum+x[i]*x[i]
        ysquaresum=ysquaresum+y[i]*y[i]
        i=i+1
    #formula for correlation
    corr = (float)(n*xysum - xsum*ysum)/(float)(math.sqrt((n*xsquaresum-xsum*xsum)*(n*ysquaresum-ysum*ysum)))
    return corr 

#Loading the dataset
data = pd.read_csv('D:\ME Cse\PYTHON\mentalability.csv')
data2 =data['NewScore(Score+21)'].tolist()
data1 = data['Age  (x)'].tolist()
n=len(data1)

#calculation of correlation
print('Correlation r :%.9f' %correlationcoeff(data1,data2,n))

#scatter plot age vs newscore
data.plot(kind='scatter',x='Age  (x)',y='NewScore(Score+21)')

#predicting mental ability - without using formula

from scipy.stats import pearsonr
from scipy.stats import spearmanr

corrp,_ = pearsonr(data1,data2)
corrs,_ = spearmanr(data1,data2)

print('Pearson Correlation  :%.6f'% corrp)
print('spearman Correlation  :%.6f'% corrp)

#correlation matrix

data.corr()