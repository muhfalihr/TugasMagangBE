# Memisahkan data di file terpisah berformat json

import json

# Membuka file menggunankan fungsi open() dengan mode default 'r' (read)
# Meng assignment file ke dalam variabel file.
with open('employees.json') as file:
    # fungsi dibawah ini dugunakan untuk membaca isi file JSON
    # Mengubahnya menjadi dictionary hasilnya disalin ke variabel data
    data = json.load(file).copy()

## FUNGSI
# berapa banyak karyawan yang berjenis kelamin laki-laki dan perempuan?
def isGender(gender:str) -> int:
    '''Menentukan Berapa banyak gender Male(Laki-laki) atau Female(Perempuan)'''
    count = 0
    for employee in data:
        if employee['gender'] == gender: count+=1
        elif employee['gender'] == gender: count+=1
    return count

# Mencari tahu siapa nama manager dengan menggunakan search algorithm?
def findManager() -> str:
    '''Mencari posisi manager dan mereturn nama'''
    for employee in data:
        if employee['position'] == 'manager': return employee['name']

# buatlah perhitungan bonus berdasarkan gaji + bonus jika work_time
# karyawan diatas 7 jam dan posisi nya bukanlah manager
def Bonus() -> str:
    '''Menghitung bonus karyawan dari perhitungan salary dan work_time, fungsi ini akan mencetak hasil ke console'''
    for employee in data:
        if employee['work_time'] > 7 and employee['position'] != 'manager':
            bonus = employee['salary'] * employee['work_time'] / 100
            total = round(bonus) + employee['salary']
            name = employee['name']
            print(f'Employees: {name} have total salary: Rp. {total:,}')

