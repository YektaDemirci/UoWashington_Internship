# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:13:40 2018

@author: Yekta
"""

import csv
import numpy as np
import getpass
userName=getpass.getuser()


giga=[]
for loc in range(1,13):
    data = list(csv.reader(open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/8trackPC/Loc"+str(loc)+".csv")))
    for x in range(0,len(data)):
        data[x].insert(0, loc)
        data[x][8]=int(data[x][8])
        giga.append(data[x])
    
with open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/8trackPC/GIGA.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(giga)

giga.sort(key=lambda x: x[8])
giga.reverse()

with open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/8trackPC/GIGA2.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(giga)
    
###################################################################
    
dataFromCSV = list(csv.reader(open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/8trackPC/GIGA2.csv")))
dataFromCSV=np.asarray(dataFromCSV)

row=0

while int(dataFromCSV[row,8]) > 1:
    row+=1

matrix = [[' ' for x in range(13)] for y in range(row)]

for x in range(0,row):
    matrix[x][int(dataFromCSV[x,0])-1]='PC'+dataFromCSV[x,2]
    matrix[x][int(dataFromCSV[x,4])-1]='PC'+dataFromCSV[x,6]
    matrix[x][12]=dataFromCSV[x,8]
    
    
with open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/8trackPC/RA.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(matrix)
    
print("\n For the 1st tensor 7/13 is done")

    