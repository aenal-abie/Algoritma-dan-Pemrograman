tahun = int(input("Masukkan tahun: "))

if(tahun % 400 == 0):
    ket = "Tahun Kabisat"
elif(tahun % 100 == 0):
    ket = "Bukan tahun Kabisat"
elif(tahun % 4 ==0):
    ket = "Tahun Kabisat"
else:
    ket = "Bukan tahun kabisat"

print(ket)