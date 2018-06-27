import matplotlib.pyplot as plt

def biseccao (x, it):
	m = int((x[0]+x[1])/2)

	for i in range(0, it):
		if fx(x[0])*fx(m)<0:
			x[1]=m
		else:
			x[0]=m
		m = int((x[0]+x[1])/2)
	return x

def secante(x, f, it, eps, TAM):	
	xAxis = []
	yAxis = []
	raiz = 0
	TAMINF = int(x[0]-TAM)
	TAMSUP = int(x[1]+TAM)
	for i in range(TAMINF, TAMSUP):
		yValue = fx(i)
		if yValue!="?":
			xAxis.append(i)
			yAxis.append(yValue)

	funcao = "x^2"
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
		raiz = "?"

	for i in range (2, len(f)):
		fSec(i, x[i-1], x[i], f[i-1], f[i], TAMINF, TAMSUP)

	if raiz!="?":
		raiz = str(x[len(x)-1])

	plt.title("{}, raiz = ".format(funcao) + raiz)
	plt.ylabel("f(x)")
	plt.xlabel("x")
	plt.legend()
	plt.grid(True)
	plt.show()

def fSec(i, x0, x1, f0, f1, TAMINF, TAMSUP):
	try:
		m = (f1-f0)/(x1-x0)
		xAxis = [x1]
		yAxis = [f1]
		for x in range(TAMINF, TAMSUP):
			y = m*(x-xAxis[0])+yAxis[0]
			xAxis.append(x)
			yAxis.append(y)
		lbl = str(i-1)+" iteração"
		plt.plot(xAxis, yAxis,"--", label = lbl)

	except ZeroDivisionError:
		print("ERRO #03: Divisao por zero")

def fx(x):
	try:
		return (x**2)-6
	except ZeroDivisionError:
		print("ERRO #04: Divisao por zero")
		return "?"

def main():
	""" Configuracoes passadas pelo usuario """
	x=[0, 100000]
	itSMax = 100
	itB = 7
	TAM = 1000
	eps = 0.0001
	
	""" Verifica se existe uma raiz no intervalo fornecido """
	if fx(x[0])*fx(x[1])<0:
		x = biseccao(x, itB)
		print("x0:{}\tx1:{}".format(x[0],x[1]))
		f=[fx(x[0]), fx(x[1])]
		secante(x, f, itSMax+1, eps, TAM)
	else:
		print("Nao existem raizes no intervalo dado")

if __name__ == "__main__":
    main()
