# Python Variables

## Tentang Variabel

Variabel adalah sebuah wadah atau _container_ yang digunakan untuk menyimpan sebuah nilai.

### Membuat sebuah varibel

Python tidak memiliki sebuah kata kunci khusus yang digunakan untuk mendeklarasikan sebuah variabel.

Variabel otomatis dibuat setelah nilai pada variabel dimasukan.

contoh:

```Python
x = 5
y = 10
print(x * y)
```

Variabel pada python bersifat dinamis.

Tipe nilai sebuah variabel dapat diubah sesuai dengan kebutuhan dari pertama kali diset.

contoh:

```Python
a = 10
b = 3.14
c = 'nama'
d = False
```

## Casting

_Casting_ adalah kondisi dimana ketikan kita hendak melakukan set terhadap variabel dengan tipe data yang lebih spesifik.

contoh:

```Python
Angka = int(1) # ini adalah tipe data Integer
Teks = str('hello world') # ini adalah tipe data String
Desimal = float(3) # ini adalah tipe data Float, 3.00 / 3.0
Desimal = float(3, 4) # ini adalah tipe data Float, 3.0000
```

## Mengetahui tipe data dari sebuah variabel

Untuk mengetahui tipe data dari sebuah varibel, dapat menggunakan operator `type()`.

contoh:

```Python
Nama = "Budi"
Usia = 25

print(type(Nama))
print(type(Usia))
```

# Perlu diketahui

Ketika berkenaan dengan tipe data string, dapat menggunakna `'` _single-qoute_ atau `"` _double-qoute_ sebagai pembungkus string.

Penamaan variabel di python case-sensitive, artinya nama variabel tidak dapat sama persis satu dan lainnya.

Dapat dibedakan dengan penggunaan kapitalisasi yang berbeda.

contoh

```Python
NamaLengkap = "Budi Sudarsono"
namaLengkap = "Budi Sudarsono"
namalengkap = "Budi Sudarsono"

print(NamaLengkap)
print(namaLengkap)
print(namalengkap)
```

## Penamaan dalam Variabel

Sebuah variabel dapat dimuat denga penamaan yang singkat seperti x atau y.

Namun sangat disarankan menggunakan kata yang deskriptif dengan isi sebuah variabel.

Aturan penulisan nama variabel di Python:

- Nama variabel harus didahului dengan sebauh _huruf_ atau _underscore_ `_`.
- Nama variabel tidak bisa dimulai dengan angka atau bilangan.
- Penamaan varibel hanya mencakup karakter _alpha-numeric_ saja, (A-Z, a-z, 0-9 dan \_).
- Pemaknaan nama yang mengandung case-sensitive, variable _nama_ dengan _Nama_ itu berbeda, meski memiliki makna yang sama.
- Sebuah nama varibel di Python tidak boleh menggunakan suatu keyword yang ditetapkan dalam bahasa pemrograman Python.

contoh

```Python
myVar = 'John'
MyVar = 'John'
myvar = 'John'
_myVar = 'John'
my_Var = 'John'
MyVar2 = 'John'
```

Jika penamaan sebuah varibel lebih dari satu kata, terdapat beberapa format yang bisas digunakan:

contoh:

```Pyton
# Camel-Case
namaDepan = "John"

#Pascal-Case
NamaBelakang = "Doe"

#Snake-case
nama_lengkap = "John Doe"
```

## Multiple value untuk beberapa varibel

Di Pytho, bisa membuat variabel secara sekaligus.

contoh:

```Python
x, y, z = "Jeruk", "Mangga", "Apel"
print(x)
print(y)
print(z)
```

Jika hendak mengisi value varibel secara bersamaan harus dilakukan secara ber-urutan.

Bisa juga satu value untuk beberapa variabel

contoh:

```Python
j, k, l = "Leci"

print(j)
print(k)
print(l)
```

## Unpack value

Kondisi ini dilakukan untuk tipe data _list_, _tuple_ dan lainnya.

Digunakan untuk mengekstrak nilai yang terdapat didalamnya.

Disebut juga sebagai _unpacking_.

contoh:

```Python
fruits = ["Apple", "Orange", "Mango"]
e, f, g = fruits
print(e)
print(f)
print(g)
```

Dengan catatan harus berurutan.

## Output varibel

Ketika hendak mencetak sebuah nilai variabel, biasanya menggunakna print statement untuk satu varibel.

contoh:

```Python
MyCar = "Mercedez"
print(MyCar)
```

Tetapi juga bisa mencetak beberapa value varibel secara bersamaan.

contoh:

```Python
CarOne = "Mercedez"
CarTwo = "Renault"
CarThree = "Audi"

print(CarOne, CarTwo, CarThree)
```

Bisa juga untuk kebutuhan operasi, seperti _arithmetic_ atau _string-concatenation_.

## Global Variabel

Dalam penempatan sebuah varibel, terdapat istilah _global-varible_ yang artinya varibel tersebut tidak dibuat didalam sebuah fungsi, melainka diluar sebuah fungsi.

Variabel seperti itu, dapat digunakan atau dipanggil oleh fungsi mana pun, dengan catatan berada diluar fungsi yang memanggilnya.

Dapat juga berada dalam sebuah fungsi, dengan catatan hanya dianggap fungsi global untuk fungsi didalam sebuah fungsi, _inner global-varible_

contoh:

```Python

# Global Varibel
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# Inner Global Varible
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
```

Jika Anda membuat variabel dengan nama yang sama di dalam sebuah fungsi, variabel ini akan bersifat lokal dan hanya dapat digunakan di dalam fungsi tersebut. Variabel global dengan nama yang sama akan tetap seperti semula, global dan dengan nilai aslinya.

## Kata kunci global

Biasanya, ketika membuat variabel di dalam sebuah fungsi, variabel tersebut bersifat lokal dan hanya dapat digunakan di dalam fungsi tersebut.

Untuk membuat variabel global di dalam sebuah fungsi, dapat menggunakan kata kunci `global`.

contoh:

```Python
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```

Selain itu, gunakan kata kunci global jika Anda ingin mengubah variabel global di dalam sebuah fungsi.
