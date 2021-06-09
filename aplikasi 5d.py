"""
Nama  : Dicky Novanda Syaifulah
NM    : 20083000068  
Kelas : 2C
Penilaian mahasiswa akan mendapat nilai huruf X
"""
#variabel ulang program
jwbulangprog ="y"
while jwbulangprog=="y" or jwbulangprogram=="Y":
    print("************************************")
    print("        Penilaian mahasiswa         ")
    print("************************************")

    #input nilai mahasiswa
    u=input("Masukkan nilai = ")
    #convert str u menjadi n int
    n=int(u)

    #cek nilai apakah sudah dari 0 - 100
    if n>0 and n<=100:
        if n>=91: sts="A"
        elif n>=81: sts="B"
        elif n>=71: sts="C"
        else:
            sts="D"
        print(sts)
        #pesan ulangi program
        jwbulangprog=input("Ulangi program ? y/t = ")
        if jwbulangprog== "t" or jwbulangprog=="T":
            break

    else:
        pesan=("Nilai harus 1 - 100")
        print(pesan)
        break