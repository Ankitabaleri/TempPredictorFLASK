# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 23:59:04 2019

@author: Nanda Krishna K S
"""

import numpy as np
import pandas as pd

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
print("The probability this weekday being Rainy=" + str(prob[0][0]) +"\nThe probability this weekday being Sunny=" +str(prob[0][1]))