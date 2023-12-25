"""main file for project """

x = input('Wprowadż liczbę całkowitą...')
if type(int(x)) is type(1):
    x = int(x)
    print(f'Wprowadzono liczbę {x}')
else:
    print('To nie jest liczba całkowita')
input('Kliknij enter aby wyjść zprogramu')

