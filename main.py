"""main file for project """

x = input('Wprowadż liczbę całkowitą...')
if  x.isnumeric():
    x = int(x)
    print(f'Wprowadzono liczbę {x}')
else:
    print('To nie jest liczba całkowita')
input('Kliknij enter aby wyjść z programu...')

