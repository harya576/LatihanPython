# --> STYLE GUIDE

def LuasPersegiPanjang(panjang: int = 2, lebar: int = None): 
    luas = panjang * lebar
    return luas

luas_satu = LuasPersegiPanjang(lebar=2)
print(luas_satu)

class DividedByZeroError(Exception): # penerapan nama exception
    def __init__(self, messsage = "Divion by Zero is not allowed"):
        super().__init__(messsage)

def divide_numbers(a,b):
    if b == 0:
        raise DividedByZeroError("Cannot divide by zero")
    return a / b

try :
    result = divide_numbers(10, 0)
except DividedByZeroError as e:
    print(f"Error: {e}")

class Myclass:
    def __init__(self):
        self._private_var = 42   # Variabel non publik dengan awalan satu garis bawah
        self._secret_list = [1, 2, 3]  # Variabel non publik lainnya

    def _private_method(self):
        print("Ini adalah method non publik")

    def public_method(self):
        print("Ini adalah method publik")
        self._private_method()  # Method publik dapat memanggil method non publik

    



