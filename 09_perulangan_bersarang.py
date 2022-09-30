# latihan perulangan bersarang/bertingkat (nested)

"""
# 01
nama = ["asep", "ujang", "engkus"]
kata_sifat = ["ganteng", "cerdas", "tampan"]

for i in nama:
    for j in kata_sifat:
        print(i, j)
"""

"""
# 02
for i in range(1, 4):
    print(f"i ke: {i}")
    for j in range(1, 3):
        print(f"    i, j ke {i}, {j}")
"""

# 03
for baris in range(5):
    for kolom in range(3):
        print("o", end=" ")
    else:
        print(" ")