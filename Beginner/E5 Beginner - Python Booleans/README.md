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
# Falsy
print(bool([]))
print(bool(()))
print(bool({}))
# Falsy
print(bool(False))
print(bool(None))
```

*Truthy* adalah nilai yang bersifat True. Sementara *Falsy* adalah nilai yang bersifat False.

Semua nilai, baik itu number atau string bersifat True.

Dikecualikan, dalam number semua number bersifat Truthy, kecuali bilangan 0 yang bersifat Falsy.

Dalam string, semua string bersifat Truthy, kecuali *empty-string* atau string kosong `""` bersifat Falsy. 

String kosong `""` berbeda dengan `" "`, untuk string kosong adalah string yang benar-benar tidak memiliki isi atau elemen string didalamnya. Meskipun sebuah string hanya berisikan *spasi*, seolah terlihat seperti string kosong, akan tetap dinilai True, meski elemen didalamnya hanay spasi saja.

Semua tipe data *list*, *tuple*, *dict* bersifat True, kecuali data tersebut kosong, maka akan bernilai False.

Jika kita memiliki kelas *class*, kemudian *object* yang mengembalikan nilai False atau 0, akan dinilai sebagai Falsy value.

contoh:

```Python
class myClass():
  def __len__(self):
    return 0

myObj = myClass()
print(bool(myObj))
```

## Functions bisa mengembalikan nilai Boolean

Dalam python dapat membuat function yang bisa mengembalikan nilai boolean.

Dari hasil atau nilai yang dikembalikan oleh functions, kita bisa melakukan kondisional setelahnya berdasarkan nilai yang dikembalikan.

contoh:

```Python
def myFunction():
  return True

print(myFunction())

if myFunction():
  print("YES!")
else:
  print("NO!")
```

## Tambahan

Python juga memiliki method bawaan untuk mengembalikan nilai boolean, dengan menggunakan `isinstance()`.

Digunakan untuk mengetahui sebuah objek memiliki tipe data tertentu.

contoh:

```Python
x = 1000
print(isinstance(x, int)) # True
print(isinstance(x, str)) # False
```