# penyederhanaan kode dari latihan 22
# membuat class test user turunan dari unittest
import unittest

def koneksi_ke_db():
    print("[terhubung ke db]")

def putus_koneksi_db(db):
    print("[tidak terhubung ke db{}]".format(db))

class User:
    username = ""
    aktif = False

    def __init__(self, db, username): # using db sample
        self.username = username

    def set_aktif(self):
        self.aktif = True

class TestUser(unittest.TestCase):
    # test case 1
    def test_user_default_not_active(self):
        db = koneksi_ke_db()
        dicoding = User(db,"dicoding")
        self.asseertFalse(dicoding.aktif) # tidak aktif secara default
        putus_koneksi_db(db)

    # test case
    def test_user_is_active(self):
        db = koneksi_ke_db
        dicoding = User(db, "dicoding")
        dicoding.set_aktif() # untuk mengaktifkan user baru
        self.assertTrue(dicoding.aktif)
        putus_koneksi_db(db)

if __name__ =="__main__":
    # Test runner
    unittest.main
