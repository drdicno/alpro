"""
Nama  : Dicky Novanda Syaifulah
NM    : 20083000068  
Kelas : 2C
Mengecek kelulusan: jika nilai diatas 60 maka lulus, selain itu tidak lulus
"""

jwb="y"
while jwb =="y" or jwb =="Y":
    print("*****************************")
    print("        Cek Kelulusan        ")
    print("*****************************")

    #input nilai n
    n=input("Masukkan Nilai = ")
    #convert nilai n ke int
    m=int(n)
    #cek apakah nilai yang diinputkan 0 - 100
    if m>= 0 and m<= 100:
        #cek nilai, jika m > 60, sts lulus selain itu Ulang
        if m>60: sts="Lulus"
        else: sts="Ulang"
        print (sts)
    else:
        pesan="Inputkan nilai 0 - 100"
        print(pesan)
    
    #inputan untuk break
    jwb = input("Mulai lagi ? y/t =")
    if jwb == "t" or jwb == "T":
        break