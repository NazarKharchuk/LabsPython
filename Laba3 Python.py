                #Варіант 9
a = float(input('The first element of the sequence :'))      #Перший елемент послідовності
x = float(input('The value of the variable :'))              #Значення змінної
eps = float(input('Enter a positive accuracy value :'))      #Точність

while eps < 0:
    eps = float(input('Enter a positive value :'))
y0 = a                                                     #Попереднє значення змінної
y1 = 0.5 * (a + (x / a))                                   #Наступне значення змінної
print( 'y0 = %10.6f' % y0 , 'y1 = %10.6f'% y1)
while abs(y1**2 - y0**2) >= eps :
    y0 = y1
    y1 = 0.5 * (y0 + (x/y0))
    print( 'y0 = %10.6f' % y0 , 'y1 = %10.6f'% y1)
yn = y1                                                    #Перше значення, для якого не виконується задана умова
print('yn = %10.6f'% yn)

