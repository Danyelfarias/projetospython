# def notas(*n):
#     global lista
#     resul={'totalnotas':'','maior':'','menor':'','media':''}
    
#     resul['totalnotas']=len(lista)
#     # if n>lista[1]:
#     #     mai=lista
#     mai=0
#     for n in lista:
#         if n>mai:
#             mai=n
    
#     mai=resul['maior']
#     men=0
#     for n in lista:
#         if n<men:
#             men=n
#     men=resul['menor']
#     quant=0
#     for n in lista:
#         quant+=n
#     resul['media']=quant / len(lista)
    

    
#     return resul

# lista=[]
# while 5<len(lista):
#     num=input('digite um numero: ')
#     lista.append(num)
# rsp=notas(lista)
# print(rsp)
def notas(*n):
    global lista
    resul = {'totalnotas': '', 'maior': '', 'menor': '', 'media': ''}

    resul['totalnotas'] = len(lista)
    
    mai = float('-inf')  # Inicializa a variável "mai" com o menor valor possível
    for num in lista:
        if num > mai:
            mai = num
    resul['maior'] = mai

    men = float('inf')  # Inicializa a variável "men" com o maior valor possível
    for num in lista:
        if num < men:
            men = num
    resul['menor'] = men

    quant = 0
    for num in lista:
        quant += num
    resul['media'] = quant / len(lista)

    return resul

lista = []
while len(lista) < 5:  # Agora o loop continua até que a lista tenha 5 elementos
    num = int(input('Digite um número: '))
    lista.append(num)

rsp = notas(lista)
print(rsp)

