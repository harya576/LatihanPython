# --> FUNGSI
"""
def mencari_luas_persegi_panjang(Panjang,Lebar): # mebuat fungsi
    luas_persegi_panjang = Panjang * Lebar
    return luas_persegi_panjang
"""

def mencari_luas_persegi_panjang(Panjang,Lebar): # Memanggil fungsi dengan  menggunakan  print (), len() dan sebagainya
    luas_persegi_panjang = Panjang * Lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(10,5) # ini contoh memanggil fungsi
print(persegi_panjang_pertama)

def mencari_luas_persegi_panjang(Panjang,Lebar): # contoh mendefinisikan docstring
    """
    Fungsi ini digunakan untuk menghitung luas persegi panjang

    args :
        panjang (int) : Panjang persegi panjang
        lebar (int) : Lebar persegi panjang 

    Return :
        int : Luas persegi panjang hasil perhitungan
    """

    luas_persegi_panjang = Panjang * Lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang (5,10)
print(persegi_panjang_pertama)


def mencari_luas_persegi_panjang(Panjang, Lebar): # penggunaan argumen dalam python (keyword argument)
    luas_persegi_panjang = Panjang * Lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang (Panjang = 5, Lebar = 10) # contohnya seperti ini

print(persegi_panjang_pertama)


def mencari_luas_persegi_panjang(Panjang, Lebar): # penggunaan argumen dalam python (positional argumen)
    luas_persegi_panjang = Panjang * Lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang (5,10)

print(persegi_panjang_pertama)



def greeting(nama, pesan): # contoh penggunaan parameter (Positional or Keywoard)
    return "Halo, " + nama + "! " + pesan

print(greeting("Teh Dwi Nurul Camtikk", "Selamat Pagi!"))
print(greeting(pesan="Selamat sore!", nama = "Teh Dwi Nurul Camtikk"))


def penjumalahan(a, b, /): # contoh penggunaan parameter (Positional Only)
    return a + b

print(penjumalahan(8, 50))

def greeting(*, nama, pesan): # contoh peggunaaan parameter (keywoard only)
    return "Halo, " + nama + "! " + pesan

print(greeting(pesan="Selamat sore!", nama= "Teh Dwi Nurul Camtikk"))


def hitung_total(*args): # contoh penggunaan parameter (Var-Positonal)
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1, 2, 3, 4, 5, 6, 7, 8, 9))


def cetak_info(**kwargs): # contoh penggunaan parameter (Var-Keywoard)
    info = ""
    for key, value in kwargs.items():
        info += key + ': '+ value + ","
    return info

print(cetak_info(nama = "Teh Dwi Nurul Camtikk", Usia = "24", pekerjaan = "Untuk saat ini berjualan cireng", Pendidikan = "Lulusan S1 Farmasi", tempat_lahir = "Tasikmalaya"))

mencari_luas_persegi_panjang = lambda panjang, lebar: panjang * lebar
print(mencari_luas_persegi_panjang(5,10))

a = 10 # contoh penerapan variabel global

def add(b):
    result = a+b
    return result

bilanganPertama = add(20)
print(bilanganPertama)

def add(a, b): # contoh penerapan lokal var
    lokal_var = 5
    result =  a + b-lokal_var
    return result

bilanganPertama = add(10,20)
print(bilanganPertama)

