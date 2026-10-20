# -->      EKSPRESI
#          ekspresi pada pemrograman merupakan kombinasi dari satu atau lebih variabel, konstanta, operator, dan fungsi yang bermakna untuk menghasilkan suatu nilai dalam suatu tipe tertentu.

x = 10 # contoh penerapan ekspresi dalam python
y = 2
result = x - y

print(result)

"""
Output:
8

"""

angka = [1, 3, 2, 3] # penggabungan dan replikasi pada list menggunakan operator penjumlahan (+)
huruf = ['H', 'A', 'R', 'Y', 'A']
gabung = angka + huruf

print(gabung)

"""
Output:
[1, 3, 2, 3, 'H', 'A', 'R', 'Y', 'A']

"""

learn = ['H', 'A', 'R', 'Y', 'A'] # replikasi dan duplikasi ekspresi menggunakan perkalian (*)
replikasi = learn * 2

print(replikasi)

"""
Output :
['H', 'A', 'R', 'Y', 'A', 'H', 'A', 'R', 'Y', 'A']

"""

a = True # Penerapan ekspresi uner
a = not a
print(a)

b = 6
b -= 1
print(b)

c = 6
c += 1
print(c)

d = 10
print(-d)

"""
Output:
False
5
7
-10

"""

# --> JENIS JENIS EKSPRESI  

print(5+5) # contoh kode ekspresi matematika, ekspresi relasional, ekspresi logika
print(5<15) 
print(True or False)

"""
Output:
10
True
True

"""

# JENIS JENIS OPERATOR 

x = 11 # 1. Operator aritmatika
y = 6

print(x + y)
print(x - y)
print(x * y)
print(x // y)
print(x / y)
print(x % y)
print(x ** y )

"""
Output:

16
6
55
2
2.2
1
161051

"""

x = 5 # 2. Operator relasional
y = 10

print(x == y)
print(x != y)
print(x > y)
print(x > y)
print(x >= y)
print(x <= y)

"""
Output:

False
True
False
True
False
True

"""

x = "Dicoding" # Operator relasioan (string sedikit berbeda)
y = "Indonesia"

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

"""
Output:

False
True
False
True
False
True

"""

print(True and True) # 3.Operator Logika (AND) operator AND hanya akan menghasilkan nilai TRUE jika kedua operan, yakni P dan Q bernilai TRUE. Sisanya akan menghasilkan nilai FALSE
print(True and False)
print(False and True)
print(False and False)

"""
Output:

True
False
False
False
    
"""

print(True or True) # Operator Logika (OR) operator OR akan menghasilkan nilai TRUE jika salah satu atau kedua operan (yakni P atau Q) bernilai True. Mari lihat penerapannya pada Python.
print(True or False)
print(False or True)
print(False or False)

"""
Output:

True
True
True
False

"""

print(not True) # Operator Logika (NOT) operator NOT akan membalikkan nilai boolean dari operan aslinya atau disebut sebagai negasi.
print(not False)

"""
Output:

False
True

"""
# +=
x = 11  # 4. Operator Assignment operator ini bertujuan untuk melakukan proses assignment atau pemberian nilai pada suatu variabel dengan nilai tetap.
x += 5
print(x)

# -=
x = 11
x -= 5
print(x)

# *=
x = 11
x *= 5
print(x)

# /=
x = 11
x /= 5
print(x)

#%=
x = 11
x%= 5
print(x)


"""
Output:
16
6
55
2.2
1
"""
x = 11
x += 5
print(x)

x = 11
x = x + 5 
print(x)


"""
Output:
16
16

"""