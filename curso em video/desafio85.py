# lista= []
# par=[]
# inpar=[]
# cont=0
# for n in range(8):
#     lista.append(int(input('digite um numero')))
# for n in lista:
#         if n%2==0:
#             par.append(n)
#         else:
#             inpar.append(n)
# print(sorted(lista))
# print(sorted(par))
# print(sorted(inpar))
# soluçao guanbara
lista=[[],[]]
for c in range(8):
    num= int(input('digite um número: '))
    if num %2==0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print(lista[0])
print(lista[1])

