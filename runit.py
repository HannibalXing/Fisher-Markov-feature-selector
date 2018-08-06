#!/usr/bin/env python2
# -*- coding: utf-8 -*-




from MFS import Alg

'''

The scipt is based on the Alg.1 of paper ''Fast selecting optimal feature subset for multi-class classification
with applications to high dimensional data'' Q. Cheng, H. Zhou, and J. Cheng, submitted to IEEE Trans. PAMI.


The input data should be .csv file, dataset contains no header index
and the first column is the labels, the rest column is the features of dataset.

written by Xin Xing

'''

filename='data.csv'

#The default gamma is -0.5, user can change gamma value for purposes
gamma=-0.5 

result=Alg(filename, gamma)
print(result)
