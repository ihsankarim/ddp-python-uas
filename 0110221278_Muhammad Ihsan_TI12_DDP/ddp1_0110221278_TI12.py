#SLIP GAJI AHMAD
nama1 = "Ahmad"
agama1 = "Islam"
gajipokok1  = 4000000
gajipokok2 = 6000000
jumlahanakahmad = 2
jumlahanakalex = 5

#List dan Tuple
listzakat = [0,0.025]
tuplezakat = (0,0.025)
# Tunjangan Jabatan
tunjabatan1 = 0.2 * gajipokok1

# If Multi kondisi
anak = 2
if(anak >0 and anak <=2 ):
    tunjangankeluarga = 0.1 * gajipokok1
elif(anak >2):
    tunjangankeluarga = 0.2 * gajipokok2
else:
    tunjangankeluarga = 0

# Gaji Pokok + Tunjangan Jabatan + Tunjangan Keluarga
gajikotor1 = gajipokok1 + tunjabatan1 + tunjangankeluarga

# Zakat Profesi
zakat1 = (0,0.025)[agama1 == gajikotor1 < 6000000 ] * gajikotor1

# Gaji Bersih 
gajibersih1 = gajikotor1 - zakat1

# CETAK SLIP GAJI AHMAD
print("                SLIP GAJI ALEX              ",
    "\n--------------------------------------------"
)
print ("Nama Pegawai\t\t:",nama1,
        "\nAgama\t\t\t:",agama1,
        "\nJumlah Anak\t\t:",jumlahanakahmad,
        "\nGaji Pokok\t\t:",gajipokok1,
        "\nTunjangan Jabatan\t:",tunjabatan1,
        "\nTunjangan Keluarga\t:",tunjangankeluarga,
        "\nGaji Kotor\t\t:",gajikotor1,
        "\nZakat Profesi\t\t:",zakat1,
        "\nGaji Bersih\t\t:",gajibersih1
)
print("")

# SLIP GAJI ALEX
nama2 = "Alex"
agama2 = "Kristen Protestan"
gajipokok1 = 4000000
gajipokok2 = 6000000
tunjabatan2 = 0.2 * gajipokok2
jumlahanakalex = 5

#Tunjangan Keluarga
# If Multi Kondisi
anak = 5
if(anak >0 and anak <=2 ):
    tunjangankeluarga = 0.1 * gajipokok1
elif(anak >2):
    tunjangankeluarga = 0.2 * gajipokok2
else:
    tunjangankeluarga = 0

# Gaji Kotor Alex
gajikotor2 = gajipokok2 + tunjabatan2 + tunjangankeluarga
# Zakat Profesi Alex
zakat = (0,0.025) [agama2 ==  gajikotor2 >= 6000000] * gajikotor2
# Gaji Bersih Alex
gajibersih2 = gajikotor2 - zakat

print("                SLIP GAJI ALEX              ",
    "\n--------------------------------------------"
)
print ("Nama Pegawai\t\t:",nama2,
        "\nAgama\t\t\t:",agama2,
        "\nJumlah Anak\t\t:",jumlahanakalex,
        "\nGaji Pokok\t\t: Rp.",gajipokok2,
        "\nTunjangan Jabatan\t: Rp.",tunjabatan2,
        "\nTunjangan Keluarga\t: Rp.",tunjangankeluarga,
        "\nGaji Kotor\t\t: Rp.",gajikotor2,
        "\nZakat Profesi\t\t: Rp.",zakat,
        "\nGaji Bersih\t\t: Rp.",gajibersih2
)






























