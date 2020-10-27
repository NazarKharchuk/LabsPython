import math 
full_angle=180

print("Enter the coordinates of the vertex A of the triangle:")
x1 = float(input('x1 = '))        #Координата х вершини А трикутника
y1 = float(input('y1 = '))        #Координата у вершини А трикутника
print("Enter the coordinates of the vertex B of the triangle:")
x2 = float(input('x2 = '))        #Координата х вершини В трикутника
y2 = float(input('y2 = '))        #Координата у вершини В трикутника
print("Enter the coordinates of the vertex C of the triangle:")
x3 = float(input('x3 = '))        #Координата х вершини С трикутника
y3 = float(input('y3 = '))        #Координата у вершини С трикутника

a = float(math.sqrt((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2)))
b = float(math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3)))
c = float(math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)))

if (a + b) > c and (a + c) > b and (b + c) > a and a > 0 and b > 0 and c > 0 :
	angle_A = float((full_angle * math.acos((b * b + c * c - a * a) / (2 * b * c))) / math.pi)
	angle_B = float((full_angle * math.acos((a * a + c * c - b * b) / (2 * a * c))) / math.pi)
	angle_C = float((full_angle * math.acos((a * a + b * b - c * c) / (2 * a * b))) / math.pi)

	print("a = %.2f" %a)
	print("b = %.2f" %b)
	print("c = %.2f" %c)
	print("angle_A = %.4f" %angle_A)
	print("angle_B = %.4f" %angle_B)
	print("angle_C = %.4f" %angle_C)
else :
	print("The triangle does not exist!")
