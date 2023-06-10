a= 0
b=float('inf')
for pesados in range(1,5):
    peso=float(input("qual é seu peso: "))
   
    if peso>a:
        a=peso
    if peso<b:
        b=peso
print(f"o maior peso entre esse é {a}")
print(f"o menor peso entre esse é {b}")

        