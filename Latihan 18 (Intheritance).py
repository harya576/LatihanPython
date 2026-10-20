# --> INHERITANCE ( PEWARISAN )

class Mobil: # penerapan mekanisme pewarisan
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan


    def tambah_kecepatan(self):
        self.kecepatan += 10


mobil_1 = Mobil("Putih", "Civic", 160)
print(mobil_1.kecepatan)

class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

# Kelas mobil dasar
mobil_1 = Mobil("Putih", "Civic", 160)
print(mobil_1.kecepatan)

# Kelas mobil sport
mobil_sport_1 = MobilSport("Hitam", "CivicTurbo", 160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.turbo()
print(mobil_sport_1.kecepatan)

class Mobil: # peneraan override
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):   # tambah kecepatan
        self.kecepatan += 10


class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50


    def tambah_kecepatan(self): # tambah kecepatan
        self.kecepatan += 20

# kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "CivicTurbo", 160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.tambah_kecepatan() # memanggil metode baru tambah_kecepatan()
print(mobil_sport_1.kecepatan)

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10

class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

    def tambah_kecepatan(self):
        super().tambah_kecepatan()
        print("lalaunan kang hayang hirup keneh!! sia hayang modar?!!")

# kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "CivicTurbo", 160)
mobil_sport_1.tambah_kecepatan() # memanggil  metode baru tambah kecepatan()
print(mobil_sport_1.kecepatan)


