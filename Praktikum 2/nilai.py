nilai = int(input("Masukkan nilai: "))

if(nilai>80):
    grade = "A"
    bobot = "4"
    kategori ="Istimewa"
    keterangan  = "Lulus"
elif(nilai>70):
    grade = "B+"
    bobot = "3.5"
    kategori ="Sangat Baik"
    keterangan  = "Lulus"
elif(nilai>65):
    grade = "B"
    bobot = "3"
    kategori ="Baik"
    keterangan  = "Lulus"
elif(nilai>60):
    grade = "C+"
    bobot = "2.5"
    kategori ="Baik"
    keterangan  = "Lulus"
elif(nilai>49):
    grade = "C"
    bobot = "2"
    kategori ="Baik"
    keterangan  = "Lulus"
elif(nilai>39):
    grade = "D"
    bobot = "1"
    kategori ="Kurang"
    keterangan  = "Tidak Lulus"
else:
    grade = "E"
    bobot = "0"
    kategori ="Kurang"
    keterangan  = "Gagal"

print("Hasil dari nilai %d :\nGrade: %s \nBobot: %s \nKategori: %s \nKeterangan: %s" 
    % (nilai, grade, bobot, kategori, keterangan))
