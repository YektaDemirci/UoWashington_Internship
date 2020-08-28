# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 11:45:13 2018

@author: Yekta
"""
import csv
import numpy as np
import getpass
userName=getpass.getuser()

import os
try:
    newpath = r"C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/7PClabel75/noLoc/"
    os.makedirs(newpath)
except:
    pass


file_object  = open("C:/Users/"+userName+"/Desktop/propertySelector/targetLocation.txt", "r")
targetLoc=file_object.read()
datafromCSV= list(csv.reader(open(targetLoc)))


for loc in range(1,13):
    propnos=[]
    properties=[]
    propertygroups=[]
    prop = list(csv.reader(open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/3scaled/scaled"+str(loc)+".csv")))
    data = list(csv.reader(open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/4pca/pca_loads/pcaLoad"+str(loc)+".csv")))
    data=np.asarray(data)
    prop=np.asarray(prop)
    props=prop[:,0]
    props=np.reshape(props,(1,-1))
    props=props.astype(float)
    data=data.astype(float)
    
    totalpc=len(data)
    
    for pc in range(0,totalpc):
        
        temp=data[pc,:]
        temp=np.reshape(temp,(1,-1))
        temp=abs(temp)
        temp=np.round_(temp, decimals=7)
        comb=np.append(props,temp,axis=0)
        
        sor=np.sort(temp)
        
        sortedlads=[]
        for x in range(0,len(sor[0])):
            indice=np.where(comb==sor[0,x])
            sortedlads.append(comb[:,indice[1][0]])
        sortedlads=np.asarray(sortedlads)
        sortedlads=sortedlads.T
        
        
        numb=[]
        amax=np.amax(sor)
        ratio=sor[0]/amax
        first=1
        for nu in range(1,np.size(sor,1)+1):
            numb.append(nu)
            if ratio[nu-1] > 0.75 and first == 1:
                indic=nu-1
                first=0
#        print(ratio[indic:])
#        numb=np.asarray(numb)
#        numb=np.reshape(numb,(1,-1))
#        numb=numb.tolist()
#        numb=numb[0]
#        soka=sor.tolist()
#        soka=soka[0]
#        plt.plot(numb,soka)
#        plt.show()
                
        final=sortedlads[:,indic:]
        final=final.T
        
        ra=final.tolist()
        ra=ra[::-1]
        ra=np.asarray(ra)
        
        perpc=[]
        
        for picc in range(0,len(ra)):
            perpc.append(datafromCSV[int(ra[picc,0])][28]+str(00000)+str(int(ra[picc,0])))
        
        properties.append(perpc)


        groups=[]

        for picc in range(0,len(ra)):
            groups.append(datafromCSV[int(ra[picc,0])][2]+datafromCSV[int(ra[picc,0])][4])
        
        propertygroups.append(groups)
        
        nos=[]
        
        for picc in range(0,len(ra)):
            nos.append(str(int(ra[picc,0])))
            
        propnos.append(nos)
        
        
        
        
        
#    with open("C:/Users/"+userName+"/Desktop/veryFinal/1st/527x60/7PClabel75/loc"+str(loc)+".csv", 'w', newline='') as myfile:
#        wr = csv.writer(myfile)
#        wr.writerows(properties)
#        
#    with open("C:/Users/"+userName+"/Desktop/veryFinal/1st/527x60/7PClabel75/GroupWayloc"+str(loc)+".csv", 'w', newline='') as myfile:
#        wr = csv.writer(myfile)
#        wr.writerows(propertygroups)
        
    with open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/7PClabel75/noLoc"+str(loc)+".csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(propnos)
        
print("\n For the 1st tensor 5/13 is done")
