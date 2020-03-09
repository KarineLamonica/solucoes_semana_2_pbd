"""Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual
operação ele deseja realizar. O resultado da operação deve ser acompanhado de
uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal."""

n1 = float (input ("Digite um numero: "))
n2 = float (input ("Digite mais um numero: "))

operação = input ("Qual operação você deseja fazer? (+, -, *, /):")

if operação == '+':
    resultado =  n1 + n2
    if resultado %2 == 0:
        print ("O numero %d é PAR!" % resultado)
    else:
        print ("O numero %d é IMPAR!" % resultado)
    if resultado >= 0:
        print ("O numero %d é POSITIVO!" % resultado)
    else:
        print ("O numero %d é NEGATIVO!" % resultado)
    
    if round (resultado) == resultado:
        print ("O numero %d é INTEIRO!" % resultado)
    else:
        print ("O numero %.1f é DECIMAL!" % resultado)

if operação == '-':
    resultado =  n1 - n2
    if resultado %2 == 0:
        print ("O numero %d é PAR!" % resultado)
    else:
        print ("O numero %d é IMPAR!" % resultado)
    if resultado >= 0:
        print ("O numero %d é POSITIVO!" % resultado)
    else:
        print ("O numero %d é NEGATIVO!" % resultado)
    
    if round (resultado) == resultado:
        print ("O numero %d é INTEIRO!" % resultado)
    else:
        print ("O numero %.1f é DECIMAL!" % resultado)

if operação == '*':
    resultado =  n1 * n2
    if resultado %2 == 0:
        print ("O numero %d é PAR!" % resultado)
    else:
        print ("O numero %d é IMPAR!" % resultado)
    if resultado >= 0:
        print ("O numero %d é POSITIVO!" % resultado)
    else:
        print ("O numero %d é NEGATIVO!" % resultado)
    
    if round (resultado) == resultado:
        print ("O numero %d é INTEIRO!" % resultado)
    else:
        print ("O numero %.1f é DECIMAL!" % resultado)

if operação == '/':
    resultado =  n1 / n2
    if resultado %2 == 0:
        print ("O numero %d é PAR!" % resultado)
    else:
        print ("O numero %d é IMPAR!" % resultado)
    if resultado >= 0:
        print ("O numero %d é POSITIVO!" % resultado)
    else:
        print ("O numero %d é NEGATIVO!" % resultado)
    
    if round (resultado) == resultado:
        print ("O numero %d é INTEIRO!" % resultado)
    else:
        print ("O numero %.1f é DECIMAL!" % resultado)

    




