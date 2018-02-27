#! /usr/bin/python3.6

from datetime import datetime

def ageinseconds(y,m,d):
    try:
        birthday = datetime(int(y),int(m),int(d))
        diff = (datetime.now() - birthday).total_seconds()
        return 'You have lived {} seconds so far'.format(diff)
    except:
        return 'Sorry. Something went wrong!'


print('Aula02 - Exercício 3\nCalculate age in seconds\n' + '=' * 29)
y = input('Enter the year you were born:')
m = input('Enter the month you were born:')
d = input('Enter the day you were born:')
print(ageinseconds(y,m,d))
