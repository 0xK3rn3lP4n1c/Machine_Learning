"""
@author: alp
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing

#Veri okuma
veriler = pd.read_csv("Iris.csv")

#Eksik veri

#Verileri kategorilerine ayırma
YaprakDegerleri = veriler.iloc[:,1:5].values
Tur = veriler.iloc[:,5:6].values
le = preprocessing.LabelEncoder()
Tur[:,0] = le.fit_transform(veriler.iloc[:,5:6])

#OneHotEncodder uygulama
ohe = preprocessing.OneHotEncoder()
Tur = ohe.fit_transform(Tur).toarray()

#Dataframe oluşturma
Sonuc1 = pd.DataFrame(data=YaprakDegerleri, index= range(150), columns=['Sepal-Uzunlugu','Sepal-Genisligi','Petal-Uzunulugu','Petal-Genisligi'])
Sonuc2 = pd.DataFrame(data=Tur, index= range(150),columns= ['Iris-setosa','Iris-versicolor','Iris-virginica'])

"""
Buradan sonra x-y train-test kısmında neyin neye göre tahmin edileceğini anlamadımdan veri toplam yöntemide askıya aldım

#Verilerin toplanması
SonucToplam = pd.concat([Sonuc1,Sonuc2], axis=1)  
print(SonucToplam)
"""
#Eğitim testi 