import matplotlib.pyplot as plt
import numpy as np
import math




def decimal_range(start, stop, increment):
    while start < stop: # and not math.isclose(start, stop): Py>3.5
        yield start
        start += increment




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




def secante(x, f, it, eps, plotRange):	
	print("# Secante")

	plotLeft = int(x[0]-plotRange)
	plotRight = int(x[1]+plotRange)
	funcao = "tmpFuncao"
	raiz = 0

	try:
		plotFuncaoPrincipal(x, funcao, plotLeft, plotRight)
		cont = 2 
		while cont<it and abs(fx(len(x)-1))>eps and f[cont-1]!=f[cont-2]:
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

	for i in range (1, len(f)):
		if x[i]!=x[i-1]:
			plotSecante(i, x[i-1], x[i], f[i-1], f[i], plotLeft, plotRight)

	if raiz!="?":
		raiz = str(x[len(x)-1])

	plt.title("{}, raiz = ".format(funcao) + raiz)




def plotFuncaoPrincipal(x, nome, plotLeft, plotRight):
	xAxis = []
	yAxis = []
	for i in decimal_range(plotLeft, plotRight, 0.01):
		yValue = fx(i)
		if yValue!="?":
			xAxis.append(i)
			yAxis.append(yValue)

	plt.plot(xAxis, yAxis,"r", label=nome)
	plt.draw()

	continua = False
	while continua!=True:
		if plt.waitforbuttonpress()==True:
			continua = True




def plotSecante(i, x0, x1, f0, f1, plotLeft, plotRight):
	try:
		print("---- x[{}]: {}".format(i, x1))
		m = (f1-f0)/(x1-x0)

		xAxis = []
		yAxis = []
		for x in decimal_range(x0-x1*0.5, x1+x1*0.5, 0.01):
			y = m*(x-x1)+f1
			xAxis.append(x)
			yAxis.append(y)
		
		plt.plot(xAxis, yAxis, linewidth=0.8)
		plt.legend()
		plt.draw()
		plt.waitforbuttonpress()

		lbl = str(i)+" iteração"
		#plt.plot(xAxis, yAxis, linewidth=2, label = lbl)

		xAxis = [x1, x1]
		yAxis = [0, f1]
		plt.text(x1, 0, "x"+str(i))
		plt.plot(xAxis, yAxis, "k--", linewidth=0.8)

		plt.draw()
		plt.waitforbuttonpress()

	except ZeroDivisionError:
		print("ERRO #03: Divisao por zero")




def fx(x):
	try:
		return math.sin(x)

	except ZeroDivisionError:
		print("ERRO #04: Divisao por zero")
		return "?"

	except TypeError:
		print("ERRO #05: TypeError")




def main():
	""" Configuracoes passadas pelo usuario """
	x=[1, 4]
	itSMax = 100
	itB = 7
	plotRange = 5 
	eps = 0.001
	funcao = "tmpFuncao"
	
	""" Configuracoes da plotagem """
	plt.ion()
	plt.show()
	plt.ylabel("f(x)")
	plt.xlabel("x")
	plt.grid(True)
	plt.title("{}, raiz = ?".format(funcao))


	""" Verifica se existe uma raiz no intervalo fornecido """
	if fx(x[0])*fx(x[1])<0:
		print("Processando...")
		""" Realiza itB iterações pelo método da Bisecção no intervalo dado """
		x = biseccao(x, itB)

		""" Calcula fx para os valores obtidos """
		f=[fx(x[0]), fx(x[1])]

		""" Calcula pelo método das secantes. 

		itSMax = Máximo de iterações realizadas
		eps = Aproximação pela secante
		plotRange = Tamanho da plotagem do gráfico """

		secante(x, f, itSMax+1, eps, plotRange)	
		plt.waitforbuttonpress()

	else:
		print("Existem mais de uma ou nenhuma raiz no intervalo dado")

if __name__ == "__main__":
    main()
