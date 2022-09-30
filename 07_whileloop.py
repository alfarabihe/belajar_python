# latihan while loop

"""
# while loop
angka = 101
print(f"sekarang berada di: {angka}\n"
    "=> seratus satu")

while angka < 110:
    angka += 1
    print(f"sekarang berada di: {angka}")
    if angka < 105:
        if angka == 102:
            print("=> seratus dua")
        elif angka == 103:
            print("=> seratus tiga")
        else:
            print("=> seratus empat")
    elif angka < 108:
        if angka == 105:
            print("=> seratus lima")
        elif angka == 106:
            print("=> seratus enam")
        else:
            print("=> seratus tujuh")
    else:
        if angka == 108:
            print("=> seratus delapan")
        elif angka == 109:
            print("=> seratus sembilan")
        else:
            print("=> seratus sepuluh")
"""

"""
# break statement
angka = 101
print(f"sekarang berada di: {angka}")

while angka < 110:
    angka += 1
    if angka == 105:
        break
    print(f"sekarang berada di: {angka}")
"""

# continue statement
angka = 101
print(f"sekarang berada di: {angka}")

while angka < 110:
    angka += 1
    if angka == 105:
        continue
    print(f"sekarang berada di: {angka}")