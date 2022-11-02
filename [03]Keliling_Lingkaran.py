# Program Keliling Lingkaran
# Menghitung keliling lingkaran dari jari-jari yang diberikan

# KAMUS
# jari, pi, keliling : float

# ALGORITMA
jari = float(input("Masukkan jari-jari lingkaran: ")) # input
pi = 3.14159265                                       # inisialisasi

keliling = 2 * pi * jari                              # proses

print(f"Kelilingnya adalah", "%.2f" % keliling)       # output