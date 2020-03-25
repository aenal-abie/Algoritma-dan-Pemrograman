a =  int(input("Masukkan nilai A: "))
b =  int(input("Masukkan nilai B: "))
c =  int(input("Masukkan nilai C: "))

if(a>b):
    if(a>c):
        terbesar = a
elif(b>c):
    terbesar = b
else:
    terbesar = c

print(terbesar)