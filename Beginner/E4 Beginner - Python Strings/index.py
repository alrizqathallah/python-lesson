print('Hello')
print("Hello")

print("It's Alright")
print("He is name is 'Cena'")
print('He is name is "Cena"')

name = "John"
print(name)

Teks = """Undang-undang dasar,
Negara Republik Indonesia
tahun 1945.
"""
print(Teks)

welcome = 'Hello World'
print(welcome[1]) # 'e'
print(welcome[0]) # 'H'
print(welcome[5]) # ' '

for x in "Hello World":
  print(x)
  
a = "Hello World"
print(len(a))

Greet = "Hello my name is Bengs, I am 28 years old right now"
print("Bengs" in Greet)

Greet = "Hello my name is Bengs, I am 28 years old right now"
if "Bengs" in Greet:
  print('Kata "Bengs" ada didalam susunan kalimat')
else:
  print('Kata "Bengs" tidak ada didalam susunan kalimat')
  
Greet = "Hello my name is Bengs Ganteng, I am 28 years old right now"
print("Ganteng" not in Greet)

h = "Hello World"
print(h[0:5])
print(h[6:11])
print(h[:5])
print(h[6:])
print(h[-5:-2])

d = "Hello World"
#Uppercase
print(d.upper())
#Lowercase
print(d.lower())
# Replace String element
print(d.replace("e", "o"))

# Split String 
n = "Halo nama saya adalah Bengs. Apa kabar?"
print(n.split("."))


#Remove Whitespace
j = "   Hello World "
print(j) #without removing whitespace
print(j.strip())

u = "Hello"
i = "World"
o = u + " " + i
print(o)
print(u + " " + i)

# F-Strings
usia = 28
pesan = f"Usia saya adalah {usia}"
print(pesan)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

teks = "Ini dikuti dari \"Dia\""
print(teks)