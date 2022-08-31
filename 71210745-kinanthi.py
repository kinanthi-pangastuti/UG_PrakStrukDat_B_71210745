#Kinanthi P (71210745)
#UG1-KALKULATOR

#print("Kalkulator? S = lanjut, Q = keluar")
#pilih = input

print("Silahkan Pilih Menu:")
print("""1. Penjumlahan
2. Pengurangan
3. Perkalian
4. Pembagian
Masukkan "Q" untuk keluar.
=======================""")

while True:
    x = input("Pilihan: ")
    if x in "qQ":
        break

    elif(x == "1"):
        a = int(input("angka pertama: "))
        b = int(input("angka kedua: "))
        hasil = (a + b)
        print("hasil:", hasil)
    elif(x == "2"):
        a = int(input("angka pertama: "))
        b = int(input("angka kedua: "))
        hasil = (a - b)
        print("hasil:", hasil)
    elif (x == "3"):
        a = int(input("angka pertama: "))
        b = int(input("angka kedua: "))
        hasil = (a * b)
        print("hasil:", hasil)
    elif (x == "4"):
        a = int(input("angka pertama: "))
        b = int(input("angka kedua: "))
        hasil = (a / b)
        print("hasil:", float(hasil))


