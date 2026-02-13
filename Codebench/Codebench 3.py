def Percentual(x,y):
	percentual = (x*y)/100
	return percentual

a = int(input())
b = int(input())

resultado = Percentual(a,b)
print("%.2f" % resultado)