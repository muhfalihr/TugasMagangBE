'''
Buatlah kelas turunan `Animal` dengan nama`Chicken` yang memiliki atribut `name`, `legs`,
dan `age` serta buatlah function dengan nama `walk` dan `eat` yang memiliki fungsi untuk
mengirimkan sebuah string ke console
'''
# Mendeklarasikan class Animal
class Animal:
    # Membuat fungsi constructor __init__
    def __init__(self, name:str, legs:int, age:int):
        self.name = name
        self.legs = legs
        self.age = age

# Mendeklarasikan Child Class dari class Animal  
class Chicken(Animal):
    # Membuat fungsi constructor __init__
    def __init__(self, name:str, legs:int, age:int, eat:str, walk:bool) -> str:
        # Method super() digunakan untuk  memberikan access ke method dan property dari parent class
        super().__init__(name, legs, age)
        self.eat = eat
        self.walk = walk

    # Membuat fungsi untuk menampilkan string ke console
    def _eat(self) -> str: print(f'{self.name} eat {self.eat}.')

    # Membuat fungsi untuk menampilkan string ke console
    def _walk(self) -> str: print(f'{self.name} is walk = {self.walk}.')


# Membuat objek ayam dibuat dengan menggunakan class Chicken
# Diberikan atribut 'Ayam Jago' sebagai name, atribut 2 sebagai legs, atribut 7 sebagai age
# atribut 'Polar/Nasi sisa' sebagai eat
ayam = Chicken('Ayam Jago', 2, 7, 'Polar / Nasi sisa', True)
# Mengakses method _eat() dan _walk()
ayam._eat()
ayam._walk()