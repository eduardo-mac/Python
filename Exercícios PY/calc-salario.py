ganho_hora = float(input('Digite quanto voçe ganha por hora trabalhada: '))
horas_trabalhadas = float(input('Quantas horas trabalhou esse mês? '))

salarioBruto = ganho_hora * horas_trabalhadas
inss = salarioBruto * 0.08
ir = salarioBruto * 0.11
sinditato = salarioBruto * 0.05
salarioLiquido = salarioBruto - inss - ir - sinditato

print(f'Salario Bruto: {salarioBruto}')
print(f'Desconto INSS: {inss}')
print(f'Desconto IR: {ir}')
print(f'Sindicato: {sinditato}')
print(f'Salario Liquidp: {salarioLiquido}')
