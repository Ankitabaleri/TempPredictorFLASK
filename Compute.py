# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 23:25:44 2019

@author: Nanda Krishna K S
"""
#Importing Librabries
import pandas as pd
import numpy as np
import math
import collections
import matplotlib.pyplot as plt
from sklearn.externals import joblib

#importing dataset
dataset=pd.read_csv("Data.csv")
df=pd.DataFrame(dataset)

#calculating frequency
frequency=collections.Counter(df.iloc[:,-1])

#to find mean and probability
probability=[]
i=0
mean=0
for key,value in frequency.items():
    probability.insert(i,float(value/28))
    mean=mean+probability[i]*key
    i=i+1

#Median
d=dict(zip(frequency.keys(),probability))
median_value=int(d.__len__()/2)
median=list(d.keys())[median_value]

#Mode
mode=list(d.keys())[list(d.values()).index(max(d.values()))]

#Plotting Probability Distribution:
T=np.array(list(frequency.keys()))
power=np.array(probability)
from scipy.interpolate import spline
xnew = np.linspace(T.min(),T.max(),300) 
power_smooth = spline(T,power,xnew)
plt.plot(xnew,power_smooth)
plt.axvline(x=mean,color='red',label='Mean')
plt.title('Probability Distribution Graph')
plt.xlabel('Temperature')
plt.ylabel('Probability Distribution Function')


#to find variance
i=0
var=0
for key,value in frequency.items():
    var=var+((key-mean)**2)*probability[i]
    i=i+1
    
#Standard deviation
sd=math.sqrt(var)



#Probability Application in Machine Learning:
from datetime import datetime
from datetime import timedelta  
week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
sample=np.array([week[datetime.today().weekday()]])

#LabelEncoder and OneHotEncoder
labelencoder=joblib.load('LabelEncoderCategories')
sample=labelencoder.transform(sample)

onehotencoder=joblib.load('OneHotEncoderCategories')
sample=onehotencoder.transform(sample.reshape(1,-1)).toarray()

#Predicting
classifier=joblib.load("MLModelLogisticRegression")
prob=classifier.predict_proba(sample)

        
