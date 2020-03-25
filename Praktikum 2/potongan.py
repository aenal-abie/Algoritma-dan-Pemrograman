member =  input("Masukkan member? (Ya=Member, Tidak=Bukan Member): ")
belanja = int(input("Masukkan jumlah pembelian: "))

if(member=="Ya"):
    if(belanja>200000):
        potongan =  belanja * 0.1
    elif(belanja>100000):
        potongan =  belanja * 0.05
    else:
        potongan =  belanja * 0.025
else:
    if(belanja>200000):
        potongan= belanja * 0.05
    else:
        potongan = 0

bayar =  belanja -  potongan
print("Total bayar adalah %s" % bayar)
