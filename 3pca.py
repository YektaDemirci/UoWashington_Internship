# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 17:29:58 2018

@author: Yekta
"""

import csv
import numpy as np
from sklearn.decomposition import PCA
import getpass
userName=getpass.getuser()
import os
try:
    newpath = r"C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/4pca/pca_data"
    os.makedirs(newpath)
    secondpath = r"C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/4pca/pca_loads"
    os.makedirs(secondpath)
    thirdpath = r"C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/4pca/pca_ratios"
    os.makedirs(thirdpath)

    
except:
    pass

tt=[]
for pep in range(1,13):
    data = list(csv.reader(open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/3scaled/scaled"+str(pep)+".csv")))
    data=np.asarray(data)
    data=data.astype(float)
    data2 = data[:,1:]
    
    togo=data2.T
    
    pca = PCA()
    pca.fit(togo)
    pca_data=pca.transform(togo)
    
    per_var=np.round(pca.explained_variance_ratio_*100, decimals=1)
    t=0
    r=0
    for x in (per_var):
        if t < 99:
            t=per_var[r]+t
            r=r+1
        else:
            break
    
    labels = ['PC' +str(x) for x in range(1, r+1)]
    labels=np.asarray(labels)        
        
    pcadata=pca_data[:,:r]
    
    loads=pca.components_[:len(labels),:]
    rt=per_var.tolist()
    rt.append(str(pep))
    tt.append(rt)
    
    with open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/4pca/pca_data/pcaData"+str(pep)+".csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(pcadata)
        
    with open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/4pca/pca_loads/pcaLoad"+str(pep)+".csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(loads)
        
with open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/4pca/pca_ratios/pcaRatios.csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(tt)

print("\n For the 1st tensor 3/13 is done")