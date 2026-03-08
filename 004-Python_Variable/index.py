x = 5
y = 10
print(x * y)

a = 10
b = 3.14
c = 'nama'
d = False

Angka = int(1) # ini adalah tipe data Integer
Teks = str('hello world') # ini adalah tipe data String
Desimal = float(3) # ini adalah tipe data Float, 3.00 / 3.0

print(Desimal)

Nama = "Budi"
Usia = 25

print(type(Nama))
print(type(Usia))

# Case-Sensitive
NamaLengkap = "Budi Sudarsono"
namaLengkap = "Budi Sudarsono"
namalengkap = "Budi Sudarsono"

print(NamaLengkap)
print(namaLengkap)
print(namalengkap)

# Contoh penamaan varibel
myVar = 'John'
MyVar = 'John'
myvar = 'John'
_myVar = 'John'
my_Var = 'John'
MyVar2 = 'John'

# Camel-Case
namaDepan = "John"

#Pascal-Case
NamaBelakang = "Doe"

#Snake-case
nama_lengkap = "John Doe"

x, y, z = "Jeruk", "Mangga", "Apel"
print(x)
print(y)
print(z)

j = k = l = "Leci"
print(j)
print(k)
print(l)

#unpacking
fruits = ["Apple", "Orange", "Mango"]
e, f, g = fruits
print(e)
print(f)
print(g)

# print multiple variable in one print statement
CarOne = "Mercedez"
CarTwo = "Renault"
CarThree = "Audi"

print(CarOne, CarTwo, CarThree)

"""
Jika Anda membuat variabel dengan nama yang sama di dalam sebuah fungsi, variabel ini akan bersifat lokal dan hanya dapat digunakan di dalam fungsi tersebut. Variabel global dengan nama yang sama akan tetap seperti semula, global dan dengan nilai aslinya.
"""

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)