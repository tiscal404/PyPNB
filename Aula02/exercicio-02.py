#! /usr/bin/python3.6

def mtomm(x):
    try:
        y = int(x) * 1000
        return '{}mm'.format(y)
    except:
        return 'Sorry. Something went wrong!'

print('Aula02 - Exercício 2\nConvert meters to millimeters\n' + '=' * 29)
print(mtomm(input('Meters:')))
