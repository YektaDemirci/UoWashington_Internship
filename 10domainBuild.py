# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 15:54:03 2018

@author: Yekta
"""


import csv
import numpy as np
from sklearn.cluster import KMeans
import getpass
userName=getpass.getuser()

import os
try:
    newpath = r"C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/11Domains/"
    os.makedirs(newpath)
except:
    pass

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


deneme = list(csv.reader(open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/10Jacobs/JacobianNoblank.csv")))
deneme = np.asarray(deneme)

deneme=deneme.astype(float)    

overall=[]

togo=deneme[:,1:]
    
ind=[]
indsec=[]
for indic in range(0,np.size(togo,1)):
    if togo[0,indic] == 2000:
        ind.append(indic)
    else:
        indsec.append(indic)
    
ind.sort(reverse=True)


sayac=0
for testoo in range(0,np.size(togo,1)):
    if togo[0,testoo] == 2000.0:
        sayac+=1
    else:
        pass

if sayac > 5:
    print("\n There is no PCA implementation for this tensor")

else:
    for y in range(0,len(deneme)):
        
        dom=[]
        
        row1=togo[y,:]
        
        row1=np.reshape(row1,(1,-1))
        
        row4=row1
    
        row1=np.reshape(row1,(-1,1))
        
        row3=np.empty([len(indsec)], dtype=float)
        row3=np.reshape(row3,(1,-1))
        
        for dum in range(0,np.size(row3,1)):                        
            row3[0,dum]=row1[indsec[dum],0]
            
        mini=np.amin(row3)
        row3=row3-mini
        maxa=np.amax(row3)
        row3=row3/maxa
        
        for dum in range(0,len(indsec)):
            row4[0,indsec[dum]]=row3[0,dum]
        
        row2=row1
            
        for blanks in ind:
            row2 = np.delete(row2, (blanks), axis=0)
            
        wcss = []
        for i in range(1, 6):
            kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
            kmeans.fit(row2)
            wcss.append(kmeans.inertia_)
            
    #    plt.plot(range(1, 6), wcss)
    #    plt.title('The Elbow Method')
    #    plt.xlabel('Number of clusters')
    #    plt.ylabel('WCSS')
    #    plt.show()
        
        numb=cluster(wcss)
        
    #    print(numb)
        
        kme = KMeans(n_clusters = numb, init = 'k-means++', random_state = 42)
        clus = kme.fit_predict(row2)
        
        contr=0
        for secon in indsec:
            row1[secon,0]=clus[contr]
            contr+=1
        
        sub=[]
        for ra in range(1,len(row1)):
            if (row1[ra-1] == row1[ra]) and (row1[ra-1]!=2000) and (row1[ra]!=2000):
                sub.append(ra-1)
                sub.append(ra)
            else:
                if sub:
                    guys = list(set(sub))
                    guys.sort()
                    dom.append(guys)
                    sub=[]
                else:
                    pass
        if sub:
            guys = list(set(sub))
            guys.sort()            
            dom.append(guys)
            sub=[]
    
        if dom:
            dom.insert(0,int(float(deneme[y,0])))
                    
            overall.append(dom)
            
    chooo=[]
        
    for y in range(0,len(overall)):
        if len(overall[y]) != 1:
            chooo.append(overall[y])                
            
    with open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/11Domains/chosens.csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(chooo)

print("\n For the 1st tensor 11/13 is done")
