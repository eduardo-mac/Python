# Lista representa uma seguência de valores
# Sintaxe: nome_lista = [valores]

n1 = [4,2,5,8,9,1,7]
n2 = [8,12,35,61,34]
valores = n1 + n2
valores[10] = 72

# print(valores[-2])
# print(len(valores))
# print(sorted(valores))
# print(sorted(valores, reverse=True))

# valores.append(87)
# print(valores)
# valores.pop()
# print(valores)
# valores.pop(3)
# print(valores)
# valores.insert(0, 21)
# print(valores)
# print(12 in valores)

# planetas = ['Marte', 'Jupter', 'Terra', 'Uranio', 'Saturno']

# for planeta in planetas:
#     print(planeta)

bebidas = []

for i in range(5):
    print(f'Digite uma bebida favorita: ')
    bebidas.append(input()) # append adiciona

bebidas.sort() # organizar lista por ordem crescente

print(f'\nBebidas escolhidas: ')
for bebida in bebidas:
    print(bebida)

