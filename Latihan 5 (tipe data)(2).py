#  4. Anda dapat mengakses beberapa substring dengan menggunakan metode indexing dan slicing.
#     Contoh :
x = 'Dicoding'
print(x[2:])

"""
Output:
coding

"""
#      pada kode di atas, diambil substring dari indeks ke-2 hingga indeks terakhir dengan menggunakan metode slicing,
#      metode slicing adalah cara yang sering digunakan untuk mendapatkan bagian dari suatu list atau array, metode ini dapat diterapkan pada string untuk mengambil satu atau banyak substring.

#   5. Anda dapat menampilkan teks/string berdasarkan input dari pengguna dengan berbagai cara :
#      - Formatted String 

name = "Harya Rachmat Suzana"
print("Hello, nama saya{name}")

"""
Output: 
Hello, nama saya Harya Rachmat Suzana

"""
#        Pada kode di atas, Anda menampilkan string dengan menggunakan metode formatted string
#        Metode ini diperuntukkan untuk menampilkan variabel bertipe string dengan menggunakan huruf “f” di depan string dan menempatkan variabel di dalam kurung kurawal.

#       - %-formatting

name = "Harya Rachmat Suzana"
print("Nama saya %s" % (name) )

"""
Output: 
Nama saya Perseus Evans

"""
#     metode ini menggunakan operator Modulo (%) untuk memasukkan nilai variabel ke dalam string dengan menggunakan format khusus yang ditentukan oleh tipe data variabel

#     - str.format()

name = "Teh Dwi Nurul Camtikk"
print("Nama saya {}".format(name))


"""
Output: 
Nama saya Teh Dwi Nurul Camtikk

"""
#    metode ini memungkinkan penggabungan variabel/nilai ke dalam string dengan menempatkan tanda kurung kurawal atau {} sebagai penempatan variabel. Sekilas mirip dengan formatted string, pembedanya adalah pada penggunaan “.format” setelah string.
# TIPE DATA COLLECTION
# Tipe data collection merupakan tipe data yang menyimpan satu atau lebih data primitif sebagai satu kelompok.
# Berikut yang termasuk tipe data collection :
"""
    1. List ( "[]" )
       List merupakan jenis kumpulan data terurut (ordered sequence) dan salah satu tipe data yang sering digunakan pada Python.
       List dalam Python ini serupa, tetapi tak sama dengan array pada bahasa pemrograman lainnya. 
       List Python tidak mengharuskan memiliki tipe data yang sama di dalamnya, sedangkan array sebaliknya. 
       List dalam python bersifat "mutable" yang artinya dapat di ubah
       Contoh :
       variabel_list = [1(integer), "Teh Dwi Nurul Camtikk"(string), True(Boolean), 1.o(float)]

"""
#     Contoh lainnya :
x = [1, 2.2,'Teh Dwi Nurul Camtikk']
print(type(x))

"""
Output: 
<class 'list'>

"""
#     metode indexing :
x = [1, "Teh Dwi Nurul Camtikk", True, 1.0]
print(x[2])

"""
Output: 
<class 'list'>

"""

#    List python bersifat mutable(dapat diubah)
#    Contoh :

x = [1, 2.2, "Teh Dwi Nurul Camtikk"]
x[0] = 'Tasikmalaya'
print(x)

"""
Output:
['Tasikmalaya', 2.2, 'Teh Dwi Nurul Camtikk']

"""

#    Contoh indexing lainnya :
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0])
print(x[2])
print(x[-1])
print(x[-3])

"""
Output:
laptop
mouse
microphone
keyboard

"""
# Pada dua sintaks pertama, Anda memerintahkan untuk menampilkan indeks ke-0 dan indeks ke-2. Selanjutnya, dua sintaks terakhir memerintahkan untuk menampilkan indeks terakhir dan indeks ke-3 dari terakhir. 
# Konsep slicing merujuk pada pengambilan data berdasarkan indeks dari rentang tertentu, contoh polanya :
"""
squence[start:stop:step]

"""
# Start merupakan indeks pertama yang Anda ambil. Stop merupakan indeks terakhir yang ingin Anda ambil. Step merupakan jumlah elemen yang ingin Anda lewati di antara setiap elemen slice. Secara default, nilai step adalah 1.
# Hal penting yang harus Anda ingat adalah nilai start bersifat inklusif sedangkan stop bersifat eksklusif. Masih ingat dengan konsep tersebut dalam matematika? Konsep ini menggambarkan batas tertentu dalam suatu interval. Jika suatu interval dikatakan inklusif, batas terakhir yang telah ditentukan akan dianggap sebagai bagian dari interval.
"""
Contoh : a>=b

Jika suatu interval dikatakan inklusif, batas terakhir yang telah ditentukan akan dianggap sebagai bagian dari interval. 
Namun, jika suatu interval dikatakan eksklusif, batas terakhir yang telah ditentukan tidak akan dianggap sebagai bagian dari interval.

"""
# Contoh implementasi slicing pada python :

x = ["Teh Dwi Nurul Camtikk", "Monitor", "Mouse", "Mousepad", "Keyboard", "Webcam", "Microphone"]

print(x[0:5:2])
print(x[1:])
print(x[:3])

"""
Output:
['Teh Dwi Nurul Camtikk', 'mouse', 'keyboard']
['monitor', 'mouse', 'mousepad', 'keyboard', 'webcam', 'microphone']
['Teh Dwi Nurul Camtikk', 'monitor', 'mouse']

"""
"""

    2. Tuple ( "()" )
       Tuple adalah jenis dari list yang tidak dapat diubah elemennya.
       Umumnya, tuple digunakan untuk data yang bersifat sekali deklarasi dan dapat dieksekusi lebih cepat
       Tuple didefinisikan dengan kurung “()“ dan setiap elemen di dalamnya dipisahkan dengan koma.


"""
# Contoh :
x = (1, "Teh Dwi Nurul Camtikk", 1+3j)
print(type(x))  

"""
Output:
<class 'tuple'>

Pada kode di atas, Anda dapat lihat bahwa nilai yang diapit tanda kurung “()” akan dianggap sebagai tuple oleh program

"""
# Anda juga dapat melakukan indexing dan slicing pada tuple sama seperti list.
# Contoh :

"""
x = (5, 'Teh Dwi Nurul Camtikk', 1+3j)
print(x[1])
print(x[0:3])
"""

""" 
Output:
program
(5, 'program', (1+3j))

Pada kode di atas, Anda mengambil string “program” yang berada pada indeks 1 dan 
menampilkan nilai dari indeks 0 hingga indeks 2 (ingat, bersifat eksklusif).

"""
# Tuple bersifat immutable yang artinya tidak dapat diubah, contoh :
"""
x = (5, 'Teh Dwi Nurul Camtikk', 1+3j)
x[1] = 'Harya Bersanding dengan Teh Dwi'

"""

"""
Output:
'tuple' object does not support item assignment

"""

"""
    3. Set ( "{}" )
    Set adalah kumpulan item bersifat unik, tanpa urutan (unordered collection), dan 
    dapat diinisialisasikan dengan kurawal “{}” di mana setiap elemennya dipisahkan dengan koma. 
    Tidak sama seperti list, dalam set kita tidak bisa melakukan indeksing karena set tidak memiliki indeks, 
    hal ini merujuk pada definisi nya yang menyatakan bahwa set merupakan kumpulan item tanpa urutan.

"""
# Contoh :

"""
x = {1,2,7,2,3,13,3}
print(x[0])
"""

"""
Output:
'set' object is not subscriptable

Pada kode di atas, program mengembalikan output 'set' object is not subscriptable,
karena setiap nilai dalam set tidak memiliki indeks sehingga tidak bisa dilakukan indexing, juga set tidak akan bisa di duplikat,
bisa untuk menghilangkan duplikat data juga,

"""
# Contoh :

x = {1, 2, 7, 2, 3, 13, 3}
print(x)
print(type(x))

"""
Output:
{1, 2, 3, 7, 13}
<class 'set'>

'set' himpunan dalam matematika yang berari kamu bisa melakukan operasi union (gabungan) dan intersection(irisan) pada set.
Python juga menyediakan method ".union()" dan ".intersection()" untuk tipe data set.

"""
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union:", union)

intersection = set1.intersection(set2)
print("Intersection:", intersection)

"""
Output:
Union: {1, 2, 3, 4, 5, 6, 7, 8}
Intersection: {4, 5}

"""

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

"""