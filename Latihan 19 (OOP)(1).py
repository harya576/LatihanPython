class Mobil: # penerapan method static
    def __init__(self, merek):
        self.merek = merek


    @staticmethod
    def intro_mobil():
        print("Ini adalah metode dari class Mobil")


Mobil.intro_mobil()
mobil_1 = Mobil("Toyota")
mobil_1.intro_mobil()


class Mobil:
    def __init__(self, merek):
        self.merek = merek


    @classmethod
    def intro_mobil(cls):
        print("Ini adalah metode dari kelas Mobil")

Mobil.intro_mobil()
mobil_1 = Mobil("Toyota")
mobil_1.intro_mobil()


class Mobil: # penerapan class method
    def __init__(self, merek):
        self.merek = merek


    @classmethod
    def intro_mobil(*args):
        print(args)

Mobil.intro_mobil()
mobil_1 = Mobil("Toyota")
mobil_1.intro_mobil()