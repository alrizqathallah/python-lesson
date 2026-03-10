# Python Booleans

## Nilai Boolean

Nilai boolean hanya merepresentasikan 2 nilai, yaitu `True` dan `False`.

Dalam pemrograman, nilai boolean akan sangat sering dipergunakan untuk membangun sebuah kondisi yang dibutuhkan.

Seperti `if` statement, dimana hanyan akan menerima nilai `True` atau `False`.

Nilai true dan false akan menentukan nilai apa yang akan kembalikan nantinya.

contoh:

```Python
print(10 > 5) # True, karena 10 lebih besar dari 5
print(10 < 5) # False, karena 10 lebih besar dari 5
print(10 == 10) # True, kerana 10 sama besar dengan 10
# integer dan string
print(10 == "10") # False, 10 sama besar dengan 10, namun keduanya berbeda dalam tipe data.
```

Dalam `if` statement, nilai boolean menjadi penentu return yang akan dikembalikan.

contoh:

```Python
x = 100
y = 10

if x > y:
  print(f"Nilai {x} lebih besar dari nilai {y}")
else:
  print(f"Nilai {x} tidak lebih besar dari nilai {y}")
```

## Mengevaluasi Value dan Variable

Method `bool()` dapat digunakna untuk mengecek sebuah nilai itu bersifat *Truthy* atau *Falsy*.

Jika yang dikembalikan adalah True, maka nilai tersebut bersifat Truthy.

Namun jika yang dikembalikan adalah False, maka nilai tersebut bersifat Falsy.

contoh:

```Python
print(bool(10)) # Truthy
print(bool("10")) # Truthy
print(bool(0)) # Falsy
print(bool("")) # Falsy
```

*Truthy* adalah nilai yang bersifat True. Sementara *Falsy* adalah nilai yang bersifat False.