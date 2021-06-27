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
print(" Kode = A. Surabaya")
print(" Kode = B. Bandung")
print("=============================================")

#memberi kode pilihan
kode = ['a','b']
kota = ['surabaya','bandung']
jarak = [169,452]
ongkirperkm = [2500,4000]

#memberi inputan user kepada user. mencetak nomor indeks dari item yang terpilih
pilihan = str.lower(input(">> Masukkan Pilihan = "))
#pilihan = input(">> Masukkan Pilihan = ")
print(pilihan)

i = 0;
while i<len(kode):
    #cek apakah kode pada index yg AKTIF == pilihan
    if kode[i] == pilihan:
        #print("index = " + str(i))
        idx = i
    i+=1

print(">> Pilihan Tujuan    = " + kota[idx])
print(">> Jarak             = " + str(jarak[idx]) + " km")
print(">> Ongkir per Km     = Rp. " + str(ongkirperkm[idx]))

ongkir = jarak[idx] * ongkirperkm[idx]
#tampilkan biaya kirim
print(">> Total Biaya       = Rp. " + str(ongkir))
print(" ")
print("==============================================")
