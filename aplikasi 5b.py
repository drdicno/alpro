"""
Nama  : Dicky Novanda Syaifulah
NM    : 20083000068  
Kelas : 2C
Mengecek Tingkat Usia
"""
jwbulangprog = "y"
while jwbulangprog== "y" or jwbulangprog== "Y":
    print("*****************************")
    print("      Cek Tingkat Usia       ")
    print("*****************************")

    #input nilai m/nilai usia
    n=input("Masukkan Usia = ")

    #convert nilai m ke int menjadi n
    m = int (n)
    #mengecek usia apakah 0 - 100
    if m>= 0 and m<=100:
        if m>= 60: sts="Lansia"
        elif m>= 35: sts="Dewasa"
        elif m>= 18: sts="Pemuda"
        elif m>= 15: sts="Remaja"
        else: sts="Anak-anak"
        print(sts)
        #apakah akan mengulang program ?
        jwbulangprog=input("Apakah ingin mengulang program ? y/t = ")
        if jwbulangprog== "t" or jwbulangprog== "T":
            break

    else:
        pesan=("Usia mulai dari 1 - 100")
        print(pesan)
        break
