# latihan operator

"""
operator aritmatika
"""

# variabel
x = 2
y = 3

# penjumlahan
print(f"hasil dari 2 tambah 3 adalah {x + y}")

# pengurangan
print(f"hasil dari 2 kurang 3 adalah {x - y}\n"
    f"hasil dari 3 kurang 2 adalah {y - x}")

# perkalian
print(f"hasil dari 2 kali 3 adalah {x * y}")

# pembagian
print(f"hasil dari 2 bagi 3 adalah {x / y}\n"
    f"hasil dari 3 bagi 2 adalah {y / x}")

# modulus/sisa bagi
print(f"modulus/sisa bagi dari 2 bagi 3 adalah {x % y}\n"
    f"modulus/sisa bagi dari 3 bagi 2 adalah {y % x}")

# perpangkatan
print(f"hasil dari 2 pangkat 3 adalah {x ** y}\n"
    f"hasil dari 3 pangkat 2 adalah {y ** x}")

# pembagian ke bawah
print(f"pembagian ke bawah dari 2 bagi 3 adalah {x // y}\n"
    f"pembagian ke bawah dari 3 bagi 2 adalah {y // x}")

"""
operator assignment/penugasan
"""

# 01
a = 1
print(a)

# 02
a = 2
a += 2
print(a)

# 03
a = 3
a -= 2
print(a)

# 04
a = 4
a *= 2
print(a)

# 05
a = 5
a /= 2
print(a)

# 06
a = 6
a %= 2
print(a)

# 07
a = 7
a //= 2
print(a)

# 08
a = 8
a **= 2
print(a)

"""
operator relasional/komparasi/perbandingan
"""

# variabel
x = 5
y = 10

# lebih dari
print(f"5 > 10 = {x > y}")

# kurang dari
print(f"5 < 10 = {x < y}")

# sama dengan
print(f"5 == 10 = {x == y}")

# lebih dari atau sama dengan
print(f"5 >= 10 = {x >= y}")

# kurang dari atau sama dengan
print(f"5 <= 10 = {x <= y}")

# tidak sama dengan
print(f"5 != 10 = {x != y}")

"""
operator logika
"""

# dan
print(f"{5 + 5 == 10 and True}\n"
    f"{5 + 5 == 10 and False}")

# atau
print(f"{5 + 5 == 10 or True}\n"
    f"{5 + 5 == 10 or False}\n"
    f"{5 + 5 == 11 or False}")

# negasi
print(f"{not 5 + 5 == 10}\n"
    f"{not 5 + 5 == 11}")

"""
operator keanggotaan/membership
"""

# variabel
x = ["fmipa", "fitb", "fttm", "ftmd"]

# in
print(f"apakah fmipa ada di variabel x? {'fmipa' in x}\n"
    f"apakah fsrd ada di variabel x? {'fsrd' in x}")

# not in
print(f"apakah fmipa tidak ada di variabel x? {'fmipa' not in x}\n"
    f"apakah fsrd tidak ada di variabel x? {'fsrd' not in x}")

"""
operator identitas
"""

# is, is not, dan mengecek id

# 01
string_a1 = "a"
string_a2 = "a"
string_b1 = "b"
string_b2 = "b"
print(f"{string_a1 is string_a2} {string_a1 is not string_b1}\n"
    f"{id(string_a1)} {id(string_a2)}\n"
    f"{id(string_b1)} {id(string_b2)}")

# 02
int_a1 = 1
int_a2 = 1
int_b1 = 2
int_b2 = 2
print(f"{int_a1 is int_a2} {int_a1 is not int_b1}\n"
    f"{id(int_a1)} {id(int_a2)}\n"
    f"{id(int_b1)} {id(int_b2)}")

# 03
float_a1 = 0.1
float_a2 = 0.1
float_b1 = 0.2
float_b2 = 0.2
print(f"{float_a1 is float_a2} {float_a1 is not float_b1}\n"
    f"{id(float_a1)} {id(float_a2)}\n"
    f"{id(float_b1)} {id(float_b2)}")

# 04
bool_a1 = True
bool_a2 = True
bool_b1= False
bool_b2 = False
print(f"{bool_a1 is bool_a2} {bool_a1 is not bool_b1}\n"
    f"{id(bool_a1)} {id(bool_a2)}\n"
    f"{id(bool_b1)} {id(bool_b2)}")

# 05
list_a1 = [1, 2, 3]
list_a2 = [1, 2, 3]
list_b1 = [4, 5, 6]
list_b2 = [4, 5, 6]
print(f"{list_a1 is list_a2} {list_a1 is not list_b1}\n"
    f"{id(list_a1)} {id(list_a2)}\n"
    f"{id(list_b1)} {id(list_b2)}")