# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:09:38 2019

@author: ASUS
"""

import shapefile # import library shapefile
w = shapefile.Writer('no6', shapeType=5)  # menggunakan fungsi writer yang digunakan untuk menggambar dan akan dinamakan no6 dalam bentuk shapetype=5 yang merupakan sebuah polygon
 
w.field("kolom1","C")  # Digunakan untuk membuat kolom pertama pada table
w.field("kolom2","C")  # Digunakan untuk membuat kolom dua pada table
 
w.record("ngek","satu") # mengisi kolum yang sudah dibuat dengan ngek dan satu
 
w.poly([[[1,3],[5,3]]])  # menghubungkan garis dengan mendefinisikan setiap titik awal dan akhir dari garis tersebut


w.close() # Menutup writer