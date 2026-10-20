# --> DEFINISI SUBPROGRAM

panjang = 5 # contoh kode berulang luas ke 1
lebar = 10

luas_persegi_panjang = panjang * lebar
print(luas_persegi_panjang)

panjang = 4 # contoh kode berulang luas ke 2
lebar = 15

luas_persegi_panjang = panjang * lebar # contoh penerapan subprogram untuk kode perulangan 
print(luas_persegi_panjang)

def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

persegi_panjang_kedua = mencari_luas_persegi_panjang(4,15)
print(persegi_panjang_kedua)

