# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 15:56:33 2020

@author: Ömer Kaan

Header: Veri Ön İşleme Şablonu_Regression
"""

#kütüphaneler
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

"""
VERİ ÖN İŞLEME
"""

#veri yükleme 
veriler = pd.read_csv("satislar.csv")
print (veriler)

#veri işleme
aylar = veriler[['Aylar']]
print (aylar)
satislar = veriler [['Satislar']]
print(satislar)


#Veri Kümesinin Eğitim ve Test Olarak Bölünmesi

from sklearn.cross_validation import train_test_split 

x_train, x_test, y_train, y_test = train_test_split(aylar,satislar,test_size = 0.33, random_state = 0)
'''
#Öznitelik Ölçeklendirme

from sklearn.preprocessing import StandardScaler 
sc = StandardScaler()

X_test = sc.fit_transform(x_test)
X_train = sc.fit_transform(x_train)
Y_test = sc.fit_transform(y_test)
Y_train = sc.fit_transform(y_train)

'''

#Model İnşası (Linear Regression)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(x_train, y_train)
tahmin = lr.predict(x_test)


#Verilerin Görselleştirmesi

x_train = x_train.sort_index()
y_train = y_train.sort_index()

plt.plot(x_train, y_train)
plt.plot(x_test, tahmin)

plt.title("Aylara Göre Satış")
plt.xlabel("Aylar")
plt.ylabel("Satışlar")








