# --> PEMROSESAN SEKUENSIAL PADA PYTHON

var_arr = [1, 2, 3, 4, 5] # conthoh penerapan kodenya

for i in range(len(var_arr)):
    current_element = var_arr[i] # indexing
    next_index = i+1 # suksor indeks

    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None

    print(f"Current element: {current_element}, next_element: {next_element}")


# --> LATIHAN ARRAY

var_arr = [1, 7, 2, 89, 3] # latihan array studi kasus mencari nilai elemen terbesar dengan menggunakan two pointers (left/rigt)
left_pointer = var_arr[0]

for i in range(1, len(var_arr)):
    right_pointer = var_arr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer

print(left_pointer)
