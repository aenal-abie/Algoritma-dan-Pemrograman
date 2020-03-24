tahun = int(input("Masukkan tahun masehi: "))
if(tahun % 400==0):
    ket = "Tahun kabisat"
elif(tahun % 100 == 0):
    ket = "Bukan Tahun kabisat"
elif(tahun % 4 == 0):
    ket = "Tahun kabisat"
else:
    ket = "Bukan Tahun kabisat"
print(ket)