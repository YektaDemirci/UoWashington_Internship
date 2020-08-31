# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 18:19:37 2018

@author: Yekta
"""
import math
import csv
import numpy as np
import pywt
from pywt import wavedec
import getpass
userName=getpass.getuser()

import os
try:
    newpath = r"C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/13DWT/"
    os.makedirs(newpath)
except:
    pass

yekta=[]

for pep in range(1,13):

    app=[]
    data=list(csv.reader(open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/1rowTables/row"+str(pep)+".csv")))
    data=np.asarray(data)
    touse=data[:,1:]
    touse=touse.astype(float)
    
    for x in range(0,len(touse)):
        
#        liste=[1.1] * 64
#        liste[2:62]=touse[x,:]
#        liste[0:2]=touse[x,58:]
#        liste[62:]=touse[x,0:2]
#        liste=np.asarray(liste)
        
        liste=touse[x,:]
        liste=np.reshape(liste,(1,-1))
        number=math.log(np.size(liste,1),2)
        number=int(number)

        coeffs = wavedec(liste, 'haar', mode='periodic', level=number)
        
        number2=int(math.log(np.size(coeffs[0],1),2))
        
        coeffFin = wavedec(coeffs[0], 'haar', mode='periodic', level=number2)
        
        approx=coeffFin[0].tolist()
        
        app.append(approx[0][0])
    
    yekta.append(app)
    
yekta=np.asarray(yekta)

yekta=yekta.T

with open("C:/Users/"+userName+"/Desktop/propertySelector/1st/527x60/13DWT/yekta.csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(yekta)
        
print("\n For the 1st tensor 12/13 is done")

    
    
         
        

    