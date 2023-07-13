# buatlah fungsi yang bisa melakukan check terhadap kata yang memiliki sifat
# palindrome, yaitu kata yang apabila dibalik maka tetap menghasilkan kata yang sama
# contoh: kodok -> kodok (true), katak -> katak (true), ab -> ba (false)

## Fungsi Polindrom
def Polindrom(kata):
    pol = True
    length = len(kata)
    for i in range(length):
        if kata[i] != kata[-i-1]:
            pol = False
    if pol:
        return 'true'
    else:
        return 'false'


kata = input('Masukkan kata: ')
print(f'{kata} ({Polindrom(kata)})')