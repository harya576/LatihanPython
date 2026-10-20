"""
    4. Dictionary
       Dictionary merupakan kumpulan pasangan key-value yang  bersifat tidak berurutan.
       Dictionary dapat menyimpan data kecil hingga besar.
       Dictionary di definisikan dengan ( "{}" ) dan :
            1. setiap element pasangan key-value di pisahkan dengan koma(,)
            2. key dan value dipisahkan dengan titi dua(:)
            3. key dan value dapat berupa tipe variabel/onjek apapun 
       Contoh :

       'name' : 'Teh Dwi Nurul Camtikk', 'age' : 24, 'isMaried': False
          ^               ^                ^      ^      ^          ^
          |               |                |      |      |          |
          |               |                |      |      |          |
        key            value              key   Value   key        Value

"""
# Contoh kodenya :

x = { 'name': 'Teh Dwi Nurul Camtikk', 'age': '24', 'isMarried': False }
print(type(x))

"""
Output:
<class 'dict'>

'dict' adalah kepanjangan dari dictionary 
 sintaks yang diapit tanda kurawal “{}” dan memiliki pasangan key-value akan dianggap sebagai data bertipe dictionary oleh program.
 dictionary juga tidak bisa menggunakan metode indexing

"""
x = { 'name': 'Teh Dwi Nurul camtikk', 'age': 24, 'isMarried': False }
print(x['name']) # memanggil key(hanya satu yaitu 'name')

""" 
Output:
Teh Dwi Nurul Camtikk

"""
# hal lain terkait dictionary :

#   1.
x = { 'name': 'Teh Dwi Nurul camtikk', 'age': 24, 'isMarried': True }
x ['partner'] = "With Harya" # menambahkan data pada dicionary dengan memasukkan key dan valuenya “x[‘partner’] = ‘With Harya’”

print(x)

"""
Output:
{'name': 'Teh Dwi Nurul Camtikk', 'age': 24, 'isMarried': True, 'Partner': 'With Harya'}

"""

#   2.

x = { 'name': 'Teh Dwi Nurul camtikk', 'age': 24, 'isMarried': False }
del x['isMarried'] # menghapus data 'isMarried' dengan menggunakan sintaks "del"

print(x)

"""
Output:
{'name': 'Perseus Evans', 'age': 20}

"""

#   3.

x = { 'name': 'Teh Dwi Nurul camtikk', 'age': 18, 'isMarried': False }
x ['name'] = "Hasna Mazaya" # mengubah data dictionary dengan mengakses key nya 'name'  

print(x)

"""
Output:
{'name': 'Hasna Mazaya', 'age': 19, 'isMarried': False}

"""


