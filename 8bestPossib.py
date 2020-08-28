# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 14:48:39 2018

@author: Yekta
"""

import csv
import numpy as np
import getpass
userName=getpass.getuser()

possibs=[]

for plusser in [6,5,4,3,2]:
    
    data = list(csv.reader(open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/9Possibs/possibles+"+str(plusser)+".csv")))
        
    if len(data) > 1:
        
        possibs.append(data[1])
        
    else:
        
        pass

check = 0
chosen = 0

while check < len(possibs)-1:
        
    count=0
    
    for x in range(0,len(possibs[0])):
        if (possibs[check][x] != possibs[check+1][x]):   
            if (possibs[check+1][x] != ' ') and (possibs[check][x] != ' '):
                count+=1
            else:
                pass
        
        else:
            pass
    
    if count > 3:
        chosen=check
        break
    
    else:
        for x in range(0,len(possibs[0])):
            if possibs[check][x] != ' ':
                possibs[check+1][x] = possibs[check][x]
        check+=1
        chosen=check
        
save=[]
save.append(possibs[chosen])

with open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/9Possibs/chosenPossib.csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(save)
    
print("\n For the 1st tensor 9/13 is done")
