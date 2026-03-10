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