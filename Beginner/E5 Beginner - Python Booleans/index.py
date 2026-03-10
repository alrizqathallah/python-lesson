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