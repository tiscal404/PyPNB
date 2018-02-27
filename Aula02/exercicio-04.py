#! /usr/bin/python3.6

def aumentosalario(salario,aumento):
    try:
        return round(float(salario) * (1 + (float(aumento) / 100)),2)
    except:
        return 'Desculpe. Algo deu errado! Tente novamente.'

salario = input('Informe seu salário atual:')
aumento = input('Informe o valor do aumento:')

print(aumentosalario(salario,aumento))
