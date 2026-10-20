# --> PERULANGAN

print(1) # contoh kode perulangan yang tidak efektif
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

var_list = [1,2,3,4,5,6,7,8,9,10] # penerapn sintaks for dalm perulangan
for i in var_list:
    print(i)

var_list = ["Teh Dwi Nurul Camtikk","Teh Dwi Nurul Maniss"] # penerapn sintaks for dalam perulangan dengan bentuk string
for i in var_list:
    print(i)

for i in range(10): # penerapn sintaks for dalam perulangan dengan bentuk fungsi range
    print(i)

for i in range(1,10,2):# penerapan sintaksis umum fungsi in range()
    print(i)

counter = 1 # impelemntasi fungsi while yang terus berulang sampai memenuhi kondisi jika menggunakan increment
while counter <= 5:
    print(counter)
    counter += 1 # increment
"""
counter = 1 # impelemntasi fungsi while yang terus berulang sampai memenuhi kondisi jika tidak menggunakan increment(dia akan terus berproses)
while counter <= 5:
    print(counter)

""" 
for i in range(1, 3): # contoh penerapan fungsi for bersarang 
    for j in range(1, 3):
        print(i,j)

for i in range(2): # perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10): # perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 1:
            break # menghetikan perualangan jika j = 1

for huruf in 'Dwi nurul ': # break jika bentuk string
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))

for huruf in 'Dwi Nurul': # penerapan continue atau melewati/mengabaikan suatu white space dalam contoh berikut
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))

numbers = [1, 2, 3, 4, 5] # penerapan Else setelah For perulangan bersifat pencarian 

for num in numbers:
    if num == 4:
        print("Angka ditemukan! Program Berhenti!")
        break
else:
    print("Angka tidak ditemukan")

count = 0 # penerapan Else setelah While blok statement else akan selalu dieksekusi saat kondisi pada while menjadi salah

while count < 3:
    print("Teh Dwi Nurul Camtikk")
    count += 1
else:
    print("Blok else akan dieksekusi karena pada kondisi pada while salah (3<3 == False).")

n = 10 # penerapan Else setelah While blok statement else akan selalu dieksekusi saat kondisi pada while menjadi salah jika menggunakan "break"
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")

x = 10 # Penerapan Pass pernyataan yang digunakan jika Anda menginginkan sebuah pernyataan atau blok pernyataan (statement), tetapi tidak ada tindakan atau program tidak melakukan apa pun.

if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")

angka = [1, 2, 3, 4] # Penerapn List Comprehension  terkadang ada kalanya Anda perlu membuat sebuah list baru berdasarkan list yang sudah ada.
pangkat = []
for n in angka:
    pangkat.append(n**2)
print(pangkat)

angka = [1, 2, 3, 4,] # Penerapn List Comprehension  terkadang ada kalanya Anda perlu membuat sebuah list baru berdasarkan list yang sudah ada tanpa perlu menggunakan ".append()" untuk menambahkan nilai baru
pangkat = [n**2 for n in angka]
print(pangkat)

