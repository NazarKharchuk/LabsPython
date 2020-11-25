        #Variant 2
first_number=22200
for i in range(0, 10):
   number1 = first_number + i * 10
   for j in range(0, 10): 
       number2 = number1 + j
       if number2 % 15 == 0:
           print(number2)

