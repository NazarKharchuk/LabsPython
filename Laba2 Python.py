a = float(input('Add rib a brick :'))  #Ребро a цеглини
b = float(input('Add rib b brick :'))  #Ребро b цеглини
c = float(input('Add rib c brick :'))  #Ребро c цеглини 
if (a > 0 and b > 0 and c > 0):
    x = float(input('Enter size x hole :'))  #Розмір x отвору
    y = float(input('Enter size y hole :'))  #Розмір y отвору
    if (x > 0 and y > 0):
        if (x >= a and y >= b or x >= b and y >= a):
            print('Will fit')
        else:
            if (x >= c and y >= a or x >= a and y >= c):
                print('Will fit')
            else:
                if (x >= c and y >= b or x >= b and y >= c):
                    print('Will fit')
                else:
                    print('Not will fit')
    else:
        print('Invalid values entered')
else:
    print('Invalid values entered')
