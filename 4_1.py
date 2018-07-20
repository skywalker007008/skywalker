import math
import random

class line:
	def __init__(self, A, B, C):
		self.A = A
		self.B = B
		self.C = C

	def dis_00(obj):
		dis = C / ((A ** 2 + B ** 2) ** 0.5)
		return dis

	def dis_xy(obj, X, Y):
		dis_x = abs(A * X + B * Y + C)
		dis = dis_x / ((A ** 2 + B ** 2) ** 0.5)
		return dis

	def tri_area(obj):
		if A == 0:
			return 0
		dis_x = abs(C / A)
		if B == 0:
			return 0
		dis_y = abs(B / A)
		area = dis_x * dis_y / 2
		return area

	def ykxb(obj):
		if B == 0:
			print("Not existence",end = '\n')
		else:
			k = A / B
			b = C / B
			print("y=%.2fx+%.3f" % (k,b))

if __name__ == '__main__':
	line_list = []
	i = 0
	while i in range(5):
		D = random.randint(-5, 5)
		B = random.randint(-5, 5)
		C = random.randint(-5, 5)
	
		temp_line = line(D, B, C)
		line_list.append([temp_line,D, B, C])
		i = i + 1

	for i in range(5):
		
		linedata = line_list[i-1]
		linename = linedata[0]
		print('%5d:%dx+%dy+%d=0' %(i,linedata[1],linedata[2],linedata[3]))
		print('The distance of (0,0) is %.2f' %linename.dis_00())
		print('The area of the triangle is %.1f' %linename.tri_area())
		random_x = random.randint(-5, 5)
		random_y = random.randint(-5, 5)
		print('The distance of (%d,%d) is %.2f' %(random_x, random_y, linename.dis_xy(random_x, random_y)))
		linename.ykxb()
		i = i +1
