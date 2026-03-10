# Contoh operator unutk menampilkan operasi pada sebuah value dan variabel
print(2 + 2) # 4

x = 5
y = 10

print(x + y) # 15

z = x + y

print(z)

# Operator Matematika
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

# Walrus operator
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
  print(f"List has {count} elements")
  
# Operator perbandingan
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

# and
x = 5

print(x > 0 and x < 10)

# or
x = 5

print(x < 5 or x > 10)

# not
x = 5

print(not(x > 3 and x < 10))

# Operator identitas
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
z = x

print(x is not y) # True, benar x dan y tidak sama
print(x is not z) # False, x dan z itu sama

fruits = ["Orange", "Mango", "Apple"]
print("Mango" in fruits) # True

cars = ["Mercedez-Benz", "BMW", "Audi"]
print("BMW" not in cars) # False
print("Volkswagen" not in cars) # True

String = "Hello Python".lower()
print("py" in String) # True
print("z" in String) # False

List = ["Ronaldo", "Messi", "Neymar"]
Tuple = ("Rossi", "Stoner", "Pedrossa")

print("Ronaldo" in List) # True
print("Kaka" in List) # False

print("Stoner" in Tuple) # True
print("Marquez" in Tuple) # False

Dictionary = {"Nama": "Ujang Rambo", "usia": 20, "Alamat": "Bandung"}
print("Nama" in Dictionary)
print("Ujang Rambo" in Dictionary)

username = ['admin', 'root', 'tester', 'superuser']
new_username = 'citer'

if new_username in username:
  print(f'Sorry, your username: "{new_username}" cannot be used!')
else:
  print(f'your username: "{new_username}" can be used!')