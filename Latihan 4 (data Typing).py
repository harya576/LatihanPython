#Data Typing
#Sekarang Anda memahami bahwa komputer perlu mengetahui data yang diinginkan dengan cara melakukan deklarasi
#Deklarasi&Inisialisasi
#Deklarasi merujuk pada pembuatan variabel dengan menentukan tipe data dan nama variabelnya. Umumnya, ini dilakukan oleh bahasa pemrograman lainnya, seperti C/C++
#contoh :
'''
int age;
float salary;

'''
#Sementara inisialisasi merujuk kepada pemberian nilai awal pada variabel yang sebelumnya telah dideklarasikan. Berikut contohnya jika menggunakan bahasa pemrograman C/C++
#contoh :
'''
int age = 17;
float salary = 5000000;

'''
#Jika diubah dalam ke dalam pyton sebagai berikut :
age = 19
salary = 12000000.0

print(type(age))
print(type(salary))

"""
Output:
<class 'int'>
<class 'float'>

"""
#Python juga merupakan bahasa pemrograman yang menerapkan dynamic typing. Artinya, Python adalah bahasa pemrograman yang hanya mengetahui tipe variabel saat program berjalan dan melakukan proses assignment. Hal ini memungkinkan kita untuk mengubah tipe data dari suatu variabel seiring berjalannya program.
#contoh :
x = 6
print(type(x))

x = "6"
print(type(x))

"""
Output:
<class 'int'>
<class 'str'>
"""
#Pada kode di atas, variabel yang digunakan sama-sama bernama “x”, tetapi yang pertama “x” bertipe integer, sedangkan yang kedua bertipe string. 