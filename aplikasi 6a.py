"""
Nama  : Dicky Novanda Syaifulah
NM    : 20083000068  
Kelas : 2C
Hitung nilai total transaksi pembelian Printer Epson T20
"""

print("************************************")
print("       Nilai Total Transaksi        ")
print("************************************")

jwbulangprog = "y"
while jwbulangprog=="y" or jwbulangprog=="Y":
    hargaprinter=660000
    #input jumlah pembelian
    u=input("Masukkan jumlah pembelian printer = ")
    #convert u str ke n int
    n=int(u)

    #cek apakah angka pembelian lebih dari 0 atau tidak
    if n>0:
        #cek total pembelian dikali harga
        totbiaya=n*hargaprinter
        print("Total biaya pembelian printer = ")
        print(totbiaya)
        #pesan ulangi program
        jwbulangprog=input("Ulangi program ? y/t = ")
        if jwbulangprog== "t" or jwbulangprog=="T":
            break
    else:
        pesan=("Pembelian harus lebih dari 0")
        print(pesan)
        break
