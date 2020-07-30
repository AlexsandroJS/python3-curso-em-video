"""
EXERCÍCIO 079: Valores Únicos em uma Lista

Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.
"""
numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar [S/N]? '))
    if r in 'Nn':
        break
print('-=' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros}')

############# adicionando essse abaixo para voce comparar e testar, observe que quando voce digita algum numero no lugar da resposta acaba aceitando 
############# eu fiz outro while para que nao aceite ate que seja dado a resposta correta, da uma olhadinha
lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        print(f'{valor} adicionado com sucesso')
        lista.append(valor)
    else:
        print('Valor duplicado! Nao vou adicionar...')
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
lista.sort()
print('-=' *30)
print(f'Os valores digitados foram {lista}')
