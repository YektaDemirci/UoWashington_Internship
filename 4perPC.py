# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 12:27:51 2018

@author: Yekta
"""

import csv
import numpy as np
import getpass
userName=getpass.getuser()
import os
try:
    newpath = r"C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/5perPC/"
    os.makedirs(newpath)
except:
    pass

total=[]
count=200
for pep in range(1,13):
    data = list(csv.reader(open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/4pca/pca_data/pcaData"+str(pep)+".csv")))
    data=np.asarray(data)
    data=data.T
    test=len(data)
    if test < count:
        count = test
    total.append(data)

for y in range(0,count):
    new=[]
    for x in range(0,len(total)):
        temp=total[x]
        new.append(temp[y])
        
    with open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/5perPC/PC"+str(y+1)+".csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(new)
    
print("\n For the 1st tensor 4/13 is done")