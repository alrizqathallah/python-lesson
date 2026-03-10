# Python Lists

## List

Dalam python, *list* merupakan tipe data yang digunakan untuk menyimpan banyak nilai.

List merupakan satu dari empat tipe data bawaan di python yang dapat digunakan untuk mengkoleksi data dalam satu variabel. Selain *Tuple*, *Dictionary* dan *Set*.

Nilai dari list ditampung dalam *square-bracket* `[]`, yang ditugaskan pada variabel.

contoh:

```Python
# Membuat list
this_list = ["List", "Tuple", "Dictionary", "Set"]
print(this_list)
```

## List Items

Nilai yang ditampung pada list disebut dengan *item* list.

Item list berurut, dapat diganti, dan dimungkinkan untuk duplikasi.

Urutan dalam list mengikuti konsep array, list pertama dimulai dari index [0] dan index kedua adalah [1].

### Berurutan

Dalam konteks berurutan yang dimaksud dalam list adalah, dimana ketika sebuah item list sudah didefinisikan dari awal dengan urutan yang tetap, maka urutan tersebut tidak dapat diubah.

Seperti suatu item yang didefinisikan dalam urutan pertama, tidak bisa diganti ke urutan kedua atau seterusnya, dan item baru akan menempati urutan yang paling akhir.

### Dapat diganti

Item pada suatu list tidak dapat diubah secara urutan setelah terdefinisi.

Namun untuk nilai item yang didefinisikan tersebut dapat diganti, seperti item A dapat diganti dengan item B.

### Dimungkinkan untuk diduplikasi

Nilai pada item list tidak harus berbeda.

Item list tetap dapat dibuat meski terdapat nilai yang sama antar item.

contoh:

```Python
# List Items
fruits = ["Apple", "Mango", "Cherry", "Apple", "Mango"]
print(fruits)
```

## Panjang List (List Length)

Panjang list yang dibuat dapat diketahui.

Dengan menggunakan fungsi `len()`.

contoh:

```Python
# Panjang list
fruits = ["Apple", "Mango", "Cherry", "Apple", "Mango"]
print(len(fruits))
```

## Tipe Data pada List

List dapat menampung berbagai tipe data

contoh: 

```Python
# Tipe Data
name = ["Bambang", "Budi", "Zaenal", "Rachmat"]
age = [27, 27, 26, 23]
height = [1.7, 1.73, 1.75, 1.75]

print(name)
print(name)
print(name)

profile = ["Bengs", 28, 1.81]
print(profile)
```

Jika kita coba cek masing-masing list dengan menggunakan method `type()`.

Hasil yang dikembalikan adalah `list`, karena python mendefinisikan list dengan tipe data list.

## List Constructor

Kita juga dapat membuat list dengan menggunakan constructor.

Dengan konstruktor `list()`

contoh:

```Python
# List Constructor
the_list = list(("Bengs", 28, 1.81))
print(the_list)
```