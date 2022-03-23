a, b, c = map(float, input().split())

delta = ((b ** 2)- 4 * a * c)

if((delta < 0) or a == 0):
	print( "Impossivel calcular")
	
elif ( delta == 0 ):
	rl1 = (-b + delta ** (1 / 2))/(2 * a)
	rl2 = rl1
	print("R1 = %.5f" % (rl1))
	print("R2 = %.5f" % (rl2))

else:
	rl1 = (-b + delta ** (1 / 2))/(2 * a)
	rl2 = (-b - delta ** (1 / 2))/(2 * a)
	print("R1 = %.5f" % (rl1))
	print("R2 = %.5f" % (rl2))