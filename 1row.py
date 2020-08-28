# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 18:33:30 2018

@author: Yekta
"""

import csv
import numpy as np
import getpass
userName=getpass.getuser()
import os
try:
    newpath = r"C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/1rowTables/"
    os.makedirs(newpath)
except:
    pass

def lettertonum(lt):
    if lt == 'A':
        return 7
    elif lt == 'R':
        return 8
    elif lt == 'N':
        return 9
    elif lt == 'D':
        return 10
    elif lt == 'C':
        return 11
    elif lt == 'E':
        return 12
    elif lt == 'Q':
        return 13
    elif lt== 'G':
        return 14
    elif lt == 'H':
        return 15
    elif lt == 'I':
        return 16
    elif lt == 'L':
        return 17
    elif lt == 'K':
        return 18
    elif lt == 'M':
        return 19
    elif lt == 'F':
        return 20
    elif lt == 'P':
        return 21
    elif lt == 'S':
        return 22
    elif lt == 'T':
        return 23
    elif lt == 'W':
        return 24
    elif lt == 'Y':
        return 25
    elif lt == 'V':
        return 26
    
    
file_object  = open("C:/Users/"+userName+"/Desktop/propertySelector/peptideLocation.txt", "r")
peptideLocation=file_object.read()

file_object  = open("C:/Users/"+userName+"/Desktop/propertySelector/targetLocation.txt", "r")
targetAndStructural=file_object.read()

file_object  = open("C:/Users/"+userName+"/Desktop/propertySelector/firstPeptideNo.txt", "r")
firstPeptide=file_object.read()

file_object  = open("C:/Users/"+userName+"/Desktop/propertySelector/LastPeptideNo.txt", "r")
lastPeptide=file_object.read()

firstPeptide=int(firstPeptide)

lastPeptide=int(lastPeptide)

length=lastPeptide-firstPeptide

length=length+2

dataFromCSV = list(csv.reader(open(peptideLocation)))
dataFromCSV2 = list(csv.reader(open(targetAndStructural)))

dataFromCSV=np.asarray(dataFromCSV)
dataFromCSV2=np.asarray(dataFromCSV2)

for a in range(1,13):
    matrix=np.empty([np.size(dataFromCSV2,0)-1,length])
    matrix = matrix.astype(np.str)
    for y in range(0,np.size(dataFromCSV2,0)-1):
        matrix[y,0]=y+1
        for x in range(1,length):
            matrix[y,x]=dataFromCSV2[y+1,lettertonum(dataFromCSV[(x+firstPeptide)-1,a+1])]
    with open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/1rowTables/row"+str(a)+".csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(matrix)

print("\n For the 1st tensor 1/13 is done")