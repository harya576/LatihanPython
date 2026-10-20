#TIPE DATA PRIMITIF (NUMBERS,BOOLEAN,INTERGER)
# Tipe data primitif (numbers)
# Ciri dari bilangan numbers adalah Anda dapat mengoperasikan bilangan tersebut dengan operasi matematika sederhana, seperti pertambahan (+), pengurangan (-), perkalian (*), dan operasi matematika lainnya.
# tipe data numbers bersifat immutable yang artinya nilai di dalamnya tidak dapat diubah
# Contoh :
x = 6
print(type(x))

x = 6.0
print(type(x))

x = 1+2j
print(type(x))

"""
Output:
<class 'int'>
<class 'float'>
<class 'complex'>

"""
var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))

"""
Output:
10
<memory address>
11
<memory address>

"""
# Tipe data primitif (Boolean)
# Tipe data primitif kedua adalah boolean, yakni tipe data yang hanya bernilai TRUE atau FALSE 
# Contoh penggunaaan :

x = True
print(type(x))

x= False
print(type(x))

"""
Output:
<class 'bool'>
<class 'bool'>

"""

# Tipe data primitif (String)
# String merupakan karakter yang berurutan. Ketika Anda membuat variabel bernilai string tentu diawali dengan single quote (‘’) atau double quote (“”).
# Contoh penggunaan :

x = 'Teh Dwi Nurul Camtikk'
print(type(x))

"""
  Output: 
  <class 'str'>

"""
# Variabel x yang menyimpan teks “Teh Dwi Nurul Camtikk” adalah variabel dengan data bertipe string. Sederhananya, teks “Teh Dwi Nurul Camtikk” tersebut adalah string.

# Fakta menarik tentang python :
#  1. Anda dapat menggunakan tiga single quote atau double quote untuk menyimpan string yang lebih dari satu baris (multi-line).
#     Contoh :

multi_line= """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu 2 bulan yang lalu."""

print(multi_line)

"""
Output:
Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu.

"""
#     Pada kode di atas, Anda menampilkan string lebih dari satu baris (multi-line) menggunakan double quote (”””).

#  2. String merupakan urutan karakter yang setiap karakternya memiliki indeks.
#     Anda dapat mengakses setiap karakter dari string (substring) dengan menggunakan metode indexing, Perlu diingat bahwa indeks selalu dimulai dari 0.
#     Contoh :

x = 'Teh Dwi Nurul Camtikk'
print(x[0])

""" 
Output:
D

"""
#     Pada kode di atas, diambil indeks ke-0 dari string “Teh Dwi Nurul Camtikk” yakni huruf “T”. Metode indexing merupakan cara untuk mengambil spesifik elemen berdasarkan indeksnya.

#  3. Namun, Anda tidak dapat mengubah substring di dalamnya. Ini dikarenakan string pada Python bersifat immutable.

x = 'Teh Dwi Nurul Camtikk'
x[0] = 'F'

""" 
Output:
TypeError: 'str' object does not support item assignment

"""
#  4. Anda dapat mengakses beberapa substring dengan menggunakan metode indexing dan slicing.
#     Contoh :

x = 'Dicoding'
print(x[2:])

"""
Output:
coding

"""
