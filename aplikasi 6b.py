"""
Nama  : Dicky Novanda Syaifulah
NM    : 20083000068  
Kelas : 2C
Hitung nilai total transaksi pembelian Printer Epson T20
"""

jwbulang="y"
while jwbulang=="y" or jwbulang=="Y":

    print("************************************")
    print("       Nilai Total Transaksi        ")
    print("************************************")

    harSat = 660000
    persenDiskon = 0.15
    minDiskon = 1500000

    #input kuantitas printer
    u=input("Masukkan jumlah printer yang dibeli = ")
    #convert str u ke int n
    n = int (u)

    #cek harga awal & cek kuantitas
    if n>0 :
        totawl=n*harSat
        print("Harga awal = Rp " + str (totawl))
    else:
        pesan=("Pesanan minimal adalah 1")
        print(pesan)
        break

    #cek nilai diskon
    if totawl>minDiskon:
        ndiskon=totawl*persenDiskon
        print("Diskon = Rp " + str(ndiskon))
    else:
        ndiskon=0

    #cek harga total
    hargatot=totawl-ndiskon
    print("Harga total = Rp " + str(hargatot))

    #inputan ulang program
    jwbulang=input("Apakah ingin mengulang program ? y/t = ")
    if jwbulang=="t" or jwbulang=="T":
        break
