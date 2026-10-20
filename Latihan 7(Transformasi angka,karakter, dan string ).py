# TRANSFORMASI ANGKA,KARAKTER, DAN STRING.
# --> Mengubah huruf besar dan kecil 
#     mengubah string menjadi huruf kapital(Uppercase)/ atau huruf kecil (lowercase) contoh sintaks :

kata = 'Teh Dwi Nurul Camtikk' # 1. Upper() mengubah string "Teh Dwi Nurul Camtikk" menjadi uppercase(KAPITAL) "method.upper()"
kata = kata.upper()
print(kata)

"""
Output:
Teh Dwi Nurul Camtikk

"""
kata = 'Teh Dwi Nurul Camtikk' # 2. lower() mengubah string "Teh Dwi Nurul Camtikk" menjadi lowercase(huruf kecil) "method.lower()"
kata = kata.lower()
print(kata)

"""
Output :
Teh Dwi Nurul Camtikk

"""

# --> Mengubah awalan dan akhiran
#     untuk menghapus karakter whitespace pada suatu string juga bisa untuk menghilangkan kata yang tidak di inginkan

print("Teh Dwi Nurul Camtikk        ".rstrip()) # 1. rstrip() menghapus whitespace pada sebelah kanan atau akhir kalimat ".rstrip()"

"""
Output :
Teh Dwi Nurul Camtikk

"""

print("     Teh Dwi Nurul Camtikk".lstrip()) # 2. lstrip()  menghapus spasi yang berada pada sebelah kiri string ".lstrip()"

"""
Output :
Teh Dwi Nurul Camtikk

"""

print("     Teh Dwi Nurul Camtikk       ".strip()) # 3. strip() menghapus spasi yang berada di kiri dan kanan ".strip()"

"""
Output :
Teh Dwi Nurul Camtikk

"""

kata = "manissmanissTeh Dwi Nurul Camtikkmanissmaniss" # contoh lain dari strip untuk menghapus suatu karakter contohnya "maniss" sintaksnya : ".strip("masukkan karakter")"
print(kata.strip("maniss"))

"""
Output :
Teh Dwi Nurul Camtikk

"""

print('Teh Dwi Nurul Camtikk'.startswith('Teh Dwi')) # 4. startswith() untuk menemukan/mencari suatu kata pada awal string juga dia akan menampilkan nilai "True or False"


"""
Output :
True

"""

print('Teh Dwi Nurul Camtikk'.endswith('Teh Dwi')) # 5. endswith() untuk menemukan/mencari suatu kata pada akhir string juga dia akan menampilkan nilai "True or False"

"""
Output :
False

"""
# --> Memisah dan Menggabungkan String.
#     memisahkan dan menggabungkan string dengan menggunakan 2 metode :

print(' '.join(['Teh Dwi', 'Nurul Camtikk', '!'])) # 1. ' '.join(['masukkan string']) menggabungkan string 'Teh Dwi' dengan 'Nurul Camtikk' dan menambahkan singe quote " '' " pada setiap kata/nilai yang ingin anda gabungkan delimeternya adalah whitespace atau spasi yang tersimpan di list "[]"


"""
Output :
Teh Dwi Nurul Camtikk !

"""

print('123'.join(['Teh Dwi', 'Nurul Camtikk'])) # menambahkan delimeter lain pada join() contohnya "123" yang tersimpan pada list "[]"

"""
Output :
Teh Dwi123Nurul Camtikk

"""

print('Teh Dwi Nurul Camtikk !'.split()) # split() memisahkan kata/substring berdasarkan delimeter lalu disimpan sebagai list ([])

"""
Output :
['Teh', 'Dwi', 'Nurul', 'Camtikk', '!']

"""

print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n')) # contoh delimeter lain (newline(\n)) untuk memisahkan setiap baris pada string multiline

"""
Output:
['Halo,', 'aku ikan,', 'aku suka sekali menyelam', 'aku tinggal di perairan.', 'Badanku licin dan renangku cepat.', 'Senang berkenalan denganmu.']

"""

# --> Mengganti Elemen Pada String 
#     mengganti elemen string di dalamnya dengan elemen string lainnya :

string = "Teh Dwi Nurul Camtikk !"
print(string.replace("Camtikk", "Maniss")) # 1. replace() untuk menggantikan suatu string contohnya dari "Camtikk" dengan "Maniss" ia juga bersifat case-sensitive

"""
Output :
Teh Dwi Nurul Maniss !

"""

# --> Pengecekan string
#     Melakukan pengecekan pada string juga pengembalian nilai boolean nilai True or False :

kata = 'TEH DWI NURUL CAMTIKK'  # 1. isupper() ia akan mengembalikan nilai true jika semua huruf kapital (UPPERCASE)  ada huruf kecil ia jika ada ia akan bernilai False
print(kata.isupper())

"""
Output:
True

"""

kata = 'teh dwi nurul camtikk' # 2. islower() ia akan bernilai true jika ia hurufnya nilai kecil semua(lowercase), jika terdapat kapital terdapat kapital ia akan bernilai False
print(kata.islower())

"""
Output:
True

"""

kata = 'tehdwinurulcamtikk' # 3. isalpha() ia akan bernilai True jika ia berbentuk huruf semua tanpa ada angka,spasi, dll 
print(kata.isalpha())

"""
Output:
True

"""

kata = 'tehdwinurulcamtikk123' # 4. isalnum() ia akan bernilai True jika dalam string adalah alfanumerik(huruf dan angka)
print(kata.isalnum())

"""
Output:
True

"""

kata = '13' # 5. isdecimal() ia akan bernilai True jika dalam string hanya (angka/numerik)
print(kata.isdecimal())


"""
Output:
True

"""


kata = '        ' # 6. isspace() ia akan bernilai True jika dalam string hanya (whitespace, spasi, tab, newline, dll)
print(kata.isspace())


"""
Output:
True

"""

print('Teh Dwi Nurul Camtikk'.istitle()) # 7. istitle() ia akan bernilai True jika dalam string hanya (Huruf Kapital Pada Setiap Kata Pertamanya)

"""
Output:
True

"""

# --> FORMATTING PADA STRING 
#     terdapat beberapa metode zfill(), rjust(), ljust(), center(), dll :

teks = 'Code' # 1. zfill () untuk menambahkan nilai 0 di depan string dengan panjang tertentu, tujuan ialah  untuk memastikan bahwa sebuah angka atau nilai memiliki panjang tetap, terutama ketika ingin menyimpan nilai dalam format yang konsisten.
tambah_number = teks.zfill(5)
print(tambah_number)

"""
Output:
0Code

"""

print('Dicoding'.rjust(20)) # 2. rjust() untuk merapikan percetakan teks menjadi rata kanan serta menambahkan white space Angka 20 yang Anda masukkan bersifat sama seperti pada zfill(). Metode rjust() akan memastikan bahwa panjang teksnya adalah 20 termasuk dengan kata "Dicoding".

"""
Output:
            Dicoding
"""

print('Dicoding'.rjust(20, '!'))

"""
Output:
!!!!!!!!!!!!Dicoding

*Menambahkan karakter "!" sebelum string "Dicoding".
"""

print('Dicoding'.ljust(20)) # 3. 1just() membuat teks menjadi rata kiri

"""
Output:
Dicoding
            '
"""

print('Dicoding'.center(10, '-')) # 4. center() menjadikan teks rata tengah

"""
Output:
-Dicoding-

*bahwa zfill(), rjust(), ljust(), dan center() berfungsi sama, yakni memastikan panjang teks sesuai dengan yang diminta.

"""

# -->STRING LITERALS 
#    diapit oleh tanda petik tunggal dalam kondisi tertentu dan dibutuhkan petik tunggal di tengah string sperti "Jum'at"

print("Halo!\nKapan terakhir kali kita bertemu ?\nKita bertemu hari jum\'at yang lalu.") # Penggunaan Escape Character dengan (\n) menampilkan baris teks yang awalnya hanya satu baris menjadi tiga baris dan dipisahkan oleh line break.


"""
Output:
Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum'at yang lalu

"""

# -->RAW STRING 
#    mencetak string seusai dengan apapun input atau teks yang diberikan, ia digunakan untuk regex atau beberapa implementasi lain yang sangat bergantung pada keberadaan backslash.

print(r'Tehdwinurulcamtikk\tManisss') # mencetak raw string dengan character (\t) raw string akan mencetak string sesuai dengan apa pun input atau teks yang diberikan.

