# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 16:00:58 2018

@author: Yekta
"""

import csv
import numpy as np
import getpass
userName=getpass.getuser()

import os
try:
    newpath = r"C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/8trackPC/"
    os.makedirs(newpath)
except:
    pass

for loc in range(1,13):
    data = list(csv.reader(open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/7PClabel75/noLoc"+str(loc)+".csv")))
#    print(len(data))
    trackPC=[]
    for pc in range(0,len(data)):
        valuestocheck=data[pc][:]
        
        for otherlocs in range(loc+1,13):
            check = list(csv.reader(open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/7PClabel75/noLoc"+str(otherlocs)+".csv")))
            
            for checkedpcs in range(0,len(check)):
                pcCounter=0
                if len(check[checkedpcs]) == 1 and (check[checkedpcs][0] in ['29','30','37','38','44','157'] ):
#                    print(check[checkedpcs][0])
                    continue
                
                for ind in range(0,len(valuestocheck)):
                
                    for indv in range(0,len(check[checkedpcs])):
                        if valuestocheck[ind] == check[checkedpcs][indv]:
                            pcCounter+=1
                if pcCounter:
                    trackPC.append(["CurrentPC",pc+1,"OtherLoc",otherlocs,"PCchecked",checkedpcs+1,"Similarity",pcCounter])
                    
    with open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/8trackPC/loc"+str(loc)+".csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(trackPC)
        
print("\n For the 1st tensor 6/13 is done")

                        
            
