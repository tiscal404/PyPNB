#! /usr/bin/python3.6

def calcpreco(kmrod,dias):
    try:
        precokmrod = float(kmrod) * 0.15
        precodias = round(float(dias)) * 60
        return 'Preço por km rodado: R$ {}\nAluguel dias: {}\nTotal a pagar: R$ {}'.format(precokmrod, precodias, precokmrod + precodias)
    except:
        return 'Algo deu errado. Tente novamente!'

kmrod = input('Informe a quilometragem rodada?')
dias = input('Quantos dias ficou com o carro?')

print(calcpreco(kmrod,dias))
