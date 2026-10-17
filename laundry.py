import os

start = 1
while start == 1:
    print("=== Laundry ===")
    print("Pilih menu : ")
    print("1. Transaksi Laundry")
    print("2. Keluar")
    userpilih = input("Pilih menu (1/2) : ")

    if userpilih == "2" :
        start = 2
        break

    if userpilih == "1" :

        print("==== Input Data Pelanggan ====")
        nama = input("Nama Pelanggan       : ")
        mem = input("Apakah member (Y//N) : ").lower()
        beratcucian = int(input("Berat Cucian (Kg)    : "))


        print("")
        print("==== Jenis Cucian ====")
        print("1. Pakaian biasa (baju/celana)")
        print("2. Sprei/bedcover")

        jenis = input("Pilih Layanan (1/2) : ")
        if jenis == "1" :
            jenis_cucian = "pakaian biasa"
            perkg_reg = 7000
            perkg_express = 10000

        elif jenis == "2" :
            jenis_cucian= "sprei,bedcover"
            perkg_reg = 10000
            perkg_express = 14000

        
        print("")
        print("==== Pilih Layanan ====")
        print("1. Reguler (3 Hari) =", perkg_reg)
        print("2. Express (7 Jam)  =", perkg_express)
        layanan = input("Pilih Layanan (1/2) : ")
        print("")

        if layanan == "1" :
            jns = "reguler"
            harga_jenis = perkg_reg

        elif layanan == "2" :
            jns = "express"
            harga_jenis = perkg_express


        def cetak_struk() :
            print("===== struk laundry ====")
            print("Nama Pelanggan  :",nama)
            print("Berat Cucian    :",beratcucian, "Kg")
            print("Jenis Cucian    :",jenis_cucian)
            print("jenis Layanan   :",jns)
            print("Harga perkg     : Rp",harga_jenis)
            
            total_awal = beratcucian * harga_jenis

            print("Total awal      : Rp", total_awal)

            if mem == "y" and beratcucian >= 10 :
                disc = 0.1
                harga_setelah_diskon = total_awal - (total_awal * disc)

            else :
                disc = 0
                harga_setelah_diskon = total_awal - (total_awal * disc)

            print("Diskon          : Rp", total_awal*disc)
            print("Total bayar     : Rp", harga_setelah_diskon)

            print("==================================")



            
        cetak_struk()
        
        z = input("Tekan Enter untuk kembali")


    else :
        print("pilihan tidak ditemukan")


