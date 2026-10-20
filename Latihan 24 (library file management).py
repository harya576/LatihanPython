# --> LIBRARY FILE MANAGEMENT

import os # library os
print(os.getcwd())


import json
 
# contoh JSON:
x = '{ "nama":"Teh Dwi Nurul Camtikk", "umur":24, "Kota":"Tasikmalaya"}'
 
# parse  x:
y = json.loads(x)
 
print(y["umur"])

import pickle
contoh_dictionary = {1:"6", 2:"2", 3:"f"}
pickle_keluar = open("dict.pickle","wb")
pickle.dump(contoh_dictionary, pickle_keluar)
pickle_keluar.close()





