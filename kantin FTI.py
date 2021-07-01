"""
Nama  : Dicky Novanda Syaifulah
NM    : 20083000068  
Kelas : 2C
Hitung nilai total transaksi pembelian di kantin fti
"""
#cek ulang program
jwbulangprog = "y"
while jwbulangprog=="y" or jwbulangprog=="Y":
    print("=====================================")
    print("            Menu Makanan             ")
    print("=====================================")
    print(" a = Nasi goreng         Rp 15.000   ")
    print(" b = Lontong Goreng      Rp 14.900   ")
    print(" c = Bakso Goreng        Rp 12.900   ")
    print(" d = Rujak Goreng        Rp 13.000   ")
    print(" e = Rujak Bakso         Rp 15.000   ")
    print(" f = Rujak Bakso Pecel   Rp 17.000   ")
    print("=====================================")
    print()

    kode1=['a','b','c','d','e','f']
    mmakan=['Nasi goreng','Lontong Goreng','Bakso Goreng','Rujak Goreng','Rujak Bakso','Rujak Bakso Pecel']
    har_mmakan=[15000,14900,12900,13000,15000,17000]


    #memberi inputan pilihan
    pilmenu_mkn = input(">> Masukkan Pilihan Menu  = ")
    #print(pilmenu_mkn)

    #mengecek pilihan apakah sama dengan 
    i = 0
    while i<len(kode1):
        #jika value pada list kode[i] == pilihan
        if kode1[i] == pilmenu_mkn:
            #ambil nama menu
            idx_nmenu = mmakan[i]
            #print(idx_nmenu)
            
            
            #ambil harga menu
            idx_hrgmenu = har_mmakan[i]
            #print(idx_hrgmenu)

        #jika tidak cocok, lanjut ke i berikutnya
        i+=1

    #input banyak porsi
    qty = input(">> Masukkan banyak porsi = ")

    #hitung harga makanan
    hrg_mkn = idx_hrgmenu * int(qty)
    #print(str(hrg_mkn))
    print()
    print(">>> Pilihan menu = " + (pilmenu_mkn)+("."), (idx_nmenu))
    print()
    print()




    print("=========================================")
    print("              Menu Minuman               ")
    print("=========================================")
    print(" a = Teh Dingin/Hangat/Panas Rp 15.000   ")
    print(" b = Kopi Dingin             Rp 14.900   ")
    print(" c = Kopi Teh Panas          Rp 12.900   ")
    print(" d = Coca Cola Dingin        Rp 13.000   ")
    print(" e = Coca Cola Panas         Rp 15.000   ")
    print("=========================================")
    print()

    kode2=['a','b','c','d','e']
    mminum=['Teh Dingin/Hangat/Panas','Kopi Dingin','Kopi Teh Panas','Coca Cola Dingin','Coca Cola Panas']
    har_mminum=[15000,14900,12900,13000,15000]

    pilmenu_minum = input(">> Masukkan Pilihan Minuman  = ")
    #print(pilmenu_minum)

    #mengecek pilihan apakah sama dengan 
    i = 0
    while i<len(kode2):
        #jika value pada list kode[i] == pilihan
        if kode2[i] == pilmenu_minum:
            #ambil nama menu
            idx_nminum = mminum[i]
            #print(idx_nminum)
            
            #ambil harga menu
            idx_hrgmminum = har_mminum[i]
            #print(idx_hrgmminum)

        #jika tidak cocok, lanjut ke i berikutnya
        i+=1

    #input banyak porsi
    qty_nmum = input(">> Masukkan banyak minuman = ")

    #hitung harga minuman
    hrg_nmum = idx_hrgmminum * int(qty_nmum)
    #print(str(hrg_nmum))
    print()
    print(">>> Pilihan minuman = " + (pilmenu_minum)+("."), (idx_nminum))
    print()
    print()

    #hitung total harga makanan dan minuman
    hrg_tot = hrg_mkn + hrg_nmum

    print("=======================================")
    print(">>> Total Harga Makanan = Rp " + str(hrg_mkn))
    print(">>> Total Harga Minuman = Rp " + str(hrg_nmum))
    print(">>> Total Harga         = Rp " + str(hrg_tot))
    print()

    #memberi inputan uang pembayaran
    print("=======================================")
    uangbyr=input(">> Uang bayar            = Rp ")

    #hitung kembalian
    uangkem = int(uangbyr) - hrg_tot

    #tampilan pembayaran dan kembalian
    print(">> Kembali               = Rp " + str(uangkem))
    jwbulangprog = input(">>> Ulang program? y/t = ")
    if jwbulangprog=="t" or jwbulangprog=="T":
        break
