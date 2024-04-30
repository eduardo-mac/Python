
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))

resultado = (idade >= 18) and (altura >= 1.65)

msg = 'Posso participar do evento ? 5' + str(resultado)

print(msg)

# and = e / or = ou / not = inverte o estado lógico
