spp =  2000000
isi = True
while(isi):
    input("Masukkan nama pendaftar: ")
    input("Masukkan no pendftaran: ")
    status_rangking = int(input("Apakah pendaftar memiliki rangking (1: Ya, 0:Tidak): "))
    if(status_rangking):
        rangking =  int(input("Masukkan rangking kelas (1-3): "))
        if(rangking==1):
            potongan_dpp = 1
        elif(rangking==2):
            potongan_dpp = 0.75
        elif(rangking==3):
            potongan_dpp = 0.5
        kategori = 1
        dpp = 10000000
        dpp = dpp - (dpp*potongan_dpp)
        lain_lain = 0
    else:
        nilai = int(input("Masukkan nilai tes: "))
        if(nilai>80):
            kategori =  1
            dpp = 10000000
            lain_lain = 0
        elif(nilai>70):
            kategori =  2
            dpp = 12000000
            lain_lain = 1500000
        else:
            kategori =  3
            dpp = 15000000
            lain_lain = 2000000

    total =  dpp + spp + lain_lain

    print("Kategori: ", kategori )
    print("SPP: ", spp)
    print("DPP: ", dpp)
    print("Total: ", total)
    isi = int(input("Apakah anda akan menginput pendaftar baru (1:Ya, 0:Tidak): "))