# Python Strings

## Strings

Tipe data string dibungkus menggunakan _quatation-mark_, baik itu `'` atau `"`.

Seperti `'hello'` atau `"hello"`.

Dapat membuat output langsung dengan string literal menggunakan `print()` statement.

contoh:

```Python
print('Hello')
print("Hello")
```

Dapat menggunakna quotation didalam quoatation, selagi tidak menggunakan quotation yang sama.

contoh:

```Python
print("It's Alright")
print("He is name is 'Cena'")
print('He is name is "Cena"')
```

### Assign String dalam varibel

Cukup memasukan string kedalam variabel, otomatis variabel dikenali sebagai tipe data string.

contoh:

```Python
name = "John"
print(name)
```

### Multiline String

Dalam python juga dapat membuat multiline string, menggunakan `"""` yang ditutup dengan `"""`.

contoh:

```Python
Teks = """Undang-undang dasar,
Negara Republik Indonesia
tahun 1945.
"""
print(Teks)
```

Bisa juga menggunakan single-qoute `'''`.

### String adalah Array

Seperti bahasa pemrograman lain, string adalah tipe data yang basisnya adalah array denagn karakter unik.

Namun python tidak memiliki tipe data karakter khusus, satu karakter diibaratkan sebagai string dengan panjang 1 (1-length).

Dengan menggunakna `[]` elemen string dapat diakses.

contoh:

```Python
welcome = 'Hello World'
print(welcome[1]) # 'e'
print(welcome[0]) # 'H'
print(welcome[5]) # ' '
```

### Perulangan "Looping" pada string

Dikarenakan string didasari oleh array, maka dapat dilakukan looping pada elemen string.

contoh:

```Python
for x in "Hello World":
  print(x)
```

### Panjang String

Dapat juga dilihat panjang dari sebuah string dengan menggunakna `len()`.

contoh:

```Python
a = "Hello World"
print(len(a))
```

### Mengecek sebuah kata dala sebuah string

Dengan operator `in` kita dapat mengecek apakah sebuah kata terdapat dalam sebuah susunan kalimant.

Hasilnya akan mengembalikan boolean `True` atau `False`.

contoh:

```Python
Greet = "Hello my name is Bengs, I am 28 years old right now"
print("Bengs" in Greet)
```

kita juga bisa mengolahnya dengan `if` statement.

contoh:

```Python
Greet = "Hello my name is Bengs, I am 28 years old right now"
if "Bengs" in Greet:
  print('Kata "Bengs" ada didalam susunan kalimat')
```

Kita juga bisa mengecek untuk memastikan sebuah kata tersebut tidak ada dalam kalimat.

Hasilnya akan mengembalikan boolean value, `True` atau `False`.

contoh:

```Python
Greet = "Hello my name is Bengs, I am 28 years old right now"
print("Ganteng" not in Greet)
```

## Python - Slicing Strings

### Slicing

Kita dapat mengembalikan string dalam rentan tertentu, disebut dengan slicing.

Menggunakan _square-bracket_ `[]` yang dipisah dengan _colon_ `:`.

contoh

```Python
h = "Hello World"
print(h[0:5])
print(h[6:11])
print(h[:5])
print(h[6:])
```

### Index Negatif

contoh:

```Python
h = "Hello World"
print(h[-5:-2])
```

## Modify Strings

### Uppercase

Python memiliki method bawaan yang dapat digunakan untuk membuat kalimat menjadi uppercase.

Menggunakan `.upper()`

contoh:

```Python
d = "Hello World"
print(d.upper())
```

### Lowercase

Python memiliki method bawaan yang dapat digunakan untuk membuat kalimat menjadi lowercase.

Menggunakan `.lower()`

contoh:

```Python
d = "Hello World"
print(d.upper())
```

### Remove / Menghilangkan whitespace

Jika dalam sebuah teks ada spasi kosong, baik di awal atau akhir, kita dapat menghilangkannya dengan method `.strip()`.

contoh:

```Python
j = "   Hello World "
print(j)
print(j.strip())
```

### Replacing String

Kita dapat juga mengganti elemen string tertentu dengan method `.replace()`.

contoh:

```Python
d = "Hello World"
print(d.replace("e", "o")) # Hollo World
```

### Split String

Di Python string dapat di split dan dikembalikan dalam bentuk `list`.

Menggunakan method `.split()`.

contoh:

```Python
d = "Hello, World"
print(d.split(","))
```

Dalam contoh diatas, kome `,` digunakan sebagai separator sebagai pembatas.

## String - Concate (Penggabungan)

### String Concatenation

String concatenation (concate) adalah menggabungkan 2 buah string menjadi satu string utuh.

Menggunakan operator `+`.

contoh

```Python
u = "Hello"
i = "World"
o = u + " " + i
print(o)
print(u + " " + i)
```

## Python. String - Format

Kita tidak bisa mengkombinasikan variabel dengan tipe data string dengan integer secara langsung.

Namun ada metode yang dapat digunakan untuk menyelesaikan permasalahan tersebut.

### F-Strings

Diperkenalkan pada Python 3.6, dan sekarang menjadi metode yang lebih disukai untuk memformat string.

Untuk melakukannya cukup dengan menempatkan huruf `f` didepan string literal, yang ditambah kurung kurawal.

Kurung kurawal `{}`, digunakan untuk menampung varibel dan operasi yang dibutuhkan.

contoh:

```Python
usia = 28
pesan = f"Usia saya adalah {usia}"
print(pesan)
```

### Placeholder dan Modifier

Kurung kurawal pada F string berfungsi sebagai placeholder.

Placeholder dapat berisikan variabel, function, operator untuk melakukan operasi.

contoh:

```Python
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)
```

## Escape Characters

### Escape sequence

Escape sequence digunakan untuk dapat menyisipkan karakter yang tidak dapat diterima dalam sebuah string.

karakter Escape didahului dengan `\`, yang diikuti karakter sequence.

contoh:

```Python
teks = "Ini dikuti dari \"Dia\""
print(teks)
```

Beberapa contoh escape character

- \' = single quote
- \\ = Backslash
- \n = New line
- \r = Carriage Return
- \t = Tab
- \b = Backspace
- \f = Form Feed
- \ooo = Octal Value
- \xhh = Hex value

## String Methods

- capitalize()	Converts the first character to upper case
- casefold()	Converts string into lower case
- center()	Returns a centered string
- count()	Returns the number of times a specified value occurs in a string
- encode()	Returns an encoded version of the string
- endswith()	Returns true if the string ends with the specified value
- expandtabs()	Sets the tab size of the string
- find()	Searches the string for a specified value and returns the position of where it was found
- format()	Formats specified values in a string
- format_map()	Formats specified values in a string
- index()	Searches the string for a specified value and returns the position of where it was found
- isalnum()	Returns True if all characters in the string are alphanumeric
- isalpha()	Returns True if all characters in the string are in the alphabet
- isascii()	Returns True if all characters in the string are ascii characters
- isdecimal()	Returns True if all characters in the string are decimals
- isdigit()	Returns True if all characters in the string are digits
- isidentifier()	Returns True if the string is an identifier
- islower()	Returns True if all characters in the string are lower case
- isnumeric()	Returns True if all characters in the string are numeric
- isprintable()	Returns True if all characters in the string are printable
- isspace()	Returns True if all characters in the string are whitespaces
- istitle()	Returns True if the string follows the rules of a title
- isupper()	Returns True if all characters in the string are upper case
- join()	Joins the elements of an iterable to the end of the string
- ljust()	Returns a left justified version of the string
- lower()	Converts a string into lower case
- lstrip()	Returns a left trim version of the string
- maketrans()	Returns a translation table to be used in translations
- partition()	Returns a tuple where the string is parted into three parts
- replace()	Returns a string where a specified value is replaced with a specified value
- rfind()	Searches the string for a specified value and returns the last position of where it was found
- rindex()	Searches the string for a specified value and returns the last position of where it was found
- rjust()	Returns a right justified version of the string
- rpartition()	Returns a tuple where the string is parted into three parts
- rsplit()	Splits the string at the specified separator, and returns a list
- rstrip()	Returns a right trim version of the string
- split()	Splits the string at the specified separator, and returns a list
- splitlines()	Splits the string at line breaks and returns a list
- startswith()	Returns true if the string starts with the specified value
- strip()	Returns a trimmed version of the string
- swapcase()	Swaps cases, lower case becomes upper case and vice versa
- title()	Converts the first character of each word to upper case
- translate()	Returns a translated string
- upper()	Converts a string into upper case
- zfill()	Fills the string with a specified number of 0 values at the beginning