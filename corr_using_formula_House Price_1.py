
import pandas as pd
import numpy as np
import seaborn as sns
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
    corr = (float)(n*xysum - xsum*ysum)/(float)(math.sqrt((n*xsquaresum-xsum*xsum)*(n*ysquaresum-ysum*ysum)))
    return corr 
#reading the House Price dataset
data = pd.read_csv('D:\ME Cse\PYTHON\correlation\House Price.csv')
#Finding the correlation between YrSold and SalePrice
data1 = data['YrSold'].tolist()
data2 = data['SalePrice'].tolist()
n=len(data1)

print('pearson correlation:%.9f' %correlationcoeff(data1,data2,n))







