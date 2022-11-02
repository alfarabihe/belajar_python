# Program Tinggi Rata-Rata
# Menghitung rata-rata dari tinggi anak yang diberikan

# KAMUS
# banyak, tinggiT, i : int
# anak, tinggiT, tinggiRat : float

# ALGORITMA
banyak = int(input("Masukkan jumlah anak: "))                 # input

tinggiT = 0                                                   # inisialisasi
for i in range(banyak):                                       # kondisi mengulang
    anak = float(input(f"Masukkan tinggi anak ke-{i + 1}: ")) # aksi
    tinggiT += anak                                           # aksi

tinggiRat = tinggiT / banyak                                  # proses

print(f"Tinggi rata-ratanya adalah", "%.2f" % tinggiRat)      # output