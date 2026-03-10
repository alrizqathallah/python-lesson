print(10 > 5) # True, karena 10 lebih besar dari 5
print(10 < 5) # False, karena 10 lebih besar dari 5
print(10 == 10) # True, kerana 10 sama besar dengan 10
# integer dan string
print(10 == "10") # False, 10 sama besar dengan 10, namun keduanya berbeda dalam tipe data.

x = 100
y = 1000

if x > y:
  print(f"Nilai {x} lebih besar dari nilai {y}")
else:
  print(f"Nilai {x} tidak lebih besar dari nilai {y}")

print(bool(10)) # Truthy
print(bool("10")) # Truthy
print(bool(0)) # Falsy
print(bool("")) # Falsy
print(bool(" ")) # Truthy
# Falsy
print(bool([]))
print(bool(()))
print(bool({}))
# Falsy
print(bool(False))
print(bool(None))

class myClass():
  def __len__(self):
    return 0

myObj = myClass()
print(bool(myObj))

def myFunction():
  return True

print(myFunction())

if myFunction():
  print("YES!")
else:
  print("NO!")
  
x = 1000
print(isinstance(x, int)) # True
print(isinstance(x, str)) # False