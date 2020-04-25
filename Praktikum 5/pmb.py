def dpp_rangking(rangking):
    if(rangking==1):
        potongan_dpp = 1
    elif(rangking==2):
        potongan_dpp = 0.75
    elif(rangking==3):
        potongan_dpp = 0.5
    dpp = 10000000
    dpp = dpp - (dpp*potongan_dpp)
    return dpp

def cek_dpp_nilai(nilai):
    if(nilai>80):
        dpp = 10000000
    elif(nilai>70):
        dpp = 12000000
    else:
        dpp = 15000000
    return dpp 

def cek_kategori_nilai(nilai):
    if(nilai>80):
        kategori =  1
    elif(nilai>70):
        kategori =  2
    else:
        kategori =  3
    return kategori

def cek_biaya_lain(nilai):
    if(nilai>80):
        lain_lain = 0
    elif(nilai>70):
        lain_lain = 1500000
    else:
        lain_lain = 2000000
    return lain_lain


spp =  2000000
input("Masukkan nama pendaftar: ")
input("Masukkan no pendftaran: ")
status_rangking = int(input("Apakah pendaftar memiliki rangking (1: Ya, 0:Tidak): "))
if(status_rangking):
    rangking =  int(input("Masukkan rangking kelas (1-3): "))
    dpp =  dpp_rangking(rangking)
    kategori = 1
    lain_lain = 0
else:
    nilai = int(input("Masukkan nilai tes: "))
    dpp = cek_dpp_nilai(nilai)
    kategori =  cek_kategori_nilai(nilai)
    lain_lain = cek_biaya_lain(nilai)

total =  dpp + spp + lain_lain

print("Kategori: ", kategori )
print("SPP: ", spp)
print("DPP: ", dpp)
print("Total: ", total)