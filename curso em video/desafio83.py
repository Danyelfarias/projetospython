# lista = {'nome':'danyel'}
# print(lista)
# print(lista['nome'])
cadastrado={}
alunos={'nome':'','media':'','situacao':''}
aluno=str(input('nome: '))

alunos['nome']=aluno
media=float(input('media: '))
alunos['media']=media
if alunos['media']>6:

    alunos['situacao']="aprovado"
else:
    alunos['situacao']='reprovado'
print(f'o aluno {alunos["nome"]} foi {alunos["situacao"]} , pois tirou {alunos["media"]} na media')
