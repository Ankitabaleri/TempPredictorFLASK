#Importing Librabries
import pandas as pd
import numpy as np

#Importing DataSet
dataset = pd.read_csv("SunnyRainyDataset.csv")
X=dataset.iloc[:,:-2].values
y=dataset.iloc[:,-2].values

#LabelEncoder and OneHotEncoder
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.externals import joblib
labelencoder=LabelEncoder()
X[:,0]=labelencoder.fit_transform(X[:,0])
joblib.dump(labelencoder,'LabelEncoderCategories')
      
onehotencoder=OneHotEncoder(categorical_features=[0])
X=onehotencoder.fit_transform(X).toarray()
joblib.dump(onehotencoder,'OneHotEncoderCategories')

y=labelencoder.fit_transform(y)
joblib.dump(labelencoder,'LabelEncoderCategoriesY')
#Spliting:
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.10,random_state=1348882)

#ML Model:
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train,Y_train)
joblib.dump(classifier,"MLModelLogisticRegression")