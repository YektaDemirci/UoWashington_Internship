# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 21:16:20 2018

@author: Yekta
"""

import numpy as np
import math
import csv

f = open('bdata.20130222.mhci.txt', 'r')
dataC=[]

for line in f:
    columns = line.split()
    if ((columns[0]=='human') and (columns[1]=='HLA-A*02:01') and columns[2]=='9'):
        temp=[]
        for x in range(0,9):
            temp.append(columns[3][x])
        temp.append(-10*(math.log(float(columns[5]),10)))
        dataC.append(temp)
        
with open("data.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(dataC)
