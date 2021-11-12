print("-------------------ELEKTRONIK--------------------")
print("Daftar Elektronik Yang tersedia"
      "\n1. Kipas Angin"
      "\n2. TV"
      "\n3. Mesin Cuci"
      "\n4. AC"
      "\n5. Kulkas" 
)
print("-------------------------------------------------")
nama = str(input("Masukan Nama Anda\t: "))
pilihan = str(input("Pilihan Produk\t\t: "))
if pilihan == "Kipas Angin":
    harga = 1000000
    print("Harga Produk\t\t: Rp.%.2f"%(harga))
    jumlahbeli = int(input("Jumlah Pesanan Anda\t: "))
    if jumlahbeli >= 1:
        hargakotor = jumlahbeli * harga
        disc = "5%"
        persendisc= 0.05
        diskon = hargakotor * persendisc
        ppnpersen = 0.1
        ppn = (hargakotor - diskon) * ppnpersen
        hargabersih = (hargakotor - diskon) + ppn
    print("Harga Kotor\t\t: Rp.%.2f"%(hargakotor))
    print("Diskon\t\t\t: %s"%(disc))
    print("Potongan Harga\t\t: Rp.%.2f" %(diskon))
    print("PPN 10%\t\t\t: Rp.",ppn)
    print("Harga Bersih\t\t: Rp.%.2f" %(hargabersih))

elif pilihan == "TV":
    harga = 2000000
    print("Harga Produk\t\t: Rp.%.2f"%(harga))
    jumlahbeli = int(input("Jumlah Pesanan Anda\t: "))
    if jumlahbeli >= 1:
        hargakotor = jumlahbeli * harga
        disc = "5%"
        persendisc = 0.05
        diskon = hargakotor * persendisc
        ppnpersen = 0.1
        ppn = (hargakotor - diskon) * ppnpersen
        hargabersih = (hargakotor - diskon) + ppn
    print("Harga Kotor\t\t: Rp.%.2f"%(hargakotor))
    print("Diskon\t\t\t: %s"%(disc))
    print("Potongan Harga\t\t: Rp.%.2f" %(diskon))
    print("PPN 10%\t\t\t: Rp.",ppn)
    print("Harga Bersih\t\t: Rp.%.2f" %(hargabersih))
elif pilihan == "Mesin Cuci":
    harga = 3000000
    print("Harga Produk\t\t: Rp.%.2f"%(harga))
    jumlahbeli = int(input("Jumlah Pesanan Anda\t: "))
    if jumlahbeli >= 1:
       hargakotor = jumlahbeli * harga
       disc = "5%"
       persendisc = 0.05
       diskon = hargakotor * persendisc
       ppnpersen = 0.1
       ppn = (harga - diskon) * ppnpersen
       hargabersih = (hargakotor - diskon) + ppn
    print("Harga Kotor\t\t: Rp.%.2f"%(hargakotor))
    print("Diskon\t\t\t: %s"%(disc))
    print("Potongan Harga\t\t: Rp.%.2f" %(diskon))
    print("PPN 10%\t\t\t: Rp.",ppn)
    print("Harga Bersih\t\t: Rp.%.2f" %(hargabersih))
elif pilihan == "AC":
    harga = 4000000
    print("Harga Produk\t\t: Rp.%.2f"%(harga))
    jumlahbeli = int(input("Jumlah Pesanan Anda\t: "))
    if jumlahbeli >= 5:
        hargakotor = jumlahbeli * harga
        disc = "10%"
        persendisc = 0.1
        diskon = hargakotor * persendisc
        ppnpersen = 0.1
        ppn = (harga - diskon) * ppnpersen
        hargabersih = (hargakotor - diskon) + ppn
   
    elif jumlahbeli >= 1 and jumlahbeli < 5:
        hargakotor = jumlahbeli * harga
        disc = "5%"
        persendisc = 0.05
        diskon = hargakotor * persendisc
        ppnpersen = 0.1
        ppn = (harga - diskon) * ppnpersen
        hargabersih = (hargakotor - diskon) + ppn
    else:
        disc = ""
    print("Harga Kotor\t\t: Rp.%.2f"%(hargakotor))
    print("Diskon\t\t\t: %s"%(disc))
    print("Potongan Harga\t\t: Rp.%.2f" %(diskon))
    print("PPN 10%\t\t\t: Rp.",ppn)
    print("Harga Bersih\t\t: Rp.%.2f" %(hargabersih))
elif pilihan == "Kulkas":
    harga = 5000000
    print("Harga Produk\t\t: Rp.%.2f"%(harga))
    jumlahbeli = int(input("Jumlah Pesanan Anda\t: "))
    if jumlahbeli >= 5:
        hargakotor = jumlahbeli * harga
        disc = "20%"
        persendisc = 0.2
        diskon = hargakotor * persendisc
        ppnpersen = 0.1
        ppn = (harga - diskon) * ppnpersen
        hargabersih = (hargakotor - diskon) + ppn
    elif jumlahbeli >= 1 and jumlahbeli < 5:
        hargakotor = jumlahbeli * harga
        disc = "5%"
        persendisc = 0.05
        diskon = hargakotor * persendisc
        ppnpersen = 0.1
        ppn = (harga - diskon) * ppnpersen
        hargabersih = (hargakotor - diskon) + ppn
    print("Harga Kotor\t\t: Rp.%.2f"%(hargakotor))
    print("Diskon\t\t\t: %s"%(disc))
    print("Potongan Harga\t\t: Rp.%.2f" %(diskon))
    print("PPN 10%\t\t\t: Rp.",ppn)
    print("Harga Bersih\t\t: Rp.%.2f" %(hargabersih))




