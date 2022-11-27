#dowolny system konwersja
number = int(input('podaj liczbe '))

pdst = -1

while pdst<2 or pdst>9:
    pdst = int(input('podaj podstawę systemu liczbowego '))
reszta=[]

while number:
    reszta.append(number%pdst)
    number = number//pdst

print(reszta[::-1])


#palendrom 

word = str(input('podaj liczbe'))

if word == word[::-1]:
    print('lizcba jest palindromro')
else:
    print('liczba nie jest palindromem')

#liczba pierwsza

number2 = int(input('podaj liczbe '))

dz = 2
t = -1

pierwiastek = int(round(number2**0.5)+1)

while dz<pierwiastek:
    if number2%dz==0:
        t = 1
        print('nie jest liczba pierwsza a jej dzielnik to '+str(dz))
        break
    dz = dz+1
if t<0:
    print('jest liczba pierwsza')
        
