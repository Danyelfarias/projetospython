a = float(input("lado 1: "))
b = float(input("lado 2: "))
c = float(input("lado 3: "))

if a == b == c:
    print("equilátero")
elif a == b != c or b == c != a or a == c != b:
    print("isósceles")
else:
    print("escaleno")

#else:
    #print(".")