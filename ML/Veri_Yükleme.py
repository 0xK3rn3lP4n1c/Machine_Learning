# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 03:59:24 2020

@author: Ömer Kaan

Header: Veri Ön İşleme (Data Preprocessing)
"""

#kütüphaneler
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

#kod bölümü
#veri yükleme 
veriler = pd.read_csv("veriler.csv")
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