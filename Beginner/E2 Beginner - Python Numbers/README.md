# Python Number

## Tipe Data Numerik (Bilangan)

Terdapat 3 tipe data numerik di Python:

- `str`
- `float`
- `complex`

Tipe data otomatis terdefinisi ketika value di-assign kedalam variabel.

contoh:

```Python
x = 5 # int
y = 3.14 # float
z = 1j # complex
```

Guna memverifikasi data (tipe data) pada sebuah varibel, dapat menggunakan operator `type()`.

contoh:

```Python
x = 5 # int
y = 3.14 # float
z = 1j # complex

print(type(x))
print(type(y))
print(type(z))
```

## Integer `int`

Integer adalah bilangan angka bulat, baik itu positif atau negatif, tanpa koma (desimal), dan tidak terbatas.

contoh:

```Python
Int1 = 1
Int2 = 1234
Int3 = -12345678

print(type(Int1))
print(type(Int2))
print(type(Int3))
```

## Float `float`

Tipe data float, merupakan tipe data bilangan desimal, memiliki kome diakhir bilangan bulat

Bisa dalam bentuk positif, atau negatif.

contoh:

```Python
Float1 = 1.10
Float2 = 2.123456
Float3 = -3.456789

print(type(Float1))
print(type(Float2))
print(type(Float3))
```

Float juga bisa menampung bilangan kelipata 10 / atau `e`

contoh:

```Python
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
```

## Complex

Bilangan kompleks ditulis dengan huruf "j" sebagai bagain imajiner

contoh:

```Python
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
```

## Konversi Tipe Data

Sebuah varibel atau output dapat dikonversi kedalam suatu tipe data lain denga operator konversi

Seperti `int()`, `float()` dan `complex()`

contoh: 

```Python
Integer = 1    # int
Float = 2.8  # float
Complex = 1j   # complex

print(type(Integer))
print(type(Float))
print(type(Complex))

#convert from int to float:
a = float(Integer)

#convert from float to int:
b = int(Float)

#convert from int to complex:
c = complex(Integer)

print(type(a))
print(type(b))
print(type(c))
```

## Bilangan Acak

Python memiliki modul bawaan yang dapat membuat bilangan acak `random`

contoh:

```Python
import random

print(random.randrange(1, 10))
```