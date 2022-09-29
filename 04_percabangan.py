# latihan percabangan

# mengecek bilangan positif, nol, atau negatif
x = int(input("masukkan bilangan: "))

""""
# if, elif, dan else
if x > 0:
    print(f"bilangan {x} merupakan bilangan positif")
elif x == 0:
    print(f"bilangan {x} merupakan bilangan nol")
else:
    print(f"bilangan {x} merupakan bilangan negatif")
"""

# if di dalam if
if x >= 0:
    if x > 0:
        print(f"bilangan {x} merupakan bilangan positif")
    else:
        print(f"bilangan {x} merupakan bilangan nol")
else:
    print(f"bilangan {x} merupakan bilangan negatif")