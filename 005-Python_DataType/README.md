# Python Data Type

## Tipe Data Built-in (bawaan)

Tipe data merupakan konsep penting dalam sebuah bahasa pemrograman.

Varibel dapat menyimpan bermacam tipe data, dan tipe data dapat melakukan serangkaian hal yang berbeda.

Beberapa contoh tipe data bawaan di Python:

- Tipe Teks: `str` (STRING)
- Tipe Numerik (bilangan): `int`, `float`, `complex` (INTEGER, FLOAT, COMPLEX)
- Tipe Sekuensial: `list`, `tuple`, `range`
- Tipe Mapping: `dict`
- Tipe Set: `set`, `frozenset`
- Tipe Boolean: `bool`
- Tipe Binary: `byte`, `bytearray`, `memoryview`
- Tipe None: `NoneType`

contoh:

```Python
x = "Hello World"

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = 20

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = 20.5

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = 1j

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = ["apple", "banana", "cherry"]

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = ("apple", "banana", "cherry")

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = range(10)

#display x:
print(x)

#convert to list to display the content of x:
print(list(x))

x = {"name" : "John", "age" : 36}

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = {"apple", "banana", "cherry"}

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = frozenset({"apple", "banana", "cherry"})

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = True

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = b"Hello"

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = bytearray(5)

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = memoryview(bytes(5))

#display x:
print(x)

#display the data type of x:
print(type(x))

x = None

#display x:
print(x)

#display the data type of x:
print(type(x)) 
```