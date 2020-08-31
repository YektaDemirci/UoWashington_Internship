# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 11:24:17 2018

@author: Yekta
************************************************
***************NOTE  23/12/2018*****************
************************************************
************************************************
In this script, linear models are trained with 
coefficients from self implemented mexican hat sor of wavelet transform
R^2 values converge to 0.35, slightly worse than Haar Transform.
Regresion is trained 30 times with different randomization,
Mean of R^2 values from 30 iteration is returned from regressor
function as the obtained R^2 value.
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
def matrixfiller(value,letter,tempMatrix):
    numpyMatrix=np.asarray(tempMatrix)
    index = np.where(numpyMatrix==letter)    
    for AAs in range(0,np.size(index[0],0)):
        tempMatrix [index[0][AAs]] [1] [index[2][AAs]] = value
        
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
    a0 = np.array([1/math.sqrt(18),1/math.sqrt(18),1/math.sqrt(18),2/math.sqrt(18),2/math.sqrt(18),2/math.sqrt(18),1/math.sqrt(18),1/math.sqrt(18),1/math.sqrt(18)])
    d1 = np.array([-1/math.sqrt(18),-1/math.sqrt(18),1/math.sqrt(18),2/math.sqrt(18),2/math.sqrt(18),2/math.sqrt(18),-1/math.sqrt(18),-1/math.sqrt(18),-1/math.sqrt(18)])
    d21= np.array([-1/math.sqrt(6),2/math.sqrt(6),-1/math.sqrt(6),0,0,0,0,0,0])
    d22= np.array([0,0,0,-1/math.sqrt(6),2/math.sqrt(6),-1/math.sqrt(6),0,0,0])
    d23= np.array([0,0,0,0,0,0,-1/math.sqrt(6),2/math.sqrt(6),-1/math.sqrt(6)])
    for noPeptide in range(0,numberOfPep):
        temp=[]
        temp1 = np.multiply(a0,dummymatrix[noPeptide][1])
        temp2 = np.multiply(d1,dummymatrix[noPeptide][1])
        temp3 = np.multiply(d21,dummymatrix[noPeptide][1])
        temp4 = np.multiply(d22,dummymatrix[noPeptide][1])
        temp5 = np.multiply(d23,dummymatrix[noPeptide][1])
        temp.append(np.sum(temp1))
        temp.append(np.sum(temp2))
        temp.append(np.sum(temp3))
        temp.append(np.sum(temp4))
        temp.append(np.sum(temp5))
        matrixWavelet.append(temp)
       
    matrixWavelet=np.asarray(matrixWavelet)
    return matrixWavelet


data = list(csv.reader(open("data.csv")))

numberOfPep=len(data)
lengthOfSeq=9

matrix=[]
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
    matrix.append([[0 for i in range(lengthOfSeq)] for j in range(2)])
    matrix[noPeptide][0][:]=data[noPeptide][:-1]
    
    y.append(float(data[noPeptide][9]))
    
y=np.asarray(y)

'''
aminoAcids is the reference dataframe
It is KxM sized matrix where
K(row) is 3, first row shows the amino acid letter,second row shows the value for an amino acid
and the third row shows how many times an amino acid occured in the overall input
'''
aminoAcids=[]
aminoAcids.append(['A','R','N','D','C','E','Q','G','H','I','L','K','M','F','P','S','T','W','Y','V'])
aminoAcids.append([round(random.uniform(-1, 1),2) for i in range(20)])
aminoAcids.append([0 for i in range(20)])

'''
This for loop is very similar to matrixfiller function
It is used for the inial matrix filling
It fills the matrix dataframe by using randomly created aminoAcid values
It also finds how many times an amino acid occured in the overallinput
'''
matrixNP=np.asarray(matrix)
for noAA in range(0,20):
    index = np.where(matrixNP==aminoAcids[0][noAA])
    aminoAcids[2][noAA]=np.size(index[0],0)
    
    for AAs in range(0,np.size(index[0],0)):
        matrix [index[0][AAs]] [1] [index[2][AAs]] =aminoAcids[1][noAA] 
del matrixNP
del index

'''
Most occured amino acid is found below and aminoAcids dataframe is sorted according to it
'''

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
            
            threshold = 2
            currentValue=aminoAcids[1][noAA]
            currentLetter=aminoAcids[0][noAA]
            
            while threshold > 0.2:    
                
                tempMatrix=matrixfiller(currentValue,currentLetter,copy.deepcopy(matrix))
                currentWaveletCoeffs=wavelet(numberOfPep,tempMatrix)
                currentR2=regressor(currentWaveletCoeffs,y)
                
                highMatrix=matrixfiller(currentValue+threshold,currentLetter,copy.deepcopy(matrix))
                highWaveletCoeffs=wavelet(numberOfPep,highMatrix)
                highR2=regressor(highWaveletCoeffs,y)
                
                lowMatrix=matrixfiller(currentValue-threshold,currentLetter,copy.deepcopy(matrix))
                lowWaveletCoeffs=wavelet(numberOfPep,lowMatrix)
                lowR2=regressor(lowWaveletCoeffs,y)
                
#                print("Low R2 ",lowR2," Current R2 ",currentR2," High R2 ",highR2)
                
                if ((currentR2 >= lowR2) and (currentR2 >= highR2)):
                    threshold = threshold - 0.2
                    if threshold < 0.1:
                        finalR2values.append(currentR2)
                elif ((lowR2 >= currentR2) and (lowR2 >= highR2)):
                    currentValue = currentValue - threshold
                elif ((highR2 >= currentR2) and (highR2 >= lowR2)):
                    currentValue = currentValue + threshold
    
            matrix = matrixfiller(currentValue,currentLetter,copy.deepcopy(matrix))
            aminoAcids[1][noAA] = currentValue
                            
        else:
            pass
        
        print(noAA)
        
    print((sum(finalR2values) / float(len(finalR2values))))
 
with open("C:/Users/"+userName+"/Desktop/BerkHoca/Results/0.35yesApprox.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(aminoAcids) 
#del lowMatrix
#del lowR2
#del lowWaveletCoeffs
#del highMatrix
#del highR2
#del highWaveletCoeffs
#del currentWaveletCoeffs
#del currentR2
