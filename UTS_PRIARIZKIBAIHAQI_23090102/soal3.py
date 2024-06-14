jumlah_barang = int(input("masukan jumlah barang :"))
harga_barang_1= int(input("masukan harga barang pertama :"))
harga_barang_2 = int(input("masukan harga barang ke dua :"))

total_barang_1 = harga_barang_1 * jumlah_barang
total_barang_2 = harga_barang_2 * jumlah_barang

total = total_barang_1 + total_barang_2

print(f"total belanjaan : {total}")