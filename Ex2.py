"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
A atribuição de conceitos obedece à tabela abaixo:  
Média de Aproveitamento  Conceito  
Entre 9.0 e 10.0            A      
Entre 7.5 e 9.0             B      
Entre 6.0 e 7.5             C     
Entre 4.0 e 6.0             D      
Entre 4.0 e zero            E       
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente 
e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E."""
 
n1 = float (input("Digite sua primeira nota: "))
n2 = float (input("Digite sua segunda nota: "))
 
media = (n1+n2) / 2

#notaA
if media >= 9.0 and media < 10:
    print ('A nota da primeira prova: ', n1)
    print ('A nota da segunda prova: ', n2)
    print ('Você tirou um A!')
    print ('Sua media é de: ', media)
    print ('Você foi aprovado')

#notaB
if media >= 7.5 and media < 9.0:
    print ('A nota da primeira prova: ', n1)
    print ('A nota da segunda prova: ', n2)
    print ('Você tirou um B!')
    print ('Sua media é de: ', media)
    print ('Você foi aprovado')

#notaC
if media >= 6.0 and media < 7.5:
    print ('A nota da primeira prova: ', n1)
    print ('A nota da segunda prova: ', n2)
    print ('Você tirou um C!')
    print ('Sua media é de: ', media)
    print ('Você foi aprovado')

#notaD
if media >= 4.0 and media < 6.0:
    print ('A nota da primeira prova: ', n1)
    print ('A nota da segunda prova: ', n2)
    print ('Você tirou um D!')
    print ('Sua media é de: ', media)
    print ('Você foi reprovado')

#notaE
if media < 4.0:
    print ('A nota da primeira prova: ', n1)
    print ('A nota da segunda prova: ', n2)
    print ('Você tirou um E!')
    print ('Sua media é de: ', media)
    print ('Você foi reprovado')