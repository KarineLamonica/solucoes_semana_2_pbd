"""Faça um Programa que leia um número e exiba o dia correspondente da semana.
 (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido."""

numero = int (input ("Digite um numero de 1 a 7: "))
 
if numero == 1:
    print ('Domingo')
elif numero == 2:
    print ('Segunda-Feira')
elif numero == 3:
    print ('Terça-Feira')
elif numero == 4: 
    print ('Quarta-Feira')
elif numero == 5:
    print ('Quinta-Feira')
elif numero == 6:
    print ('Sexta-Feira')
elif numero == 7:
    print ('Sábado')
else:
    print ('Valor Inválido')