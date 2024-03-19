# Daftar varian kosmetik
varian = ["Lipstik", "Bedak", "Eyeshadow", "Maskara"]

# Daftar harga dari supplier
harga_supplier = [100000, 50000, 75000, 60000]

# Persentase keuntungan
persentase_keuntungan = 10

# Hitung harga jual
harga_jual = []
for i in range(len(varian)):
  harga_jual.append(harga_supplier[i] + (harga_supplier[i] * persentase_keuntungan / 100))

# Tampilkan tabel daftar kosmetik
print("=" * 30)
print("Daftar Kosmetik")
print("=" * 30)
print("| Varian | Harga Supplier | Harga Jual |")
print("|---|---|---|")
for i in range(len(varian)):
  print("| {} | Rp {} | Rp {} |".format(varian[i], harga_supplier[i], harga_jual[i]))
print("=" * 30)

# Tampilkan total keuntungan
total_keuntungan = 0
for i in range(len(varian)):
  total_keuntungan += harga_jual[i] - harga_supplier[i]
print("Total Keuntungan: Rp {}".format(total_keuntungan))
