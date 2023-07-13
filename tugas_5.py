# buatlah fungsi untuk menyelesaikan permasalahan di bawah.
# output: JOHN DOE
# output: john doe
# output: John Doe

# Deklarasi fungsi Upper(), Lower(), dan Capital()
Upper = lambda userInput: userInput.upper()
Lower = lambda userInput: userInput.lower()
def Capital(userInput):
    capt = userInput.split()
    for i in capt: print(f'{i.capitalize()}',end=' ')

# Membuat Variable
name = "jOhn DoE"

# Menampilkan hasil diconsole
print(Upper(name))
print(Lower(name))
Capital(name)