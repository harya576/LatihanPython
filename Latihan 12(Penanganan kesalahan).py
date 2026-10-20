# -->  PENANGANAN KESALAHAN
"""
if 9>10: # contoh identation error
print("Hello Word")

"""

"""
i = 1 # contoh kesalahan sintaksis (syntax error)
while i<3
    print("Dicoding")
    i+=1

"""

"""
print(angka) # contoh kesalahan pengecualian (exceptions)

"""

"""
bukan_angka = '1' # contoh lain kesalahan pengecualian (exceptions)
bukan_angka + 2

"""

"""
z = 0 # contoh penerapan peanganan pengecualian 
print(1/z)

"""
"""
z=0  # contoh penerapan try except
try:
    print(1/z)
except ZeroDivisionError:
    print("Anda tidak bisa membagi angka dengan nilai nol")

"""

"""
var_dict = {"rata_rata":"1.0"} # contoh penerapan struktur lengkap try

try:
    print(f"rata rata adalah {var_dict['rata_rata']}")
except KeyError:
    print("Key tidak di temukan.")
except TypeError:
    print("Anda tidak bisa membagi nilai dengan tipe data string")
else:
    print("Kode ini dieksekusi jika tidak ada exception")
finally:
    print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception")
"""

var = -1
if var < 0:
    raise ValueError("Bilangan negatif tidak diperbolehkan")
else:
    for i in range(var):
        print(i+1)