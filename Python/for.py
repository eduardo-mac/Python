# Sintaxe do for em PY
   # for ITEM in SEQUÊNCIA:
   # intruções executadas para cada item da seguência

#nome = str(input('Escreva seu nome: '))

#for x in range(0,11,1):
#    print(f'{x} {nome}')

# range(valor_final, valor_inicial, incremento) pode trabalhar com esses 3 parêmetros


pedras = ('Rubi','Esmeralda','Quartzo','Safira','Diamante','Turmalina')

for pedra in pedras:
    if pedra == 'Quartzo':
        continue # pula o laço atual, ou seja, não vai exibir o 'Quartzo'
    print(pedra)