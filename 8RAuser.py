# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 11:19:23 2018

@author: Yekta
"""

import csv
import numpy as np
import getpass
userName=getpass.getuser()

import os
try:
    newpath = r"C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/9Possibs/"
    os.makedirs(newpath)
except:
    pass

data = list(csv.reader(open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/8trackPC/RA.csv")))

data=np.asarray(data)

for plusser in [2,3,4,5,6]:

    row=0
    cont=0
    possibles=[]
    
    while int(data[row,12]) > plusser:
        sim=int(data[row,12])
        for x in range(0,len(data[row])-1):
            if (data[row,x] !=' ') and cont == 0:
                loc1=x
                cont=1
            elif (data[row,x] !=' ') and cont == 1:
                loc2=x
                cont=0
            else:
                pass
            
        if row == 0:
            matrix = [' ' for x in range(12)]
            matrix[loc1] = data[row,loc1]
            matrix[loc2] = data[row,loc2]
            possibles.append(matrix)
            
        else:
            for pos in range(0,len(possibles)):
                if possibles[pos][loc1] ==  data[row,loc1]:
                    possibles[pos][loc2] = data[row,loc2]
                
                elif possibles[pos][loc2] ==  data[row,loc2]:
                    possibles[pos][loc1] = data[row,loc1]
                    
                else:
                    matrix = [' ' for x in range(12)]
                    matrix[loc1] = data[row,loc1]
                    matrix[loc2] = data[row,loc2]
                    possibles.append(matrix[:])
                    
        boy=len(possibles)
        while boy > 0 :
            check=boy-1
            while check > 0:
                for rax in range(0,len(possibles[boy-1])):
                    if (possibles[boy-1][rax] != ' ') and (possibles[boy-1][rax] == possibles[check-1][rax]):
                        for tax in range(0,len(possibles[boy-1])):
                            if possibles[boy-1][tax] != ' ':
                                possibles[check-1][tax] = possibles[boy-1][tax]
                        del(possibles[boy-1])
                        check=0
                        break
                check=check-1
            boy=boy-1
        
#        print(row)
        row += 1
        
    nums=[1,2,3,4,5,6,7,8,9,10,11,12]
    possibles.insert(0,nums)
    
    with open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/9Possibs/possibles+"+str(plusser)+".csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(possibles)

print("\n For the 1st tensor 8/13 is done")
