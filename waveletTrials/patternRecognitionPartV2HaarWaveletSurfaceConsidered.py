# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 11:24:17 2018

@author: Yekta
************************************************
***************NOTE  23/12/2018*****************
************************************************
************************************************
Linear models are trained with coefficients from
level 6 Haar wavelet coefs.
Surface area is considered.
0s padded to the right ends so the border effect
is high. Padding should be optimized. 
R^2 values are super low
************************************************
************************************************
************************************************
"""
import csv
import pywt
import random
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import getpass
import copy
import math

userName=getpass.getuser()

'''
regressor function does the simple linear regression.
Input data is divided into test and training by 1/3 ratio
cv in the for loop represents cross-validation
30 iterated cross-validation is done and the average R^2 value is returned
'''
def regressor(X,y):
    crossValidate=[]
    for cv in range(0,30):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3)
        reg = LinearRegression()
        reg.fit(X_train, y_train)
        y_pred = reg.predict(X_test)
        rScore=r2_score(y_test, y_pred)
        crossValidate.append(rScore)
#    print(crossValidate)
#    print(sum(crossValidate) / float(len(crossValidate)))
    return (sum(crossValidate) / float(len(crossValidate)))

'''
matrixfiller function changes value of a letter in the overall matrix
Once numerical value of a letter is changed,this function updates the matrix
'''
def matrixfiller(current,value,letter,tempMatrix):
    if (current == 0) or (value == 0):
        print("FATAL FAIL")
    numpyMatrix=np.asarray(tempMatrix)
    index = np.where(numpyMatrix==current)    
    for AAs in range(0,np.size(index[0],0)):
        tempMatrix [index[0][AAs]] [index[1][AAs]] = value
        
    return tempMatrix

'''
wavelet function takes the matrix as input and finds wavelet coefficients of each peptide
Single level discrete wavelet is used.
Wavelet function is haar, padding symmetric(Actually padding does not matter in GrBP case since mod2(GrBPseqLength)==0 and single level dwt is used)
Approximations and details coefficients are linked
Each row represents a peptide
###############################################################
*****If only the detail coefficients are used the R^2 values are slightly better****

'''
def wavelet(numberOfPep,dummymatrix):
    matrixWavelet=[]
    for noPeptide in range(0,numberOfPep):
       temp=[]
       coeffs=pywt.wavedec(dummymatrix[noPeptide][:],'haar',mode='symmetric',level=6)
       for xa in range(0,len(coeffs)):
           for ya in range(0,len(coeffs[xa])):
               temp.append(coeffs[xa][ya])
               
       matrixWavelet.append(temp)
       
    matrixWavelet=np.asarray(matrixWavelet)
    return matrixWavelet


data = list(csv.reader(open("data.csv")))

numberOfPep=len(data)
lengthOfSeq=9

#matrix=[]
y=[]


'''
matrix is the main dataframe
It is constructed according to input data
It is KxMxN sized matrix where
K is the total peptide number
M is 2 which shows Amino Acids of a peptide and its values
N is the length of peptide sequences(12 in GrBP case)
#####################################################
y is the target property for linear regression
It is binding affinity in GrBP case
y is also obtained in the below for loop but it is not related with matrix
'''

for noPeptide in range(0,numberOfPep):
#    matrix.append([[0 for i in range(lengthOfSeq)] for j in range(1)])
#    matrix[noPeptide][0][:]=data[noPeptide][:-1]
    y.append(float(data[noPeptide][9]))
    
y=np.asarray(y)

'''
aminoAcids is the reference dataframe
It is KxM sized matrix where
K(row) is 3, first row shows the amino acid letter,second row shows the value for an amino acid
and the third row shows how many times an amino acid occured in the overall input
'''
aminoAcids=[]
aminoAcids.append(['A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V'])
aminoAcids.append([round(random.uniform(-1, 1),2) for i in range(20)])
aminoAcids.append([0 for i in range(20)])
surface=np.array([115, 225, 160, 150, 135, 190, 180,  75, 195, 175, 170, 200, 185, 210, 145, 115, 140, 255, 230, 155])/75*2
surface=np.round(surface)
surface=surface.astype(int)
aminoAcids.append(surface.tolist())
del surface

'''
This for loop is very similar to matrixfiller function
It is used for the inial matrix filling
It fills the matrix dataframe by using randomly created aminoAcid values
It also finds how many times an amino acid occured in the overallinput
'''
#matrixNP=np.asarray(matrix)
#for noAA in range(0,20):
#    index = np.where(matrixNP==aminoAcids[0][noAA])
#    aminoAcids[2][noAA]=np.size(index[0],0)
#    
#    for AAs in range(0,np.size(index[0],0)):
#        matrix [index[0][AAs]] [1] [index[2][AAs]] =aminoAcids[1][noAA]
#del matrixNP
#del index
matrix1=[]
matrix2=[]
forNumb=0
index=1
for xx in range(0,numberOfPep):
    temps=[]
    temp2=[]
    temp3=[]
    for yy in range(0,lengthOfSeq):
        if data[xx][yy] == 'A':
            forNumb=aminoAcids[3][0]
            index=0
            temp2.append('A')
        elif data[xx][yy] == 'R':
            forNumb=aminoAcids[3][1]
            index=1
            temp2.append('R')
        elif data[xx][yy] == 'N':
            forNumb=aminoAcids[3][2]
            index=2
            temp2.append('N')
        elif data[xx][yy] == 'D':
            forNumb=aminoAcids[3][3]
            index=3
            temp2.append('D')
        elif data[xx][yy] == 'C':
            forNumb=aminoAcids[3][4]
            index=4
            temp2.append('C')
        elif data[xx][yy] == 'E':
            forNumb=aminoAcids[3][5]
            index=5
            temp2.append('E')
        elif data[xx][yy] == 'Q':
            forNumb=aminoAcids[3][6]
            index=6
            temp2.append('Q')
        elif data[xx][yy] == 'G':
            forNumb=aminoAcids[3][7]
            index=7
            temp2.append('G')
        elif data[xx][yy] == 'H':
            forNumb=aminoAcids[3][8]
            index=8
            temp2.append('H')
        elif data[xx][yy] == 'I':
            forNumb=aminoAcids[3][9]
            index=9
            temp2.append('I')
        elif data[xx][yy] == 'L':
            forNumb=aminoAcids[3][10]
            index=10
            temp2.append('L')
        elif data[xx][yy] == 'K':
            forNumb=aminoAcids[3][11]
            index=11
            temp2.append('K')
        elif data[xx][yy] == 'M':
            forNumb=aminoAcids[3][12]
            index=12
            temp2.append('M')
        elif data[xx][yy] == 'F':
            forNumb=aminoAcids[3][13]
            index=13
            temp2.append('F')
        elif data[xx][yy] == 'P':
            forNumb=aminoAcids[3][14]
            index=14
            temp2.append('P')
        elif data[xx][yy] == 'S':
            forNumb=aminoAcids[3][15]
            index=15
            temp2.append('S')
        elif data[xx][yy] == 'T':
            forNumb=aminoAcids[3][16]
            index=16
            temp2.append('T')
        elif data[xx][yy] == 'W':
            forNumb=aminoAcids[3][17]
            index=17
            temp2.append('W')
        elif data[xx][yy] == 'Y':
            forNumb=aminoAcids[3][18]
            index=18
            temp2.append('Y')
        elif data[xx][yy] == 'V':
            forNumb=aminoAcids[3][19]
            index=19
            temp2.append('V')
        for z in range(0,forNumb):
            temp3.append(aminoAcids[1][index])
    while len(temp3)<64:
        temp3.append(0)   
    matrix1.append(temp2)
    matrix2.append(temp3)
del xx
del yy
del z
del temp2
del temp3
del temps
'''
Most occured amino acid is found below and aminoAcids dataframe is sorted according to it
'''
matrixNP=np.asarray(data)
for noAA in range(0,20):
    index = np.where(matrixNP==aminoAcids[0][noAA])
    aminoAcids[2][noAA]=np.size(index[0],0)
del matrixNP

transposed=[*map(list, zip(*aminoAcids))]
transposed.sort(key=lambda x: x[2], reverse=True)
aminoAcids = [*map(list, zip(*transposed))]
del transposed


'''
finalR2values show the final R^2 value per aminoAcid to check if the results are reliable
'''        
finalR2values=[-1]
'''
The for loop below is the main algorithm
There is an if statement which checks if an amino acid occurs in an overall input
Then optimization starts for the amino acid which occurs the most
R^2 value is found for (a value,value+threshold,value-threshold)
According to R^2 result, value and threshold are optimized
If the current value gives the best R^2 value,then threshold is decreased by 0.05
If current value+-threshold gives better R^2 value the current value is updated
'''
#This 0.5 can be changed it is kind of a dummy number just to make loop go on
while (sum(finalR2values) / float(len(finalR2values))) <= 0.5 :

    finalR2values=[]

    for noAA in range(0,20):
        
        if aminoAcids[2][noAA] > 0:
            
            threshold = 1.501
            currentValue=aminoAcids[1][noAA]
            currentLetter=aminoAcids[0][noAA]
            
            while threshold > 0.:    
                
                tempMatrix=matrixfiller(currentValue,currentValue,currentLetter,copy.deepcopy(matrix2))
                currentWaveletCoeffs=wavelet(numberOfPep,tempMatrix)
                currentR2=regressor(currentWaveletCoeffs,y)
                
                highMatrix=matrixfiller(currentValue,currentValue+threshold,currentLetter,copy.deepcopy(matrix2))
                highWaveletCoeffs=wavelet(numberOfPep,highMatrix)
                highR2=regressor(highWaveletCoeffs,y)
                
                lowMatrix=matrixfiller(currentValue,currentValue-threshold,currentLetter,copy.deepcopy(matrix2))
                lowWaveletCoeffs=wavelet(numberOfPep,lowMatrix)
                lowR2=regressor(lowWaveletCoeffs,y)
                
#                print("Low R2 ",lowR2," Current R2 ",currentR2," High R2 ",highR2)
                
                if ((currentR2 >= lowR2) and (currentR2 >= highR2)):
                    threshold = threshold - 0.251
                    if threshold < 0.251:
                        finalR2values.append(currentR2)
                elif ((lowR2 >= currentR2) and (lowR2 >= highR2)):
                    currentValue = currentValue - threshold
                elif ((highR2 >= currentR2) and (highR2 >= lowR2)):
                    currentValue = currentValue + threshold
    
            matrix2 = matrixfiller(currentValue,currentValue,currentLetter,copy.deepcopy(matrix2))
            aminoAcids[1][noAA] = currentValue
                            
        else:
            pass
        
        print(noAA)
        
    print(finalR2values)
 
#with open("C:/Users/"+userName+"/Desktop/BerkHoca/Results/gg.csv", 'w', newline='') as myfile:
#    wr = csv.writer(myfile)
#    wr.writerows(aminoAcids) 
#del lowMatrix
#del lowR2
#del lowWaveletCoeffs
#del highMatrix
#del highR2
#del highWaveletCoeffs
#del currentWaveletCoeffs
#del currentR2
