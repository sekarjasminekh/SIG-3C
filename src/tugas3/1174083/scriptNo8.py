# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:33:31 2019

@author: bakti
"""
import shapefile #mengimport shapefile

sf = shapefile.Reader("contohFile") #untuk membaca file tanpa menggunakan ekstensi
anu=sf.shapes() #untuk menyimpan variable sf di dalam anu
anu[0].points #membaca data di dalam variable anu yang pertama points yaitu berisikan file .shp

# In[]