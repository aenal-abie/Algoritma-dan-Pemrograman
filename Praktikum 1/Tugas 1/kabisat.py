#Jika angka tahun itu habis dibagi 400, maka tahun itu sudah pasti tahun kabisat.
#Jika angka tahun itu tidak habis dibagi 400 tetapi habis dibagi 100, maka tahun itu sudah pasti 
#      bukan merupakan tahun kabisat.
#Jika angka tahun itu tidak habis dibagi 400, tidak habis dibagi 100 akan tetapi habis dibagi 4, 
#      maka tahun itu merupakan tahun kabisat.
#Jika angka tahun tidak habis dibagi 400, tidak habis dibagi 100, dan tidak habis dibagi 4, 
#      maka tahun tersebut bukan merupakan tahun kabisat.

tahun = int(input("Masukkan Tahun: "))
kabisat = (tahun % 400 == 0) or (tahun % 400 != 0 and tahun % 100 !=0 and tahun % 4 ==0 )
keterangan = "Tahun Kabisat" if(kabisat) else "Bukan tahun kabisat"
print(keterangan)