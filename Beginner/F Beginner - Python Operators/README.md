# Python Operators

## Operators

Dalam Python, operator digunakan untuk menampilkan operasi yang dilakukan pada nilai sebuah variabel.

Berikut operasi penjumlahan yang dapat dilakukan dengan operator `+`.

contoh:

```Python
print(2 + 2) # 4

x = 5
y = 10

print(x + y) # 15

z = x + y

print(z)
```

### Jenis Operator di Python

- Operator Matematika (Arithmetic)
- Operator Penugasan (Assignment)
- Operator Perbadingan (Comparasion)
- Operator Logika (Logical)
- Identity Operator
- Membership Operator
- Bitwise Operator

## Operator Matematika

Operator matematika di Python, digunakan untuk mengoperasikan nilai numerik (bilangan).

- Addition `+` = x + y
- Subtraction `-` = x - y
- Multiplication `*` = x \* y
- Division `/` = x / y
- Modulus `%` = x % y
- Exponentiation `**` = x \*\* y
- Floor Division `//` = x // y

contoh:

```Python
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y) # Float
print(x % y)
print(x ** y)
print(x // y) # Integer
```

### Pembagian (Division) di Python

Python memiliki 2 jenis pembagian

- `/` Division, akan mengembalikan nilai dalam bentuk `float`.
- `//` Floor Division, akan mengembalikan nilai dalam bentuk `Integer`.

## Operator Penugasan

Operator penugasan, digunakan untuk menugaskan sebuah value (nilai) kedalam sebuah variabel.

contoh:

```Python
# =
x = 5 # sama dengan x = 5

# +=
x += 5 # sama dengan x = x + 5

# -=
x -= 5 # sama dengan x = x - 5

# *=
x *= 5 # sama dengan x = x * 5

# /=
x /= 5 # sama dengan x = x / 5

# %=
x %= 5 # sama dengan x = x % 5

# **=
x **= 5 # sama dengan x = x ** 5

# //=
x //= 5 # sama dengan x = x // 5

# &=
x &= 5 # sama dengan x = x & 5

# |=
x |= 5 # sama dengan x = x | 5

# ^=
x ^= 5 # sama dengan x = x ^ 5

# >>=
x >>= 5 # sama dengan x = x >> 5

# <<=
x <<= 5 # sama dengan x = x << 5

# :=
print(x := 3) # sama dengan x = 3, print(x)
```

### Operator Walrus

Mulai python versi 3.8, diperkenalkan operator bernama "walrus operator".

Fungsi yang memberikan nilai pada varibel sebagai bagian ekspresi yang lebih besar.

contoh:

```Python
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
  print(f"List has {count} elements")
```

## Operator Perbandingan

Operator perbandingan digunakan untuk membandingkan 2 buah nilai.

Hasil operasi dengan operator perbandingan akan mengambalikan value boolean, True atau False.

contoh:

```Python
# ==
x == y

# !=
x != y

# >
x > y

# <
x < y

# >=
x >= y

# <=
x < y

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
```

## Operator Logika

Operator logika digunakan untuk mengkombinasikan sebuah statement pengkondisian

contoh:

```Python
# and
x = 5

print(x > 0 and x < 10)

# or
x = 5

print(x < 5 or x > 10)

# not
x = 5

print(not(x > 3 and x < 10))
```

- `and`, Jika ada dua nilai bernilai True maka hasil dari operasi tersebut akan bernilai True. Jika satu saja bernilai False baik diawal atau selanjutnya, maka akan bernilai False.

- `or`, Kebalikan dari `and`, jika ada satu nilai saja bernilai True, maka hasilnya akan True, meski nilai lainnya adalah False.

- `not`, not adalah operator yang membalikan sebuah nilai, jika True akan dinilai False, dan False akan dinilai sebagai True.

## Operator Identitas (Identity)

Di python ada dua operator identitas, `is` dan `is not`.

`is` Operator ini mengembalikan nilai True jika kedua variabel menunjuk ke objek yang sama (memiliki alamat memori yang sama).

`is not` Kebalikan dari is. Operator ini mengembalikan nilai True jika kedua variabel menunjuk ke objek yang berbeda, meskipun isinya mungkin identik.

contoh:

```Python
# Membuat dua list dengan isi yang sama
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True (Isinya sama)
print(a is b)   # False (Objeknya berbeda di memori)
print(a is c)   # True (c merujuk ke objek yang sama dengan a)

# is not
x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)
```

Perbedaan Penting: 

`==` vs `is`

Seringkali pemula bingung antara `==` (operator perbandingan) dan `is` (operator identitas). Berikut perbandingannya:

`==` menyamakan nilai (value), memeriksa apakah sebuah objek atau variabel memiliki nilai yang sama.

`is` menyamakan identitas (variabel), memeriksa apakah sebauh objek atau variabel berada dalam alamat memori yang sama.

## Operator Membership

Jika operator identitas itu memastikan sebuah variabel, operator membership berguna untuk memvalidasi sebuah value atau variabel merupakan sebuah urutan (strings, list, tuple, atau dictionary).

### Operator `in`.

Operator `in` akan mengembalikan nilai True, jika nilai yang dicari berada dalam urutan atau sebuah objek.

Kita gambarkan dengan `list` buah-buahan

contoh:

```Python
fruits = ["Orange", "Mango", "Apple"]
print("Mango" in fruits)
# Jika "Mango" ada didalam list, maka akan mengembalikan nilai True.
# Jika tidak, akan mengembalikan nilai False
```

### Operator `not in`.

Operator `not in` adalah kebalikan dari in.

Operator ini memastikan sebuah value tidak berada didalam objek.

contoh:

```Python
cars = ["Mercedez-Benz", "BMW", "Audi"]
print("BMW" not in cars)
# Jika "BMW" ada didalam list, maka hasil yang dikembalikan adalah False.
# Sebaliknya, jika "BMW" tidak ada dialam list, maka akan mengembalikan nilai True.
```

### Cara kerja pada sebauh tipe data.

Dalam tipe data string, operator membership dapat digunakan untuk mengecek elemen pada string.

contoh:

```Python
String = "Hello Python".lower()
print("py" in String) # True
print("z" in String) # False
# Mengecek apakah elemen "py" ada didalam String.
```

Didalam `list` dan `tuple`.

Operator membership mengecek apakah ada nilai yang dimaksud berada didalam objek.

contoh:

```Python
List = ["Ronaldo", "Messi", "Neymar"].lower()
Tuple = ("Rossi", "Stoner", "Pedrossa").lower()

print("Ronaldo" in List)
print("Kaka" in List)

print("Stoner" in Tuple)
print("Marquez" in Tuple)
```

Operator membership untuk tipe data Dictionary.

Bertugas untuk mengecek, apakah sebuah *key* ada dialam dictionary.

contoh:

```Python
Dictionary = {"Nama": "Ujang Rambo", "usia": 20, "Alamat": "Bandung"}
print("Nama" in Dictionary)
```

**Penting** dalam dictionary, operator membership hanya memastikan sebuah *key* tersedia atau ada dalam sebuah objek dictionary.
**Penting** operator membership menerapkan *case-sensitivity*.

### Contoh Kasus

```Python
username = ['admin', 'root', 'tester', 'superuser']
new_username = 'admin'

if new_username in username:
  print(f'Sorry, your username: {new_username} cannot be used!')
else:
  print(f'your username: {new_username} can be used!')
```

## Opeartor Bitwise

Jika operator logika bekerja dengan nilai True atau False, Operator Bitwise bekerja jauh lebih dalam, yaitu di level biner (0 dan 1). Operator ini memanipulasi angka bulat (integer) dengan cara membandingkan atau menggeser bit-bit penyusunnya.

Bayangkan Anda sedang membedah sebuah angka untuk melihat mesin di dalamnya. Misalnya, angka 5 dalam biner adalah 0101, dan angka 3 adalah 0011.

Berikut adalah 6 operator bitwise di Python:

- AND (&)
Membandingkan tiap bit; hasilnya 1 hanya jika kedua bit bernilai 1.

- OR (|)
Hasilnya 1 jika salah satu atau kedua bit bernilai 1.

- XOR (^)
Hasilnya 1 jika bitnya berbeda. Jika sama (keduanya 0 atau keduanya 1), hasilnya 0.

- NOT (~)Membalikkan semua bit (0 jadi 1, 1 jadi 0). Di Python, ini menggunakan rumus $-(x + 1)$.

- Shift Left (<<)Menggeser bit ke kiri dan mengisi bagian kanan dengan nol. Ini sama dengan mengalikan angka dengan $2^n$.

- Shift Right (>>)Menggeser bit ke kanan. Ini sama dengan membagi angka dengan $2^n$ (pembulatan ke bawah).

### Kapan Kita Menggunakannya?
Meskipun jarang digunakan dalam pembuatan aplikasi web biasa, operator bitwise sangat krusial dalam:

- Kompresi data dan enkripsi.

- Pemrograman sistem (low-level) atau hardware/IoT.

- Grafika Komputer untuk manipulasi warna (RGB).

- Optimasi performa pada algoritma tertentu.

## Operator Presedence

Operator Precedence (Urutan Hierarki Operator) adalah aturan yang menentukan operator mana yang akan dieksekusi lebih dulu dalam sebuah ekspresi matematika atau logika.

Sama seperti aturan KABATAKU (Kali, Bagi, Tambah, Kurang) dalam matematika sekolah, Python juga memiliki tingkatan prioritas agar hasil perhitungan tidak membingungkan.

Urutan Prioritas (Dari Tertinggi ke Terendah)
Berikut adalah tabel operator dari yang paling kuat (dikerjakan duluan) hingga yang paling lemah:

- `()` Tanda kurung, selalu nomor 1
- `**` Exponent (pangkat)
- `*`, `/`, `%` dan `//`
- `+` dan `-`
- Operator Perbandingan, Identitas, dan Membership
- `not`
- `and`
- `or`