"""
Nama  : Dicky Novanda Syaifulah
NM    : 20083000068  
Kelas : 2C
menampilkan beberapa merek Oli motor & menghitung total biaya
"""

print("=============================================")
print(" Kode & Daftar Merek Oli")
print("=============================================")
print(" a. Duration SW20 1L      @ Rp53.000")
print(" b. Castrol Magnatec 1L   @ Rp50.000")
print(" c. Federal Supreme XX 1L @ Rp54.000")
print(" d. Yamalube 1L           @ Rp45.000")
print(" e. Shell 1L              @ Rp46.000")
print("=============================================")

#membuat list yang dibituhkan
kode = ["a","b","c","d","e"]
harga = [53000,50000,54000,45000,46000]

#menginput kode yang akan dibeli
pil=input(">> Masukkan kode pilihan yang akan dibeli = ")
indexpil = kode.index(pil)

indexhar = indexpil
#menginput jumlah yang akan dibeli
jumlah=int (input(">> Masukkan jumlah yang ingin dibeli = "))

#cetak tampilan layar
print("=============================================")
print("Kode produk      = ", kode[indexpil])
print("Jumlah produk    = ", jumlah)

#hitung transksi
harga = harga[indexhar]*jumlah
print("Harga            = Rp. " + str (harga))

#mengecek potongan harga
if harga >= 200000 :
    hardiskon = 0.05 * harga
    print("=============================================")
    print("Diskon           = Rp. " + str (hardiskon))
else : hardiskon = 0

#menghitung harga setelah diskon
hargaseb_ppn = harga - hardiskon
print("=============================================")
#print("Total harga      = Rp. " + str(hargaseb_ppn))

#menghitung ppn 1%
harga_ppn = hargaseb_ppn * 0.01
fixharga = hargaseb_ppn + harga_ppn
print("Total harga (ppn 1%)     = Rp. " + str(fixharga))
