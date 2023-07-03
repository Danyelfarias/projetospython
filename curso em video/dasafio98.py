def maior (*num):
    maior=0
    for n in num:
        if n>maior:
            maior=n
    
    print(maior)


maior(2,3,1)
# def maior(*num):
#     maior_num = float('-inf')  # Inicializa o maior_num com um valor muito pequeno

#     for n in num:
#         if n > maior_num:
#             maior_num = n

#     print(maior_num)

# maior(2, 3, 1)
