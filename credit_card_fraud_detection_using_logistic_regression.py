# -*- coding: utf-8 -*-
"""Credit Card Fraud Detection using Logistic Regression

Author @Himesh

Original file is located at
    https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
data= pd.read_csv('/content/drive/MyDrive/creditcard.csv')
df=pd.DataFrame(data)
df.head()
df['Class'].value_counts()
df.groupby('Class').mean()
legit=df[df.Class==0]
fraud=df[df.Class==1]


new_legit=legit.sample(n=492)
new_data=pd.concat([new_legit,fraud],axis=0)
new_data.head()
new_data['Class'].value_counts()


x=df.drop('Class',axis=1)
y=df['Class']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model=LogisticRegression()
model.fit(x_train,y_train)
x_train_pred=model.predict(x_train)
train_acc=accuracy_score(x_train_pred,y_train)
print("Accuracy of training:",train_acc)
x_test_pred=model.predict(x_test)
test_acc=accuracy_score(x_test_pred,y_test)
print("Accuracy of Testing:",test_acc)

