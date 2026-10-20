# -->OPERASI PADA LIST,SET DAN STRING 
#   Contoh contoh pada list, set ,dan string :
# 1. len() untuk menghitung panjang atau banyaknya list,set,dan string. khusus pada string program akan menghitung jumlahnya

contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9] # list ia menghitung semua jumlah pada  "[]" lalu menampilkan jumlahnya

print(contoh_list)
print(len(contoh_list))

"""
Output:
[1, 3, 3, 5, 5, 5, 7, 7, 9]
9
"""

contoh_list = set([1, 3, 3, 5, 5, 5, 7, 7, 7, 9]) # set ia mengkonversi dari list ke set lalu berubah menjadi anggota set yang tidak memiliki duplikat lalu ia menghitung dan berjumlah 5

print(contoh_list)
print(len(contoh_list))

"""
Output:
{1, 3, 5, 7, 9}
5
"""

contoh_list = "Teh Dwi Nurul Camtikk" # string menghitung jumlah karakter string (termasuk whitespace/spasi)

print(contoh_list)
print(len(contoh_list))

"""
Output:
Teh Dwi Nurul Camtikk
21
"""

# -->  MIN() DAN MAX ()
#      selain menghitung panjang atau banyaknya elemen, Anda juga dapat mengetahui berapa nilai minimum dan maksimum dari suatu list menggunakan fungsi min() dan max().

angka = [13, 7, 24, 5, 96, 84, 71, 11, 38] # Pada ini, Anda mencari anggota dengan nilai terkecil (minimal) dan nilai terbesar (maksimal) pada variabel "angka" yang merupakan list.
print(min(angka))
print(max(angka))

"""
Output:
5
96
"""

# --> COUNT
#     digunakan untuk mengetahui berapa kali suatu objek muncul dalam list

genap = [2, 4, 4, 6, 6, 6, 8, 10, 10] # menghitung angka dengan (count(masukkan angka apa yang mau di hitung)) 
print(genap.count(6))

"""
Output:
3
"""

string = "Teh Dwi Nurul Camtikk dulu aku menyukainya" # menghitung banyaknya huruf/substring a dalam string dengan sintaks count()
substring =  "a"
print(string.count(substring))


# --> In dan Not In
#     In dan not in untuk mengetahui nilai atau objek yang ada dalam list juga bisa untuk memastikan suatu nilai ada dalam list bahkan dalam string 
#     operator In dan Not In juga mengembalikan nilai boolean True or False, contoh kodenya :

kalimat = ('Teh Dwi Nurul Camtikk dan Maniss') 
print('Dwi' in kalimat)
print('Camtikk' in kalimat)
print('Dwi' not in kalimat)
print('Camtikk' not in kalimat)

"""
Output:
True
True
False
False

"""

# -->Memberikan Nilai untuk Multiple Variable
#    Dalam list atau tuple, terkadang Anda perlu memberikan nilai pada variabel-variabel tersebut. Secara konvensional, Anda bisa melakukan hal tersebut dengan menandai indeks yang diinginkan dan memberikan nilai satu per satu sesuai keinginan. 
"""
data = ['shirt', 'white', 'L']
apparel = data[0]
color = data[1]
size = data[2]

"""

data = ['Baju', 'Putih', 'L'] # penggabungan kode diatas
apparel, color, size = data

print(data)
print(apparel)
print(color)
print(size)


"""
Output:
['Baju', 'Putih', 'L']
Baju
Putih
L
"""

# -->SORT
#    untuk mengurutkan angka ataupun huruf

kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat'] # mengurut dengan huruf pertama dalam alfabet dengan sintaks 
kendaraan.sort()

print(kendaraan)

"""
Output:
 ['helikopter', 'mobil', 'motor', 'pesawat']

"""

#     beberapa hal mengenai sort():

kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat'] # 1. membalikan urutan huruf dengan sintaks sort(reverse=True)
kendaraan.sort(reverse=True)

print(kendaraan)

"""
Output:
 ['pesawat', 'motor', 'mobil', 'helikopter']

"""
"""
urutan = ['Tehdwi', 1, 3, 'Tasikmalaya', 13] # 2. Metode sort tidak dapat mengurutkan list yang memiliki angka dan string sekaligus di dalamnya
urutan.sort()
"""
"""
Output:
TypeError: '<' not supported between instances of 'int' and 'str'

"""

kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat'] # 3. Metode sort menggunakan urutan ASCII sehingga nilai huruf kapital (uppercase) akan lebih dahulu dibandingkan huruf kecil (lowercase).
kendaraan.sort()

print(kendaraan)

"""
Output:
['Pesawat', 'helikopter', 'mobil', 'motor']

"""