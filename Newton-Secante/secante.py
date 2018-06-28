import matplotlib.pyplot as plt

def biseccao (x, it):
	print("# Bisecção")
	m = int((x[0]+x[1])/2)

	for i in range(0, it):
		f1Value = fx(x[0])
		f2Value = fx(m)
		if f1Value!="?" and f2Value!="?" and fx(x[0])*fx(m)<0:
			x[1]=m
		else:
			x[0]=m
		print("---- Intervalo da {} iteração: [{}, {}]".format(i+1, x[0], x[1]))
		m = int((x[0]+x[1])/2)
	return x

def secant(x, f, it, eps, plotRange):	
	print("# Secante")
	xAxis = []
	yAxis = []
	root = 0
	plotLeft = int(x[0]-plotRange)
	plotRight = int(x[1]+plotRange)
	for i in range(plotLeft, plotRight):
		yValue = fx(i)
		if yValue!="?":
			xAxis.append(i)
			yAxis.append(yValue)

	funcao = " x**2-6 "
	plt.plot(xAxis, yAxis, label=funcao)

	try:
		cont = 2 
		while cont<it and abs(fx(len(x)-1)):
			xValue = x[cont-1]-((f[cont-1]*(x[cont-1]-x[cont-2]))/(f[cont-1]-f[cont-2]))
			x.append(xValue)
			fValue = fx(xValue)
			f.append(fValue)
			cont+=1

	except ZeroDivisionError:
		print("ERRO #01: Divisao por zero")
	except TypeError:
		print("ERRO #02: TypeError")
		root = "?"

	for i in range (2, len(f)):
		fSec(i, x[i-1], x[i], f[i-1], f[i], plotLeft, plotRight)

	if root!="?":
		root = str(x[len(x)-1])

	plt.title("{}, raiz = ".format(funcao) + root)
	plt.ylabel("f(x)")
	plt.xlabel("x")
	plt.legend()
	plt.grid(True)
	plt.show()

def fSec(i, x0, x1, f0, f1, plotLeft, plotRight):
	try:
		m = (f1-f0)/(x1-x0)
		xAxis = [x1]
		yAxis = [f1]
		for x in range(plotLeft, plotRight):
			y = m*(x-xAxis[0])+yAxis[0]
			xAxis.append(x)
			yAxis.append(y)
		lbl = str(i-1)+" iteração"
		plt.plot(xAxis, yAxis,"--", label = lbl)

	except ZeroDivisionError:
		print("ERRO #03: Divisao por zero")

def fx(x):
	try:
		return x**2-6

	except ZeroDivisionError:
		print("ERRO #04: Divisao por zero")
		return "?"

	except TypeError:
		print("ERRO #05: TypeError")
		

def main():
	x=[0, 100000]
	itSMax = 100
	itB = 7
	plotRange = 1000
	eps = 0.00001
	
	if fx(x[0])*fx(x[1])<0:
		x = biseccao(x, itB)

		f=[fx(x[0]), fx(x[1])]

		secant(x, f, itSMax+1, eps, plotRange)	

	else:
		print("Nao existem raizes no intervalo dado")

if __name__ == "__main__":
    main()
