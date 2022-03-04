# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 16:30:24 2020

@author: Ömer Kaan

Header: Veri Dönüşümleri
"""

#kütüphaneler
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

#kod bölümü
#veri yükleme 
veriler = pd.read_csv("eksikveriler.csv")
print (veriler)

#veri işleme
boy = veriler[['boy']]
print (boy)
boy_kilo = veriler [['boy','kilo']]
print(boy_kilo)

class insan :
    boy = 180 
    def kosmak(self,b):
        return b + 10
    
ali = insan ()

print (ali.boy)
print (ali.kosmak(10))

#eksik veriler

from sklearn.preprocessing import Imputer

imputer= Imputer(missing_values='NaN', strategy= 'mean', axis= 0)

Yas= veriler.iloc[:,1:4].values

print (Yas)

imputer= imputer.fit(Yas[:,1:4])

Yas[:,1:4]= imputer.transform(Yas[:,1:4])

print (Yas)

#kategorik Veriler

ulke= veriler.iloc[:,0:1].values
cinsiyet= veriler.iloc[:,-1:].values

print (ulke)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
ulke[:,0] = le.fit_transform(ulke[:,0]) 

print (ulke)

from sklearn.preprocessing import OneHotEncoder 
ohe= OneHotEncoder(categorical_features="all")
ulke = ohe.fit_transform(ulke).toarray()
print (ulke)














