# latihan genap-ganjil

x = int(input("masukkan bilangan: "))

if x > 0:
    if x % 2 == 0:
        print(f"bilangan {x} merupakan bilangan positif genap")
    else:
        print(f"bilangan {x} merupakan bilangan positif ganjil")
elif x < 0:
    if x % 2 == 0:
        print(f"bilangan {x} merupakan bilangan negatif genap")
    else:
        print(f"bilangan {x} merupakan bilangan negatif ganjil")
else:
    print(f"bilangan {x} merupakan bilangan nol")