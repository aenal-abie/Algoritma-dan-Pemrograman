def hitung_grade(nilai_angka):
    if(nilai_angka>80):
        grade = "A"
    elif(nilai_angka>70):
        grade = "B+"
    elif(nilai_angka>65):
        grade = "B"
    elif(nilai_angka>60):
        grade = "C+"
    elif(nilai_angka>50):
        grade = "C"
    elif(nilai_angka>40):
        grade = "D"
    else:
        grade = "E"
    return grade


nilai =  int(input("Masukkan sebuah nilai 0-100: "))
grade = hitung_grade(nilai)
print("Grade nilai anda adalah", grade)