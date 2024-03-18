# Daftar varian dan harga beli
varian = ["Bedak", "Lipstik", "Eyeshadow", "Maskara"]
harga_beli = [10000, 15000, 20000, 25000]

# Persentase keuntungan
keuntungan = 10

# Menghitung harga jual
harga_jual = []
for i in range(len(varian)):
  harga_jual.append(harga_beli[i] + (harga_beli[i] * keuntungan / 100))

# Menghitung modal dan laba
modal = sum(harga_beli)
laba = sum(harga_jual) - modal

# Menampilkan tabel hasil
print("-" * 40)
print("| Varian | Harga Beli | Harga Jual |")
print("-" * 40)
for i in range(len(varian)):
  print("| {:^10} | Rp{:^10} | Rp{:^10} |".format(varian[i], harga_beli[i], harga_jual[i]))
print("-" * 40)

# Menampilkan total modal dan laba
print("Total Modal: Rp", modal)
print("Total Laba: Rp", laba)