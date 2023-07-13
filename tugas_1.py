class Animal:
    # Constructor
    def __init__(self, name:str, legs:int, age:int):
        self.name = name
        self.legs = legs
        self.age = age
    
    # Fungsi return name
    def get_name(self): return self.name
    
    # Fungsi return legs
    def get_legs(self): return self.legs
    
    # Fungsi return age
    def get_age(self): return self.age
    
    # Fungsi return set_legs dari 4 ke 2
    def set_legs(self, newlegs):
        self.legs = newlegs
        return self.legs


# Membuat objek lalu disimpan di variabel dengan nama animal
animal = Animal('Chicken', 4, 10) # Menginputkan atribut ke class Animal
name = animal.get_name() # access attribute name dari objek animal menggunakan methode get_name()
legs = animal.get_legs() # access attribute legs dari objek animal menggunakan methode get_legs()
age = animal.get_age() # access attribute age dari objek animal menggunakan methode get_age()
set_legs = animal.set_legs(2) # method set_legs() digunakan untuk merubah legs

# Value dari attribute objek animal dicetak ke layar / diprint
print(f'{name}\n{legs}\n{age}')
print(f'Animal : {name} Have {set_legs} Legs')

# Output:
#   Chicken
#   4
#   10
#   Animal : Chicken Have 2 Legs