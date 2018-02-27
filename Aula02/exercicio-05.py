#! /usr/bin/python3.6

def calcdesconto(preco,desconto):
    try:
        x = float(preco)
        y = float(desconto)
        desc = x * (y / 100)
        precodesc = x - desc
        return 'Desconto: R$ {}. Total a pagar: R$ {}'.format(round(desc), round(precodesc))
    except:
        return 'Desculpe! Ago deu errado. Tente novamente.'

preco = input('Informe o preço do produto:')
desconto = input('Informe o preço do desconto:')

print(calcdesconto(preco,desconto))
