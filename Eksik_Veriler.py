# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 16:30:24 2020

@author: Ömer Kaan

Header: Eksik Veriler (Missing Values)
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





