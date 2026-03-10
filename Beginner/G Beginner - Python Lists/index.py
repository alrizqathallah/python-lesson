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
  
# Mengganti nilai item
ballon_dor = ["Messi", "Ronaldo", "Mbappe", "Halland", "Bengs"]
print(ballon_dor)

ballon_dor[4] = "Alrizq"
print(ballon_dor) 

ballon_dor[2:4] = ["Vini", "Pedri"]
print(ballon_dor)

ballon_dor.insert(1, "Bambang")
print(ballon_dor)

# Append Items
formula_one = ["RedBull", "Mercedez", "Ferrari", "Audi", "McLaren", "Aston Martin", "Renault"]
formula_one.append("Alpine")

print(formula_one)

# Insert Items
formula_one.insert(1, "Alpine")

print(formula_one)

# Extend
moto_gp = ["Ducati", "Honda", "Yamaha", "KTM", "Aprilia"]
formula_one.extend(moto_gp)

print(formula_one)

# Concatenation
grand_prix = formula_one + moto_gp

print(grand_prix)