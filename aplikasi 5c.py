"""
Nama  : Dicky Novanda Syaifulah
NM    : 20083000068  
Kelas : 2C
Menampilkan nilai huruf dengan Menginputkan sebuah bilangan bulat dari 0-100
"""
#variabel ulang program
jwbulangprog ="y"
while jwbulangprog=="y" or jwbulangprogram=="Y":
    print("************************************")
    print("      Menampilkan Nilai Huruf       ")
    print("************************************")

    #input nilai (u) untuk nilai awal
    u=input("Masukkan bilangan bulat dari 0 - 100 = ")
    #convert nilai u str menjadi n int
    n=int(u)
    #cek apakah bilangan antara 0 - 100
    if n>0 and n<=100:
        if n>80 : sts=("Baik Sekali")
        elif n>=65 : sts=("Baik")
        elif n>=55 : sts=("Cukup")
        elif n>=40 : sts=("Kurang")
        else: sts=("Kurang Sekali")
        print(sts)
        #pesan ulangi program
        jwbulangprog=input("Ulangi program ? y/t = ")
        if jwbulangprog== "t" or jwbulangprog=="T":
            break
    else:
        pesan=("Inputkan bilangan dari 0 hingga 100")
        print(pesan)
        break