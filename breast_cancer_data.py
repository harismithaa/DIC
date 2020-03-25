import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.datasets import load_breast_cancer

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
#Loading the breast cancer dataset
data = load_breast_cancer()

#correlation between tumour-size and target
data1 = data.data[:,2].tolist()
data2 = data.target.tolist()
n=len(data1)

#correlation
print('correlation , r :%.9f' %correlationcoeff(data1,data2,n))

#without using formula
from scipy.stats import pearsonr
corr,_ = pearsonr(data1,data2)
print('pearson correlation:%.6f'% corr)

from scipy.stats import spearmanr
corr,_ = spearmanr(data1,data2)
print('spearman correlation:%.6f'% corr)