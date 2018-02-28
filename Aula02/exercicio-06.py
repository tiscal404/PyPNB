#! /usr/bin/python3.6

def calctempoviagem(s,vm):
    try:
        t = float(s) / float(vm)
        return 'Tempo estimado da viagem: {}h'.format(t)
    except:
        return 'Algo deu errado. Por favor tente novamente!'

dist = input('Qual distância irá percorrer?(Km)')
vm = input('Qual a velocidade média estimada? (Km/h)')

print(calctempoviagem(dist,vm))
