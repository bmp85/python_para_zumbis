#6) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu 
#salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa 
#que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. 
#Calcule os descontos e o salário líquido, conforme a tabela abaixo:
 #   a. + Salário Bruto : R$
 #  b. - IR (11%) : R$
 #   c. - INSS (8%) : R$
 #   d. - Sindicato ( 5%) : R$
 #   e. = Salário Liquido : R$
 
valor_hora = float(input("Valor hora: "))
horas_mes = int(input(" Horas trabalhadas no mes: "))

salario_bruto  = valor_hora * horas_mes 

imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

salario = salario_bruto - imposto_renda -inss - sindicato

print (f'+Salário Bruto:\t\t R$ {salario_bruto:.2f}')
print (f'-IR:\t\t\t R$ {imposto_renda:.2f}')
print (f'-INSS:\t\t\t R$ {inss:.2f}')
print (f'-Sindicato:\t\t R$ {sindicato:.2f}')
print (f'=Salário Líquido:\t R$ {salario:.2f}')
