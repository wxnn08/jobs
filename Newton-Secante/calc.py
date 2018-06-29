import matplotlib.pyplot as plt
import math


""" Funcao para plotar o grafico com maior precisao. Em um 'for' soh e possivel utilizar int """
def decimal_range(start, stop, increment):
    while start < stop:
        yield start
        start += increment


def biseccao (x, it):
	print("# Bisecção")
	m = (x[0]+x[1])/2

	for i in range(0, it):
		f1Value = fx(x[0])
		f2Value = fx(m)
		if f1Value!="?" and f2Value!="?" and fx(x[0])*fx(m)<0:
			x[1]=m
		else:
			x[0]=m
		print("---- Intervalo da {} iteração: [{}, {}]".format(i+1, x[0], x[1]))
		m = (x[0]+x[1])/2
	return x


def secante(x, f, it, eps, plotRange, funcaoMascara):	
	print("\n# Secante")

	plotLeft = x[0]-plotRange
	plotRight = x[1]+plotRange
	raiz = 0

	try:
		plotFuncaoPrincipal(x, funcaoMascara, plotLeft, plotRight)
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
			print("---- x[{}]: {}".format(i, x[i]))
	print("\n** Aperte qualquer tecla para realizar as iteracoes **")
	for i in range (1, len(f)):
		if x[i]!=x[i-1]:
			plotSecante(i, x[i-1], x[i], f[i-1], f[i], plotLeft, plotRight)

	if raiz!="?":
		raiz = str(x[len(x)-1])

	plt.title("{}, raiz = ".format(funcaoMascara) + raiz)


def plotFuncaoPrincipal(x, lblLegenda, plotLeft, plotRight):
	xAxis = []
	yAxis = []
	for i in decimal_range(plotLeft, plotRight, 0.01):
		yValue = fx(i)
		if yValue!="?":
			xAxis.append(i)
			yAxis.append(yValue)

	plt.plot(xAxis, yAxis,"r", label=lblLegenda)
	plt.show()
	plt.draw()
	

def plotSecante(i, x0, x1, f0, f1, plotLeft, plotRight):
	try:
		continua = False
		while continua!=True:
			continua = plt.waitforbuttonpress()

		m = (f1-f0)/(x1-x0)

		xAxis = []
		yAxis = []
		for x in decimal_range(x0-x1/2, x1+x1/2, 0.01):
			y = m*(x-x1)+f1
			xAxis.append(x)
			yAxis.append(y)
		
		lbl = str(i)+" iteração"
		plt.plot(xAxis, yAxis, linewidth=0.8, label = lbl)

		xAxis = [x1, x1]
		yAxis = [0, f1]
		plt.text(x1, 0, "x{}={:.3f}".format(i,x1), fontsize=8)
		plt.plot(xAxis, yAxis, "k--", linewidth=0.8)

		plt.legend()
		plt.draw()

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
	plotRange = 100
	eps = 0.000001
	funcaoMascara = "tmpFuncao"
	
	""" Configuracoes da plotagem """
	plt.ion()
	plt.ylabel("f(x)")
	plt.xlabel("x")
	plt.grid(True)
	plt.title("{}, raiz = ?".format(funcaoMascara))


	""" Verifica se existe uma raiz no intervalo fornecido """
	if fx(x[0])*fx(x[1])<0:

		""" Pensando... """
		print("Processando...")
		print(" ------------------------------------------ ")

		""" Realiza itB iterações pelo método da Bisecção no intervalo dado """
		x = biseccao(x, itB)

		""" Calcula fx para os valores obtidos """
		f=[fx(x[0]), fx(x[1])]

		""" Calcula pelo método das secantes. 

		itSMax = Máximo de iterações realizadas
		eps = epslon: aproximação da secante
		plotRange = Tamanho da plotagem do gráfico """

		secante(x, f, itSMax+1, eps, plotRange, funcaoMascara)	
		print(" ------------------------------------------ \n\n")

		""" Desliga modo iterativo para manter o gráfico gerado na tela, caso contrário ele desaparece muito rápido """
		plt.ioff()
		plt.show()

	else:
		print("Existem mais de uma ou nenhuma raiz no intervalo dado")

if __name__ == "__main__":
    main()
