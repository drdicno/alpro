# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 11:14:56 2021
@author: x220
Buat program untuk menghitung biaya total pengiriman barang di perusahaan Ekspedisi
Lorena di Malang
1. set variabel kota, jarak, ongkirperkm, totongkir
2. input pilihan kota
3. jika kota Sby, jarak = 169, ongkirperkm=2500, selain itu
jika kota Bdg, jarak = 452, ongkirperkm=4000
4. totongkir = jarak * ongkirperkm
5. tampilkan kota, totongkir
"""

print("=============================================")
print(" TRANSKASI BIAYA EKSPEDISI ")
print("=============================================")
print(" Kode = a. Surabaya")
print(" Kode = b. Bandung")
print("=============================================")

#membuat list pilihan berupa kode
kode = ["a","b"]
kota = ["Surabaya","Bandung"]
jarak = [169,452]
ongkirperkm = [2500,4000]

#memberi inputan tujuan
pilihan = input(">> Masukkan Kode Tujuan = ")
if pilihan == "a" :
    index = kode.index("a")
elif pilihan == "b":
    index = kode.index("b")
else : print("Cek kembali pilihan")

#cetak tampilan layar
print (">> Kode tujuan     = ", kode[index])
print (">> Kota            = ", kota[index])
print (">> Jarak           = ", jarak[index])
print (">> Ongkir per KM   = ", ongkirperkm[index])

#hitung transksi
fixjarak = jarak[index]
fixongkir = ongkirperkm[index]
totongkir = fixjarak * fixongkir

#tampilan ke layar
print ("=============================================")
print ("Total biaya        = Rp. "+ str (totongkir))
