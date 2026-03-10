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