# --> PERCABANGAN DAN TERNARY OPERATORS

ketersediaan = "Daging Ayam" # Contoh kode percabangan jika-maka(If-Else)

if ketersediaan == "Daging Ayam":
    print("Ibu membeli dan memasak ayam")
else :
    print("Ibu membeli dan memasak tempe")

score = 100 # Implementasi If yang merupakan blok kode

if score == 100:
    print("Nilai anda sempurna")

x = "" # contoh kode python menganggap setiap nilai kosong(zero) dan null sebagai False begitupun sebaliknya

if x:
    print("Ini True")

score = 100 # contoh blok kode if hanya satu baris saja atau one liner

if score == 100: print("Nilai anda sempurna")

tinggi_badan = 120

if tinggi_badan >=160: # penggunaan blok kode else jika blok kode if bernilai false
    print("Anda boleh menaiki roller coaster")
else:
    print("Anda tidak diperbolehkan naik roller coaster")

nilai = 80 # Penggunaan blok kode elif penempatan setelah blok kode if

if nilai>=80:
    print("Selamat anda mendapat nilai A")
    print("Pertahankan!")
elif nilai>=70:
    print("Hore! anda mendapat nilai B")
    print("Tingkatkan!")
elif nilai>=60:
    print("Hmm... Anda mendapat nilai C")
    print("Ayo semangat!")
else:
    print("Waduh anda mendapat nilai D")
    print("Yuk belajar lebih giat lagi!")

nilai = 81 # penambahan operator and atau or pada percabangan  
perilaku = 'tidak baik'

if nilai>= 80 and perilaku == 'baik':
    print("Selamat! Anda bernilai baik dan telah berkelakuan baik")
    print("Pertahankan!")
elif nilai>=80 and perilaku !='baik':
    print("Kamu mendapat nilai A, tetapi perilaku anda kurang baik")
    print("Perbaiki lagi ya!")
else:
    print("Yuk belajar lebih giat lagi")

lulus = True # penerapan ternary operators
print("Selamat") if lulus else print("Perbaiki")

lulus = True # penerapan ternary operators jika dalam bentuk blok
if lulus:
    print("selamat")
else:
    print("Perbaiki")

lulus = True # penerapan ternary tuples
kelulusan = ("Perbaiki, Anda belum lulus.","Selamat, Anda lulus!")[lulus]
print(kelulusan)

lulus = True # penerapan ternary tuples jika dalam bentuk blok
if lulus:
    print("Selamat, Anda lulus!")
else:
    print("Perbaiki, belum lulus.")
