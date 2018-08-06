
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 21:58:04 2018

@author: XIN
"""

import matplotlib.pyplot as plt


from scipy import interp
import numpy as np
import pandas as pd
from sklearn import datasets

'''

'''
def Alg(filename,gamma):
    #read the input data
    data=pd.read_csv(filename,header=None)

    #Total data
    #get the feature data without the labels
    
    Data=pd.DataFrame.as_matrix(data)
    X=Data[:,1:]
    
    #get the labels and number of classes of dataset
    y=Data[:,0]
    GroupNum=len(set(y))

    #TotalNum is the whole number of the dataset
    #Totalfeature is the total feature of the dataset
    TotalNum, TotalFeature= X.shape

    #We want to divide the whole data set into each class group
    Individual_Group={}
    Individual_Group_Num={}

    for i in range(GroupNum):
        Individual_Group[i+1]=Data[Data[:,0]==(i+1)]
        Individual_Group[i+1]=Individual_Group[i+1][:,1:]
        Individual_Group_Num[i+1]=Individual_Group[i+1].shape[0]
    


    theta=[]

#To calculate the theta j :

    for j in range(0, TotalFeature):
        second_step=0 
        third_step=0
        first_step_sum=0
        first_step=np.zeros(GroupNum)
    
        for i in range (0, TotalNum):
            second_step=second_step+X[i,j]*X[i,j]
        
        for u in range(0, TotalNum):
            for v in range(0, TotalNum):
                third_step=third_step+X[u,j]*X[v,j]
            
            for k in range(GroupNum):
                Train=Individual_Group[k+1]
                classNum=Individual_Group_Num[k+1]
                for u in range(0, classNum):
                    for v in range(0, classNum):
                        first_step[k]=first_step[k]+Train[u,j]*Train[v,j]
                first_step[k]=first_step[k]*1/classNum
    
        for k in range(GroupNum):    
            first_step_sum=first_step_sum+first_step[k]
        
        theta.append(1.0/TotalNum*first_step_sum +(-gamma/TotalNum)*second_step+(gamma-1.0)/(TotalNum*TotalNum)*third_step)
    return theta      
     
       