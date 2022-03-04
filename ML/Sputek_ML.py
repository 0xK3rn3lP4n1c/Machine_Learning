# -*- coding: utf-8 -*-
"""
SPUTEK Teknoloji Machine Learning For Energy Tracking Systems

Created on Mon Dec 28 16:14:07 2020

@author: Ömer Kaan
"""
#kütüphaneler
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

"""
VERİ ÖN İŞLEME
"""

#veri yükleme 
veriler = pd.read_csv("file:///C:/Users/%C3%96mer%20Kaan/Documents/Makine%20%C3%96%C4%9Frenmesi/Sputek_Degerler.csv")
print (veriler)


#veri işleme
Saat = veriler[['Saat']] #saat verileri
print (Saat)
Voltaj = veriler [['Gerilim']] #saate göre karşılaştırmak istediğimiz veri
print(Voltaj)


#Veri Kümesinin Eğitim ve Test Olarak Bölünmesi

from sklearn.cross_validation import train_test_split 

x_train, x_test, y_train, y_test = train_test_split(Saat,Voltaj,test_size = 0.33, random_state = 0)

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

plt.title("Saate Göre Voltaj Değerleri")
plt.xlabel("Saat")
plt.ylabel("Voltaj")
