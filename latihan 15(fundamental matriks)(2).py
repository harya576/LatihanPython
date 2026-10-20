# --> FUNDAMENTAL MATRIKS

matriks =  [[3, 4, 5], # penggunan matriks dengan nested list (kurung dalam kurung contohnya [[]])
            [6, 7, 8],
            [9, 10, 11]]

print(matriks)


import numpy # impelementasi matrik dengan menggunakan libarary numpy

matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriks)


import numpy
import sys

var_list= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var_array= numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])

print("Ukuran keseluruhan elemn list dalam bytes = ",sys.getsizeof(var_list)*len(var_list))
print("Ukuran keseluruhan elemen NumPy dalam bytes = ", var_array.size*var_array.itemsize)

# --> IMPLEMENTASI MATRIKS

matriks = [[1, 0, 0, 0, 0], # contoh implementasi kode deklarasi matrik sekaligus menginisialisasikan nilai matriksnya sekaligus menggunakan metode nxm(baris x kolom)
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1]]

print(matriks)


matriks = [[0 for j in range(4)] for i in range(3)] # contoh implementasi kode deklarasi matriks dengan nilai default dengan menggunakan dua metode sekaligus dengan nested list dan nested for(for bersarang)

print(matriks)


var_mat = [[1, 2, 3, 4, 5], # contoh penerapan kode operasi matriks dengan membuat matriks 2x2
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]

print(var_mat[2][2])

var_mat = [[5, 0],
           [1, -2]]
def_mat = [[0 for j in range(2)] for i in range(2)]

for i in range(len(var_mat)):
    for j in range(len(var_mat)):
        def_mat[i][j] = var_mat[i][j]*2

print(def_mat)


import numpy as np

var_mat = np.array([[5, 0],
                   [1, -2]])

result = var_mat * 2

print(result)

import numpy

var_mat = np.array()





