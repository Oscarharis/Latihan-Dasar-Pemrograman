#
hargaSupplier = int(input("silahkan Masukan Harga Dari Suplier : "))
persen = int(input("silahkan Masukan persentase : "))
hargaPersen = hargaSupplier *(persen /100)
hargaJual =  hargaSupplier + hargaPersen

print("Harga Dari Supplier :",hargaSupplier)
print("Persentase keuntungan :",persen)
print("Keuntungan Dari Persen : ",hargaPersen)
print("Harga Jual : ",hargaJual)
