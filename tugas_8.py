first_numbers = [9, 7, 10, 7, 10]
second_numbers = [2, 3]
# lakukan perkalian silang antara baris angka pertama dengan baris angka yang kedua
# sehingga menghasilkan
# result = [
# [18, 14, 20, 14, 20],
# [27, 21, 30, 21, 30]
# ]
result1 = []

for num2 in second_numbers:
    row = []
    for num1 in first_numbers:
        row.append(num2 * num1)
    result1.append(row)
print(result1)

# kemudian dari hasil tersebut tambahkanlah masing - masing nilai berdasarkan
# posisi baris nya
# result = [45, 35, 50, 35, 50]
def suml2D(list):
    hasil = []
    for i in range(len(list)):
        for j in range(len(list[i])):
            if i > 0:
                list[0][j]+=list[i][j]
                hasil.append(list[0][j])
    if i > 1:
        return hasil[-(len(list[i])):]
    else:
        return hasil[:]
    
print(suml2D(result1))