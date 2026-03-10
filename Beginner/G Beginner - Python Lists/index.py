# Membuat list
this_list = ["List", "Tuple", "Dictionary", "Set"]
print(this_list)

# List Items
fruits = ["Apple", "Mango", "Cherry", "Apple", "Mango"]
print(fruits)
# Panjang list (length)
print(len(fruits))

# Tipe Data
name = ["Bambang", "Budi", "Zaenal", "Rachmat"]
age = [27, 27, 26, 23]
height = [1.70, 1.73, 1.75, 1.75]

print(name)
print(age)
print(height)

profile = ["Bengs", 28, 1.81]
print(profile)

# list constructor
the_list = list(("Bengs", 28, 1.81))
print(the_list)

# Access List
cars = ["Mercedez", "BMW", "Audi", "Volkswagen", "Porsche"]
print(cars[1]) # BMW
print(cars[4]) # Porsche
print(cars[-1]) # Porsche
print(cars[1:4]) # "BMW", "Audi", "Volkswagen"
print(cars[:4]) # "Mercedez", "BMW", "Audi", "Volkswagen"
print(cars[1:]) # "BMW", "Audi", "Volkswagen", "Porsche"
print(cars[-4:-1]) # "BMW", "Audi", "Volkswagen"

# Check items exist
if "Mercedez" in cars:
  print("Mercedez, exist!")
else:
  print("Mercedez, doesn't exist!")
