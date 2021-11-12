print("PILIH ELEKTRONIK APA")
print("Daftar Elektronik Yang tersedia"
      "\n1. Kipas Angin"
      "\n2. TV"
      "\n3. Mesin Cuci"
      "\n4. AC"
      "\n5. Kulkas" 
)
print()
nama = str(input("Masukan Nama Anda\t: "))
pilihan = str(input("Pilih Barang\t\t: "))
if pilihan == "Kipas Angin":
    harga = 1000000
    print("Harga Produk\t\t: Rp.%.2f"%(harga))
    jumlahbeli = int(input("Jumlah pesanan anda\t: "))
    if jumlahbeli >= 1:
        hargakotor = jumlahbeli * harga
        persendisc= 0.05
        diskon = hargakotor * persendisc
        ppnpersen = 0.1
        ppn = (hargakotor - diskon) * ppnpersen
        hargabersih = (hargakotor - diskon) + ppn
    print("Harga Kotor\t\t: Rp.%.2f" %(hargakotor))
    print("Diskon yang didapat\t: Rp.%.2f" %(diskon))
    print("PPN 10%\t\t\t: Rp.",ppn)
    print("Harga Bersih\t\t: Rp.%.2f" %(hargabersih))

elif pilihan == "TV":
    harga = 2000000
    jumlahbeli = int(input("Pesanan anda: "))
    if jumlahbeli >= 1:
        disc = 0.05
elif pilihan == "Mesin Cuci":
    harga = 3000000
    jumlahbeli = int(input("Pesanan anda: "))
    if jumlahbeli >= 1:
        disc = 0.05
elif pilihan == "AC":
    harga = 4000000
    jumlahbeli = int(input("Jumlah Pesanan: "))
    if jumlahbeli >= 3:
        disc = 0.1
    elif jumlahbeli >= 1 and jumlahbeli < 3:
        disc = 0.05
    else:
        disc = 0
elif pilihan == "Kulkas":
    harga = 5000000
    jumlahbeli = int(input("Jumlah Pesanan: "))
    if jumlahbeli >= 5:
        disc = 0.2
    elif jumlahbeli >= 1 and jumlahbeli < 3:
        disc = 0.05
    


