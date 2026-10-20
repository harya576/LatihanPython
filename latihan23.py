# --> LIBARARY PYTHON

import re # penerapan library regix

pola = 'a...s$'
string_test = 'abyss'
hasil= re.match(pola, string_test)

if hasil:
    print("Pencarian berhasil")
else:
    print("Pencarian Gagal")

import math # penerapan library math

print(math.sqrt(25))
print(math.pi)
"""
import argparse # penerapan library parser

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help="Masukkan nama anda :")
parser.add_argument('-t', '--tanggal', required=True, help="Masukkan tanggal lahir anda :")
args = parser.parse_args()

print("Terimakasih telah menggunakan latihan23.py"+args.nama)
"""

"""
import pandas as pd 

data = { # membuat data frame dari dictionary
    'Nama': ['Harya', 'Nenes', 'Falah', 'Aji'],
    'Usia' : [25, 13, 29, 48],
    'Pekerjaan' : ['DevOps', 'FrontEnd', 'Engineer', 'Doctor']
}

df = pd.DataFrame(data)

# output data framenya
print(df)

"""

import numpy

matriks = numpy.array([[1, 2, 3], [4, 5, 6,], [7, 8, 9]])
print(matriks)


import numpy

matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
print(matriks)

import matplotlib.pyplot as plt
 
# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
 
# Membuat plot garis
plt.plot(x, y)
 
# Menambahkan judul dan label sumbu
plt.title("Contoh Plot Garis")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")
 
# Menampilkan plot
plt.show()

