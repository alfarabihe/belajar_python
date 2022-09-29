# latihan kalkulator sederhana (2 angka)

# pembuka
print(f"{'='*46}\n"
    "SELAMAT DATANG DI PROGRAM KALKULATOR SEDERHANA\n"
    F"{'='*46}\n"
    "Silakan gunakan operator di bawah ini:\n"
    "1. penjumlahan        : +\n"
    "2. pengurangan        : -\n"
    "3. perkalian          : * atau x\n"
    "4. pembagian          : /\n"
    "5. pembagian ke bawah : //\n"
    "6. sisa bagi          : %\n"
    "7. perpangkatan       : **")

# variabel
x = int(input("masukkan angka pertama : "))
y = str(input("masukkan operator      : "))
z = int(input("masukkan angka kedua   : "))

# algoritma
if y == "+":               # 1
    print(f"{x} + {z} = {x + z}")
elif y == "-":             # 2
    print(f"{x} - {z} = {x - z}")
elif y == "*" or y == "x": # 3
    print(f"{x} * {z} = {x * z}")
elif y == "/":             # 4
    print(f"{x} / {z} = {x / z}")
elif y == "//":            # 5
    print(f"{x} // {z} = {x // z}")
elif y == "%":             # 6
    print(f"{x} % {z} = {x % z}")
elif y == "**":             # 7
    print(f"{x} ** {z} = {x ** z}")
else:
    print("masukkan operator sesuai petunjuk!")