#! /usr/bin/python3.6

def calcdiasperdidos(cigdia,anosfum):
    try:
        doomdays = (int(cigdia) * (10/1440)) * (int(anosfum) * 365)
        return 'Parabéns! Seus dias de vida foram reduzidos em {} dias'.format(int(round(doomdays)))
    except:
        return 'Algo deu errado. Tente novamente'

cigdia = input('Quantos cigarros fuma por dia?')
anosfum = input('Há quantos anos fuma?')

print(calcdiasperdidos(cigdia,anosfum))
