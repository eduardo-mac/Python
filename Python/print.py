# Sintaxe
# print (objetos, argumentos)

nome = str(input('Digite seu nome: '))
idade = int(input('Escreva sua idade: '))
msg = 'Olá ' + nome + '! Seja bem vindo' # concatenação
msg_formatada = 'O seu nome é {0} e você tem {1} anos de idade'.format(nome, idade)
msg_f = f' {nome} você é agraciado! Daqui a 30 anos você terá {idade + 30}'
print(msg, end='') #end é para não pular a linha
print(msg_f)
print(msg_formatada)

