# --> FUNDAMENTAL ARRAY

x = [1, 2, 3, 4, 5] # contoh penerapan  list sebagai array dalam python
print(x)

"""
import array # contoh penerapan array dalam python dengan menggunakan library pada python "array" yang hanya interger tidak boleh adanya tipe lai seperti string 

x = array.array("i",[1, 2, 3, 4, 5, 'Dicoding']) 
print(x)
print(type(x))
"""

nama_siswa1 = 90 # contoh penggunaan array dalam struktur data linear dalan kasus seorang guru matematika membuat kode program python
nama_siswa2 = 100
nama_siswa3 = 50
nama_siswa4 = 80
nama_siswa5 = 85
nama_siswa6 = 45
nama_siswa7 = 80
nama_siswa8 = 75
nama_siswa9 = 50
nama_siswa10 = 60

print(nama_siswa1)
print(nama_siswa2)
print(nama_siswa3)
print(nama_siswa4)
print(nama_siswa5)
print(nama_siswa6)
print(nama_siswa7)
print(nama_siswa8)
print(nama_siswa9)
print(nama_siswa10)


siswa = [90, 100, 50, 80, 85, 45, 80, 75, 50, 60] # contoh penggunaan array dalam struktur data dengan menggunakan list lalu melakukan indexing linear dalan kasus seorang guru matematika membuat kode program python

print(siswa)
print(siswa[0]) # indexing dengan menyebut index ke berapa contohnya adalah "0"

# --> IMPLEMENTASI ARRAY DALAM PYTHON 

var_list = [1, 2, 3] # penerapan deklarasi array lalu outputnya akan menghasilkan lokasi memroi setiap elemen pun juga berbeda tiap elemennya
for elemen in var_list:
    print(id(elemen))


var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] # contoh penerapn dekalarasi array dengan menggunakan metode mendefiniskan isi array 
print(var_arr)

var_arr = [0 for i in range(10)] # contoh penerapan deklarasi array dengan menggunakan metode mendefinisikan nilai default 
print(var_arr)

var_arr = [0 for i in range(10)] # contoh penerapan deklarasi array dengan menggunakan metode mengubah nilai default dengan nilai yang baru berdasarkan suatu operasi 

for i in range(10):
    var_arr[i] = i

print(var_arr)

var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] # contoh penerapan mengakses elemen pada array dengan indexing
print(var_arr[0]) # indexing
  


