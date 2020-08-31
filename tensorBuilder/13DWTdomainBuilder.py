# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 13:02:05 2018

@author: Yekta
"""


'''Go to the very bottom'''

import csv
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

import getpass
userName=getpass.getuser()

import os
try:
    newpath = r"C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/14DWTdomains/"
    os.makedirs(newpath)
except:
    pass
    
deneme = list(csv.reader(open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/13DWT/yekta.csv")))
deneme = np.asarray(deneme)

deneme=deneme.astype(float)    

overall=[]

def cluster(wcss=[]):
    ratios=[]
    falls=[]
    for x in range(0,len(wcss)):
        ratios.append(wcss[x]/wcss[0])
    
    for y in range(0,len(wcss)-1):
        if ratios[y]-ratios[y+1] > 0.1:
            falls.append(ratios[y]-ratios[y+1])
    
    if falls and max(falls) > 0.3:
        return len(falls)+1
    else:
        return 0


for y in range(0,len(deneme)):
    
    dom=[]
    
    dom.append(y+1)
    
    row1=deneme[y,:]
    
    row1=np.reshape(row1,(-1,1))

        
    wcss = []
    for i in range(1, 10):
        kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
        kmeans.fit(row1)
        wcss.append(kmeans.inertia_)
        
#    plt.plot(range(1, 10), wcss)
#    plt.title('The Elbow Method')
#    plt.xlabel('Number of clusters')
#    plt.ylabel('WCSS')
#    plt.show()
    
    numb=cluster(wcss)
    
#    print(numb)
    
    kme = KMeans(n_clusters = numb, init = 'k-means++', random_state = 42)
    clus = kme.fit_predict(row1)
    
    sub=[]
    for ra in range(1,len(clus)):
        if clus[ra-1] == clus[ra]:
            sub.append(ra-1)
            sub.append(ra)
        else:
            if sub:
                guys = list(set(sub))
                dom.append(guys)
                sub=[]
            else:
                pass
    if sub:
        guys = list(set(sub))
        dom.append(guys)
        sub=[]

    
    overall.append(dom)

with open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/14DWTdomains/chosens.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(overall)

print("\n For the 1st tensor 13/13 is done")
