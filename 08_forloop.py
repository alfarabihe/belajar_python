# latihan for loop

"""
# list
x = ["fmipa", "fttm", "fitb", "fti"]
for i in x:
    print(i)
"""

"""
# string
for i in "fmipa":
    print(i)
"""

"""
# break statement
# 01
for i in "fmipa":
    print(i)
    if i == "i":
        break

print(" ")

# 02
for i in "fmipa":
    if i == "i":
        break
    print(i)
"""

"""
# continue statement
# 01
for i in "fmipa":
    print(i)
    if i == "i":
        continue

print(" ")

# 02
for i in "fmipa":
    if i == "i":
        continue
    print(i)
"""

"""
# range() statement
# 01
for i in range(11):
    print(i)

print(" ")

# 02
for i in range(6, 11):
    print(i)

print(" ")

# 03
for i in range(0, 11, 2):
    print(i)
"""

"""
# else
# 01
for i in range(6):
    print(i)
else:
    print("selesai")

print(" ")

# 02
for i in range(6):
    if i == 3: break
    print(i)
else:
    print("selesai")
"""

# for kondisi:
#     aksi

angka = [0, 9, 2, 5, 4, 5]
print(angka)

for i in angka:
    print(f"i sekarang: {i}")

print("program selesai")