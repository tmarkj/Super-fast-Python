# Super-fast-Python

Here is a simple example of interfacing your Python with C and Fortran. 
This allows for Python to call much faster languages to handle the heavy lifting. 
The more complicated tasks of plotting or reading in data can be handled in Python.
Anything where a loop is needed (and it's too hard to get to work with Numpy) can be written in C or Fortran.

Note that this is only tested in Linux. 
I have no idea how to get this to work in Windows.

## Dependencies

* NumPy
* gcc
* make

## Compiling Fortran with f2py

This is the command I used to compile the fortran file:

```
f2py -c -m sum_f sum.f95
```
