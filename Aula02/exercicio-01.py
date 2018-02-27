def addition(a,b):
    try:
        c = int(a) + int(b)
        return "{}+{}={}".format(a,b,c)
    except:
        return 'Sorry, something went wrong! Only integer numbers are accepted.'

print('Aula02 - Exercício 1\nMath Operation - Addition\n' + '=' * 25)
x = input('Enter the first number:')
y = input('Enter the second number:')

print(addition(x,y))