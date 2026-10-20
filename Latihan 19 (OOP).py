# --> OOP ( OBJECT ORIENTED PROGRAMMING)

class Mobil: # contoh penerapan class
    warna = "Orange"

class Mobil:
    Warna = "Orange" # contoh penerapan atribut

mobil_1 = Mobil()

class Mobil:
    warna  = "Biru" # atribut

mobil_1 = Mobil() # objeck
print(mobil_1.warna)

class Mobil: # mengganti value dari atribut
    warna = "Merah"

mobil_1 = Mobil()
mobil_1.warna = "Hijau"
print(mobil_1.warna)

class Motor: # penggunaan atribut kelas
    Warna = "Putih" # atribut

motor1 = Motor()
print(motor1.Warna)

motor2 = Motor()
print(motor2.Warna)

Motor.Warna = "Hitam"

print(motor1.Warna)
print(motor2.Warna)

class Mobil: # penerapan class constructor
    def __init__(self): # atribut instance
        self.warna = 'Merah'
        
mobil_1 = Mobil()
mobil_2 = Mobil()

print(mobil_1.warna)
print(mobil_2.warna)

mobil_1.warna = "Hitam" # Mengubah atribut instance

print(mobil_1.warna) # Menampilkan kembali atribut warna
print(mobil_2.warna)

class Mobil: # penerapan class constructor dengan beberapa argumen
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

mobil_1 = Mobil ('Merah', 'Toyota', 160)

print(mobil_1.warna)
print(mobil_1.merek)
print(mobil_1.kecepatan)

def my_decorator(func): # penerapan methode dari objek  dengan dekorator
    def wrapper():
        print("Sebelum fungsi di eksekusi")
        func()
        print("Setelah fungsi di eksekusi")
    return wrapper

@my_decorator # dekorasi fungsi dengan dekorator
def say_hello():
    print("Hello Word!")

say_hello() # memanggil fungsi yang sudah di dekorasi

class Mobil: # penerapan methode dari objek dengan menggunakan dekorasi fungsi lalu melakukan perubahan += 10
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10

mobil_1 = Mobil("Putih", "Toyota", 160)
print("Sebelum ditambahkan: ")
print(mobil_1.kecepatan)

mobil_1.tambah_kecepatan() # memanggil metode tambah_kecepatan

print("Sesudah ditambahkan")
print(mobil_1.kecepatan)



