import FungsiTugas7 as ft


first_numbers = [9, 7, 10, 7, 10]


## Dapatkan total nilai baris angka diatas
print(f'Total nilai baris angka = {ft.Total(first_numbers)}')

## Dapatkan nilai yang paling maksimal dan minimal dari baris angka di atas
# Menggunakan function built-in
maksimal = max(first_numbers)
minimal = min(first_numbers)
print(f'Nilai Max dari first_number = {maksimal}')
print(f'Nilai Min dari first_number = {minimal}')

# Menggunakan Fungsi sendiri tapi hanya digunakan untuk number
maximal = ft.MaxforNum(first_numbers)
mini = ft.MinforNum(first_numbers)
print(f'Nilai Max dari first_number = {maximal}')
print(f'Nilai Min dari first_number = {mini}')

## Berapa banyak angka yang bisa dibagi 2

print(f'Banyak angka yang bisa dibagi 2 = {ft.Genap(first_numbers)} Angka')

## buat lah baris ganjil menjadi dikali 2 dan baris genap ditambah 4
ft.JilNap(first_numbers)

## Berapa banyak angka yang sama muncul di dalam baris angka tersebut
ft.jumAngkasama(first_numbers)