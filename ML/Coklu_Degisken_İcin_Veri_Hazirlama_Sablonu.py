# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 16:30:24 2020

@author: Ömer Kaan

Header: Verilerin Birleştirilmesi ve Dataframe Oluşturulması
"""

#kütüphaneler
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

#kod bölümü
#veri yükleme 
veriler = pd.read_csv("veriler.csv")
print (veriler)

#kategorik Veriler

ulke= veriler.iloc[:,0:1].values
c= veriler.iloc[:,-1:].values
yas= veriler.iloc[:,1:4].values

print (ulke)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
ulke[:,0] = le.fit_transform(ulke[:,0]) 

print (ulke)

from sklearn.preprocessing import OneHotEncoder 
ohe= OneHotEncoder(categorical_features="all")
ulke = ohe.fit_transform(ulke).toarray()
print (ulke)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
c[:,-1] = le.fit_transform(c[:,-1]) 

print (c)

from sklearn.preprocessing import OneHotEncoder 
ohe= OneHotEncoder(categorical_features="all")
c = ohe.fit_transform(c).toarray()
print (c)

#Verilerin Birleştirilmesi ve Dataframe Oluşturulması

sonuc = pd.DataFrame(data = ulke, index = range(22), columns = ['fr','tr','us'])

print(sonuc)

sonuc2 = pd.DataFrame(data = yas, index = range(22), columns = ['boy','kilo','yas'])

print(sonuc2)

sonuc3 = pd.DataFrame(data = c[::,:1], index = range(22), columns = ['cinsiyet'])

print(sonuc3)

bsonuc = pd.concat([sonuc,sonuc2],axis = 1)
print(bsonuc)

tsonuc = pd.concat([bsonuc,sonuc3],axis = 1)
print(tsonuc)

#Veri Kümesinin Eğitim ve Test Olarak Bölünmesi

from sklearn.cross_validation import train_test_split 

x_train, x_test, y_train, y_test = train_test_split(bsonuc,sonuc3,test_size = 0.33, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

b = bsonuc.iloc[:,-3:4].values
print(b)

sol = bsonuc.iloc[:,:3]
sag = bsonuc.iloc[:,4:]

veri = pd.concat([sol,sag],axis=1)

x_2train, x_2test, y_2train, y_2test = train_test_split(veri,b,test_size = 0.33, random_state = 0)

regressor2 = LinearRegression()
regressor2.fit(x_2train, y_2train)

y_2pred = regressor2.predict(x_2test)







