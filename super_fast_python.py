#!/usr/bin/python3

import numpy as np
import sum_f
import ctypes
from timeit import default_timer as timer

print("Generate the array")
array_size = 100000000
array = np.random.randint(0, 2, size=array_size)

## Fortan sum 

start = timer()
f_result = sum_f.sum(array, len(array))
end = timer()
fortran_exe_time = end - start
print(f"Fortran sum: {f_result}")
print(f"Fortran execution time: {fortran_exe_time:.3E}")


## C sum

c_int_array = np.ctypeslib.ndpointer(dtype=np.int64, ndim=1, flags='C')

lib = np.ctypeslib.load_library('sum.so', '.')
parallel_lib = np.ctypeslib.load_library('parallel_sum.so', '.')
lib.sum.argtypes = [c_int_array, ctypes.c_int]
parallel_lib.sum.argtypes = [c_int_array, ctypes.c_int]

start = timer()
c_result = lib.sum(array, len(array))
end = timer()
c_exe_time = end - start
print(f"C sum: {c_result}")
print(f"C execution time: {c_exe_time:.3E}")

start = timer()
c_result = parallel_lib.sum(array, len(array))
end = timer()
c_exe_time = end - start
print(f"C sum parallel: {c_result}")
print(f"C execution time parallel: {c_exe_time:.3E}")

## numpy sum

start = timer()
np_sum = np.sum(array)
end = timer()
np_time = end - start
print(f"Numpy sum: {np_sum}")
print(f"Numpy execution time: {np_time:.3E}")

## python sum
test_python = False

if test_python:
    
    start = timer()
    sum_value = 0
    for value in array:
        sum_value += value
    end = timer()

    python_exe_time = end - start

    print(f"Python sum: {sum_value}")
    print(f"Python execution time {python_exe_time:.3E}")

