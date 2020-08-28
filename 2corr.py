# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 17:07:32 2018

@author: Yekta
"""

import csv
import numpy as np
import getpass
userName=getpass.getuser()
import warnings
warnings.simplefilter('error', RuntimeWarning)
import os
try:
    newpath = r"C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/2corr"
    os.makedirs(newpath)
    secondpath = r"C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/3scaled"
    os.makedirs(secondpath)
except:
    pass


for bac in range (1,13):
    data = list(csv.reader(open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/1rowTables/row"+str(bac)+".csv")))
    array4 = np.asarray(data)
    array4 = array4.astype(float)
    array3 = array4[:,1:]
    
    thrown=[]
            
    for ok in range(0,np.size(array3,0)):
        con=array3[ok,0]
        count=0
        for rok in range(1,np.size(array3,1)):
            if array3[ok,rok] == con:
                count=count+1
        if count == np.size(array3,1)-1:
            thrown.append(ok+1)
    
    thrown=sorted(thrown, reverse=True)
    
    if thrown:
        for x in thrown:
            array3 = np.delete(array3, (x-1), axis=0)
            array4 = np.delete(array4, (x-1), axis=0)
    
    array=np.corrcoef(array3)
    
    
    a=0
    
    matrixtest = [[0 for x in range(np.size(array,0))] for y in range(np.size(array,0))]
    t=0
    qq=[]
    
    while(a<=np.size(array,0)-1):
        for x in array[a+1:,a]:
            if(abs(x)>0.9):
                qq.append([t+1,a])
            matrixtest[t+1][a]=x
            t=t+1
        a=a+1
        t=a
        
    if qq:
        qq=np.asarray(qq)
        matrixtest=np.asarray(matrixtest)
        
        qq2=qq[:,0]
        mylist=qq2.tolist()
        used = set()
        unique = [x for x in mylist if x not in used and (used.add(x) or True)]
        unique=sorted(unique, reverse=True)
        
        
        
        
        for x in unique:
            thrown.append(array4[x,0])
            array4 = np.delete(array4, (x), axis=0)
            
        with open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/2corr/thrownPropsFor"+str(bac)+".csv", 'w', newline='') as myfile:
            wr = csv.writer(myfile)
            wr.writerows(map(lambda y: [y], thrown))
        
    with open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/2corr/reduced"+str(bac)+".csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(array4)
        
        
    for y in range(0,np.size(array4,0)):
        mean=np.mean(array4[y,1:])
        array4[y,1:]=array4[y,1:]-mean
        mini=np.amin(array4[y,1:])
        maxa=np.amax(array4[y,1:])
        leng=2/(maxa-mini)
        for z in range(1,np.size(array4,1)):
            if array4[y,z] == mini:
                array4[y,z] = -1
            else:
                array4[y,z]=((array4[y,z]-mini)*leng)-1
                
    with open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/3scaled/scaled"+str(bac)+".csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(array4)
        
print("\n For the 1st tensor 2/13 is done")