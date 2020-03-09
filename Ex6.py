"""O Hipermercado Tabajara está com uma promoção de carnes que é
imperdível. Confira: 
                     Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos
de carne da promoção, porém não há limites para a quantidade de carne por
cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e
a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo
as informações da compra: tipo e quantidade de carne, preço total, tipo de
pagamento, valor do desconto e valor a pagar."""

print ('BEM VINDO AO HIPERMERCADO TABAJARA')

tipo = int (input ('Escolha seu tipo de carne:\n[0] Filé Duplo\n[1] Alcatra\n[2] Picanha\ntipo: '))
quantidade = float (input ('Digite a quantidade de carne em KG: '))
cliente = input('Você é cliente Tabajara? '). upper().strip()[0]
carne = ('Filé Duplo', 'Alcatra', 'Picanha')

if tipo == 0:
    if quantidade <= 5:
        if cliente == 'S':
            filé_duplo = 4.90 * quantidade 
            desconto = filé_duplo - (filé_duplo * 5 / 100)
            desc = filé_duplo - desconto
            print ('-=' * 30)
            print ('Cliente Cartão Tabajara')
            print (f'Tipo de Carne: {carne[tipo]}')
            print (f'Quantidade de carne: {quantidade:.2f} KG')
            print (f'Valor total: {filé_duplo:.2f}')
            print ('Desconto de 5% na compra com Cartão Tabajara')
            print (f'Valor do desconto: {desc:.2f}')
            print (f'Total a pagar: {desconto:.2f}')
            print ('-=' * 30)

        else:
            filé_duplo = 4.90 * quantidade 
            print ('-=' * 30)
            print (f'Tipo de Carne: {carne[tipo]}')
            print (f'Quantidade de carne: {quantidade:.2f}KG')
            print (f'Pagará ao total: R$ {filé_duplo:.2f}')
            print ('-=' * 30)

    elif quantidade > 5:
        if cliente == 'S':
            filé_duplo = 5.80 * quantidade 
            desconto = filé_duplo - (filé_duplo * 0.05)
            desc = filé_duplo - desconto
            print ('-=' * 30)
            print ('Cliente Cartão Tabajara')
            print (f'Tipo de Carne: {carne[tipo]}')
            print (f'Quantidade de carne: {quantidade:.2f} KG')
            print (f'Valor total: {filé_duplo:.2f}')
            print ('Desconto de 5% na compra com Cartão Tabajara')
            print (f'Valor do desconto: {desc:.2f}')
            print (f'Total a pagar: {desconto:.2f}')
            print ('-=' * 30)
        
        else:
            filé_duplo = 5.80 * quantidade 
            print ('-=' * 30)
            print (f'Tipo de Carne: {carne[tipo]}')
            print (f'Quantidade de carne: {quantidade:.2f}KG')
            print (f'Pagará ao total: R$ {filé_duplo:.2f}')
            print ('-=' * 30)

if tipo == 1:
    if quantidade <= 5:
        if cliente == 'S':
            alcatra = 5.90 * quantidade 
            desconto = alcatra - (alcatra * 5 / 100)
            desc = alcatra - desconto
            print ('-=' * 30)
            print ('Cliente Cartão Tabajara')
            print (f'Tipo de Carne: {carne[tipo]}')
            print (f'Quantidade de carne: {quantidade:.2f} KG')
            print (f'Valor total: {alcatra:.2f}')
            print ('Desconto de 5% na compra com Cartão Tabajara')
            print (f'Valor do desconto: {desc:.2f}')
            print (f'Total a pagar: {desconto:.2f}')
            print ('-=' * 30)

        else:
            alcatra = 5.90 * quantidade 
            print ('-=' * 30)
            print (f'Tipo de Carne: {carne[tipo]}')
            print (f'Quantidade de carne: {quantidade:.2f}KG')
            print (f'Pagará ao total: R$ {alcatra:.2f}')
            print ('-=' * 30)

    elif quantidade > 5:
        if cliente == 'S':
            alcatra = 6.80 * quantidade 
            desconto = alcatra - (alcatra * 0.05)
            desc = alcatra - desconto
            print ('-=' * 30)
            print ('Cliente Cartão Tabajara')
            print (f'Tipo de Carne: {carne[tipo]}')
            print (f'Quantidade de carne: {quantidade:.2f} KG')
            print (f'Valor total: {alcatra:.2f}')
            print ('Desconto de 5% na compra com Cartão Tabajara')
            print (f'Valor do desconto: {desc:.2f}')
            print (f'Total a pagar: {desconto:.2f}')
            print ('-=' * 30)
        
        else:
            alcatra = 6.80 * quantidade 
            print ('-=' * 30)
            print (f'Tipo de Carne: {carne[tipo]}')
            print (f'Quantidade de carne: {quantidade:.2f}KG')
            print (f'Pagará ao total: R$ {alcatra:.2f}')
            print ('-=' * 30)

if tipo == 2:
    if quantidade <= 5:
        if cliente == 'S':
            picanha = 6.90 * quantidade 
            desconto = picanha - (picanha * 5 / 100)
            desc = picanha - desconto
            print ('-=' * 30)
            print ('Cliente Cartão Tabajara')
            print (f'Tipo de Carne: {carne[tipo]}')
            print (f'Quantidade de carne: {quantidade:.2f} KG')
            print (f'Valor total: {picanha:.2f}')
            print ('Desconto de 5% na compra com Cartão Tabajara')
            print (f'Valor do desconto: {desc:.2f}')
            print (f'Total a pagar: {desconto:.2f}')
            print ('-=' * 30)

        else:
            picanha = 6.90 * quantidade 
            print ('-=' * 30)
            print (f'Tipo de Carne: {carne[tipo]}')
            print (f'Quantidade de carne: {quantidade:.2f}KG')
            print (f'Pagará ao total: R$ {picanha:.2f}')
            print ('-=' * 30)

    elif quantidade > 5:
        if cliente == 'S':
            picanha = 7.80 * quantidade 
            desconto = picanha - (picanha * 0.05)
            desc = picanha - desconto
            print ('-=' * 30)
            print ('Cliente Cartão Tabajara')
            print (f'Tipo de Carne: {carne[tipo]}')
            print (f'Quantidade de carne: {quantidade:.2f} KG')
            print (f'Valor total: {picanha:.2f}')
            print ('Desconto de 5% na compra com Cartão Tabajara')
            print (f'Valor do desconto: {desc:.2f}')
            print (f'Total a pagar: {desconto:.2f}')
            print ('-=' * 30)
        
        else:
            picanha = 7.80 * quantidade 
            print ('-=' * 30)
            print (f'Tipo de Carne: {carne[tipo]}')
            print (f'Quantidade de carne: {quantidade:.2f}KG')
            print (f'Pagará ao total: R$ {picanha:.2f}')
            print ('-=' * 30)