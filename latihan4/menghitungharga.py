# Daftar varian dan harga beli
varian = ["Bedak", "Lipstik", "Eyeshadow", "Maskara"]
harga_beli = [10000, 15000, 20000, 25000]

# Persentase keuntungan
keuntungan = 10

# Menghitung harga jual
harga_jual = []
for i in range(len(varian)):
  harga_jual.append(harga_beli[i] + (harga_beli[i] * keuntungan / 100))

# Menampilkan tabel hasil
print("=" * 40)
print("| Varian | Harga Beli (Rp) | Keuntungan (Rp) | Harga Jual (Rp) |")
print("=" * 40)
for i in range(len(varian)):
  print("| {:^10} | {:^10} | {:^10} | {:^10} |".format(varian[i], harga_beli[i], 
                                                                    round(harga_beli[i] * keuntungan / 100), 
                                                                    harga_jual[i]))
print("=" * 40)

# Menampilkan total keuntungan
total_keuntungan = 0
for i in range(len(harga_jual)):
  total_keuntungan += harga_jual[i] - harga_beli[i]

print("Total Keuntungan (Rp):", total_keuntungan)
