# KONVERSI TIPE DATA
"""
Konversi antara tipe data dengan menggunakan beberapa fungsi,
fungsi merupakan blok kode yang dapat di panggil untuk melakukan tugas tertentu,
untuk saat ini cukup memahami dulu fungsi operasi terhadap list,set,dan string
"""
# Di bawah ini merupakan berbagai fungsi yang dapat digunakan untuk mengonversi data antar list, set, dan string :

# 1.

print(float(5)) # konversi interger ke float cukup menggunakan fungsi float "()" dengan memasukan nilai interger di dalamnya "5"

"""
Output:
5.0

"""

# 2.

print(int(5.6)) # konversi float ke interger menggunakan fungsi "int ()" dengan memasukkan nilai float di dalamnya "5.6 dan -5.6"
print(int(-5.6))

""" 
Output:
5
-5

"""

# 3.
print(int("25")) # konversi dari-dan-ke string
print(str(25))
print(float("25"))
print(str(25.6))

"""
Output:
25
25
25.0
25.6

"""
# Harus diperhatikan bahwa konversi dari-dan-ke string akan melalui pengujian dan dipastikan validitasnya. 
# Jika pengujian dan validitasnya gagal, error akan dihasilkan, contoh :

"""
print(int("1p")) 

Output:
ValueError: invalid literal for int() with base 10: '1p

error alasannya karena 1p di anggap tidak valid 
"""
# 4. 

print(set([1,2,3]))
print(tuple({5,6,7}))
print(list('Teh Dwi Nurul Camtikk'))

"""
Output:
{1,2,3}
(5,6,7)
['T', 'e', 'h', ' ', 'D', 'W', 'i', ' ', 'N', 'u', 'r', 'u', 'l', ' ', 'C', 'a', 'm', 't', 'i', 'k', 'k']

Untuk melakukan konversi kumpulan data dari-dan-ke set/list/tuple, 
anda cukup menggunakan fungsi dari tipe data yang diinginkan. Misalnya, set(), tuple(), dan list() seperti pada kode di atas.


"""

# 5. 

print(dict([[1,2],[3,4]])) #Untuk konversi ke dictionary, data harus memenuhi persyaratan key-value. Selain itu, Anda bisa melakukan konversi ke dictionary menggunakan fungsi dict(). 

"""
Output:
{1:2, 3:4}

Pada kode di atas terdapat list berisi dua list yang berisi pasangan nilai, 
yakni [1,2] dan [3,4]. Lalu, list tersebut diubah menjadi dictionary dengan nilai 1 dan 3 sebagai key serta nilai 2 dan 4 sebagai value.

"""
#         Konversi list dari beberapa tuple yang isinya pasangan nilai menjadi dictionary, sebagai berikut :

print(dict([3,26],[4,44]))

"""
Output:
{3:26, 4:44}

Pada kode di atas terdapat list yang berisi dua tuple dengan pasangan nilai, 
yakni (3,26) dan (4,44). Setelah diubah menjadi dictionary, nilai 3 dan 4 menjadi key, sedangkan nilai 26 dan 44 menjadi value.
"""


