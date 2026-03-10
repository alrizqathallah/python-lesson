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

### List Items

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

### Panjang List (List Length)

Panjang list yang dibuat dapat diketahui.

Dengan menggunakan fungsi `len()`.

contoh:

```Python
# Panjang list
fruits = ["Apple", "Mango", "Cherry", "Apple", "Mango"]
print(len(fruits))
```

### Tipe Data pada List

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

### List Constructor

Kita juga dapat membuat list dengan menggunakan constructor.

Dengan konstruktor `list()`

contoh:

```Python
# List Constructor
the_list = list(("Bengs", 28, 1.81))
print(the_list)
```

## Access List Items

List item dapat diakses dengan mengacu pada urutan indexnya.

contoh:

```Python
# Access List
cars = ["Mercedez", "BMW", "Audi", "Volkswagen", "Porsche"]
print(cars[1]) # BMW
```

Untuk mengakses item pada list, juga dapat menggunakan minus indexing.

contoh:

```Python
# Access List
cars = ["Mercedez", "BMW", "Audi", "Volkswagen", "Porsche"]
print(cars[1]) # BMW
print(cars[-1]) # Porsche
print(cars[-2]) # Volkswagen
```

Selain menggunakan minus indexing, juga dapat menggunakn range indexing

contoh:

```Python
# Access List
cars = ["Mercedez", "BMW", "Audi", "Volkswagen", "Porsche"]
print(cars[1]) # BMW
print(cars[-1]) # Porsche
print(cars[-2]) # Volkswagen
print(cars[1:4]) # "BMW", "Audi", "Volkswagen",
print(cars[:4]) # "Mercedez", "BMW", "Audi", "Volkswagen"
print(cars[1:]) # "BMW", "Audi", "Volkswagen", "Porsche"
print(cars[-4:-1]) # "BMW", "Audi", "Volkswagen"
```

Kita juga dapat mengecek, apakah sebuah item ada dalam list.

contoh:

```Python
# Access List
cars = ["Mercedez", "BMW", "Audi", "Volkswagen", "Porsche"]
if "Mercedez" in cars:
  print("Mercedez, exist!")
else:
  print("Mercedez, doesn't exist!")
```

## Change List Items

### Merubah nilai item pada list

Untuk mengganti nilai pada item, perlu spesifik pada index item.

contoh:

```Python
# Mengganti nilai item
ballon_dor = ["Messi", "Ronaldo", "Mbappe", "Halland", "Bengs"]
print(ballon_dor)

ballon_dor[4] = "Alrizq"
print(ballon_dor)

ballon_dor[2:4] = ["Vini", "Pedri"]
print(ballon_dor)
```

### Insert items

Untuk mengganti nilai item, selain langsung mengganti melalui index.

Bisa menggunakan fungsi `insert()`

contoh:

```Python
# Mengganti nilai item
ballon_dor = ["Messi", "Ronaldo", "Mbappe", "Halland", "Bengs"]
print(ballon_dor)

ballon_dor[4] = "Alrizq"
print(ballon_dor)

ballon_dor[2:4] = ["Vini", "Pedri"]
print(ballon_dor)
```

## Menambahkan list items

### Append

`.append()` merupakan method yang digunakan untuk dinambahkan satu item ke akhir list

Merupakan metode yang paling umum digunakan.

Hanya menambahkan 1 elemen saja.

contoh:

```Python
# Append Items
formula_one = ["RedBull", "Mercedez", "Ferrari", "Audi", "McLaren", "Aston Martin", "Renault"]
formula_one.append("Alpine")

print(formula_one)
```

### Insert

`.insert()` dapat digunakan item secara lebih spesifik.

Index dapat ditentukan, dengan menetapkan index yang dituju dan nilai yang dimasukan.

contoh: 

```Python
# Insert Items
formula_one = ["RedBull", "Mercedez", "Ferrari", "Audi", "McLaren", "Aston Martin", "Renault"]
formula_one.insert(1, "Alpine")

print(formula_one)
```

### Extend

Dengan method `.extend()` memungkinkan untuk menambahkan banyak item dari list yang berbeda atau tipe data iterable lainnya. 

Item tersebut akan ditambahkan dibagian akhir.

contoh:

```Python
# Extend
formula_one = ["RedBull", "Mercedez", "Ferrari", "Audi", "McLaren", "Aston Martin", "Renault"]
moto_gp = ["Ducati", "Honda", "Yamaha", "KTM", "Aprilia"]
formula_one.extend(moto_gp)

print(formula_one)
```

### Operator concatenation

Selain menggunakan operator diatas, kita juga dapat menambahkan item dengan menggunakan operator concate `+`.

contoh:

```Python
# concatenation
formula_one = ["RedBull", "Mercedez", "Ferrari", "Audi", "McLaren", "Aston Martin", "Renault"]
moto_gp = ["Ducati", "Honda", "Yamaha", "KTM", "Aprilia"]

grand_prix = formula_one + moto_gp

print(grand_prix)
```

## Menghapus List items

