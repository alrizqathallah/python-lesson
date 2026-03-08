# Python Syntax

## Eksekusi Sintaks Python

Sintaks python dapat dieksekusi langsung melalui Python CLI (Command Line Interface) yang berbasis terminal.

- Pada terminal dengan `python` atau `python 3`
- `print('Hello World')`

## Indentasi pada Python

Indentasi mengacu pada spasi yang muncul diawal baris.
Python menggunakan format indentasi untuk membatasi blok kode, berbeda dengan bahasa pemrograman lain yang menggunakan `{}` atau `()`.
Dalam bahasa lain, indentasi hanya digunakan untuk meningkatkan readability saja, namun di Python, indentasi sangat penting dan krusial.

contoh:

```Python
if 4 > 2:
  print('Four is greater than two')
```

```Python
if 5 > 2:
  print('Five is greater than two')
  if 4 < 5:
    print('Four is smaller than five')
```

## Variabel di Python

Dalam python, variabel ditetapkan setelah dinilai dimasukan.

contoh:

```Python
nama = "Budi"
x = 5
isStudent = True
```

Python tidak menggunakan kata kunci secara khusus untuk mendeklarasikan dan mengisi nilai dalam variabel.

## Komentar di Python

Komentar adalah sebuah fungsi yang digunakan untuk memberikan catatan pada kode yang ditulis.

Komentar tidak akan dibaca / akan di abaikan oleh interpreter, sehingga tidak akan ikut tampil pada output.

Python menggunakan # 'pawn' untuk memberi komentar pada kode.

contoh:

```Python
# This is comment

x = 4 # This is a variabel

print(x)
# This si print statement
```

## Statement

*Statement* adalah satu baris atau sekumpulan instruksi / kode program, yang akan dieksekusi oleh komputer.

Contoh, `print()` statement:

```Python
print('Hello World')
```

Komputer akan mengeksekusi perintah (statement) print tersebut.

Statement akan dieksekusi satu per satu (baris per baris).

contoh:

```Python
print('Ini adalah statement pertama')
print('Ini adalah statement kedua')
print('Ini adalah statement ketiga')
```

statement akan dieksekusi oleh komputer, baris per baris, dari statement pertama ke statement ketiga.

## Penutup Statement

Dalam Python, tidak dibutuhkan penutup statement seperti *semicolon* `;` , 

Hanya dalam kasus tertentu kita dapat memanfaatkannya sebagai pembatas antar statement yang dikesekusi dalam baris yang sama.

contoh:
```Python
print('Ini pertama'); print('ini kedua'); print('ini ketiga')
```