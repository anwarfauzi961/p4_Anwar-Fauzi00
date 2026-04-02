# Input jumlah hari
hari = int(input("Masukkan jumlah hari: "))

# Konversi
tahun = hari // 365
sisa_hari = hari % 365

bulan = sisa_hari // 30
sisa_hari = sisa_hari % 30

# Output
print("Tahun:", tahun)
print("Bulan:", bulan)
print("Hari:", sisa_hari)