# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 12:38:24 2018

@author: Yekta
"""

import csv
import numpy as np
import getpass
userName=getpass.getuser()


import os
try:
    newpath = r"C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/10Jacobs/"
    os.makedirs(newpath)
except:
    pass

dataFromCSV = list(csv.reader(open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/9Possibs/chosenPossib.csv")))
dataFromCSV = np.asarray(dataFromCSV)


    
bigs=[]

labels=dataFromCSV[0,:]

loc=1

for lab in labels:
#        print(lab)
    if lab == ' ':
        bigs.append([])
        loc+=1
        pass
    else:
        data= list(csv.reader(open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/4pca/pca_loads/pcaLoad"+str(loc)+".csv")))
        prop = list(csv.reader(open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/3scaled/scaled"+str(loc)+".csv")))
        
        data=np.asarray(data)
        prop=np.asarray(prop)
        
        pros=prop[:,0]
        pros=np.reshape(pros,(1,-1))
    
        
        lods=data[int(lab[2:])-1,:]
        lods=np.reshape(lods,(1,-1))
        
        duo=np.append(pros,lods,axis=0)
        duo=duo.T
        duolist=duo.tolist()
        
        bigs.append(duolist)
        loc+=1
    
uzun=[]
for y in range(0,len(bigs)):
    for x in range(0,len(bigs[y])):
        uzun.append(float(bigs[y][x][0]))

mylist = list(set(uzun))
mylist=np.asarray(mylist)
mylist=mylist.astype(int)
mylist=np.sort(mylist)
mylist=mylist.tolist()

matrix = [[999 for x in range(13)] for y in range(len(mylist))]
matrix=np.asarray(matrix)
matrix=matrix.astype(float)


for dum in range(0,len(mylist)):
    matrix[dum,0]=mylist[dum]


for loc in range(1,13):
    rayto=bigs[loc-1]
    rayto=np.asarray(rayto)
    rayto=rayto.astype(float)
    for propert in range(0,len(rayto)):
        inf=np.where(matrix == rayto[propert,0])
        matrix[int(inf[0][0]),loc] = rayto[propert,1]
        
with open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/10Jacobs/Jacobian.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(matrix)
     
###################################################################
import csv
import numpy as np
import getpass
userName=getpass.getuser()       
                         
    
proper=[]
control=[]

data12= list(csv.reader(open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/10Jacobs/Jacobian.csv")))
data12=np.asarray(data12)
data12=data12.astype(float)

for x in range(1,np.size(data12,1)):
    cont=0
    for y in range(0,np.size(data12,0)):
        if data12[y,x] == 999:
            cont+=1
        else:
            break
    if cont == np.size(data12,0):
        data12[:,x]=2000
    

rips=np.where(data12 == float(999))

rip=rips[0]

unq = list(set(rip))

unq=sorted(unq, reverse=True)

for x in unq:
    data12 = np.delete(data12, (x), axis=0)
    
with open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/10Jacobs/JacobianNoBlank.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(data12)
                        
print("\n For the 1st tensor 10/13 is done")
