from collections import Counter

def Total(list) -> int:
    '''Fungsi untuk mendapatkan total angka didalam list'''
    sum = 0
    for i in list: sum+=i
    return sum

def MaxforNum(list) -> int:
    '''Input harus berupa data list dan value nya bertipe data number'''
    for i in range(len(list)):
        if list[i] > list[i+1<len(list)+1]:
            hasil = list[i]
    return hasil

def MinforNum(list) -> int:
    '''Input harus berupa data list dan value nya bertipe data number'''
    for i in range(len(list)):
        if list[i] < list[i+1<len(list)-1]:
            hasil = list[i]
    return hasil


def Genap(list) -> int:
    '''Fungsi untuk mencari berapa banyak angka yang dapat dibagi 2'''
    count = 0
    for i in list:
        if i % 2 == 0: count+=1
    return count

def JilNap(list) -> str:
    '''Fungsi untuk membuat baris angka Ganjil yang dikali 2 dan angka Genap yang di tambah 4'''
    for num in list:
        if num != list[0]:
            print(', ', end='')
        if num % 2 != 0:
            num*=2
            print(f'Ganjil = {num}',end='')
        elif num % 2 == 0:
            num+=4
            print(f'Genap = {num}',end='')
    print()

def jumAngkasama(list) -> str:
    '''Fungsi untuk mencari jumlah angka yang sama disebuah list'''
    # Function Counter disini akan merubah list menjadi dictionary dengan key angka dan value jumlah angka
    angka = Counter(list)
    for num, count in angka.items():
        if count > 1:
            print(f'Angka {num} muncul {count} kali')