# Import function dari program Utility didalam folder FUNGSI
import FUNGSI as F


# Mencari tahu siapa nama manager dengan menggunakan search algorithm?
input('1. Mencari tahu siapa nama manager dengan menggunakan search algorithm? (Tekan Enter)')
print(f'\nNama Manager = {F.findManager()}')

# Berapa banyak karyawan yang berjenis kelamin laki-laki dan perempuan?
input('\n2. Berapa banyak karyawan yang berjenis kelamin laki-laki dan perempuan? (Tekan Enter)')
print(f'\nKaryawan berjenis Kelamin: \nLaki-laki = {F.isGender("male")} Orang.\nPerempuan = {F.isGender("female")} Orang.')

# perhitungan bonus berdasarkan gaji + bonus jika work_time karyawan diatas 7 jam dan posisi nya bukanlah manager
input('\n3. Bonus karywan jika work_time diatas 7 jam dan posisi bukan manager? (Tekan Enter)')
print() # print kosong untuk enter
F.Bonus() # Menggunakan fungsi F.Bonus() untuk mengeluarkan hasil di console