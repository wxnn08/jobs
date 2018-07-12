import matplotlib.pyplot as plt
import tkinter as tk
import math

arquivo = open("input.txt", "r")
func = arquivo.read()

""" Funcao para plotar o grafico com maior precisao. Em um 'for' soh e possivel utilizar int, agora da pra usar numeros decimais """
def decimal_range(start, stop, increment):
	while start < stop:
		yield start
		start += increment


def biseccao (x, it):
	print("# Bisecção")
	m = (x[0]+x[1])/2

	""" Algoritmo da bisseccao """
	for i in range(0, it):
		if fx(x[0])*fx(m)<0:
			x[1]=m
		else:
			x[0]=m
		print("---- Intervalo da {} iteração: [{}, {}]".format(i+1, x[0], x[1]))
		m = (x[0]+x[1])/2
	return x


def secante(x, f, it, eps, plotRange, funcaoMascara):	
	print("\n# Secante")

	""" Area de plotagem """ 
	""" Fiquei chutando uns valores ate dar certo, mas da pra usar o valor de plotRange passado na funcao"""
	plotLeft = x[0] - plotRange # Limite a esquerda da plotagem
	plotRight = x[1] + plotRange # Limite a direita da plotagem
	raiz = "0"

	try:
		plotFuncaoPrincipal(x, funcaoMascara, plotLeft, plotRight) # Plota funcao principal

		cont = 2 
		while cont<it and abs(f[cont-1]-f[cont-2])>eps and f[cont-1]!=f[cont-2]:
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
		raiz = "{:.15f}".format(x[len(x)-1])

	plt.title("{}, raiz = ".format(funcaoMascara) + raiz)


def plotFuncaoPrincipal(x, lblLegenda, plotLeft, plotRight):
	xAxis = []
	yAxis = []
	for i in decimal_range(plotLeft, plotRight, 0.01):
		yValue = fx(i)
		if yValue!="?":
			xAxis.append(i)
			yAxis.append(yValue)

	plt.plot(xAxis, yAxis,"r", linewidth=1.5 , label=lblLegenda)
	plt.show()
	

def plotSecante(i, x0, x1, f0, f1, plotLeft, plotRight):
	try:
		continua = False
		while continua!=True:
			continua = plt.waitforbuttonpress()

		m = (f1-f0)/(x1-x0)

		xAxis = []
		yAxis = []
		for x in decimal_range(plotLeft, plotRight, 0.01):
			y = m*(x-x1)+f1
			xAxis.append(x)
			yAxis.append(y)
		
		lbl = "{} iteracao, x{} = {:.3f}".format(i,i,x1)
		#plt.text(xAxis[len(xAxis)-1], yAxis[len(yAxis)-1], "i{}".format(i))
		plt.plot(xAxis, yAxis, "--", linewidth=0.9, label = lbl)

		xAxis = [x1, x1]
		yAxis = [0, f1]
		plt.plot(xAxis, yAxis, "k--", linewidth=0.8)

		plt.legend()
		plt.draw()

	except ZeroDivisionError:
		print("ERRO #03: Divisao por zero")


def fx(x):
	try:
		return float(eval(func))

	except ZeroDivisionError:
		print("ERRO #04: Divisao por zero")
		return "?"

	except TypeError:
		print("ERRO #05: TypeError")
	 
def main():
	
	""" Entradas da interface para o usuario """
	comeco = entradaA.get()
	fim = entradaB.get()
	precisao = entradaEpslon.get()
	maxIt = entradaMaxIt.get()
	plotArea = entradaPlotArea.get()
	entradas.destroy()

	""" Configuracoes para os calculos """
	x=[float(comeco), float(fim)]
	itSMax = int(maxIt)
	itB = 7
	eps = float(precisao)
	plotRange = int(plotArea)
	
	
	""" Configuracoes da plotagem """
	arquivo2 = open("title.txt", "r")
	funcaoMascara = arquivo2.read()


	plt.ion()
	plt.ylabel("f(x)")
	plt.xlabel("x")
	plt.grid(True)
	plt.title("{}, raiz = ?".format(funcaoMascara))

	""" Pensando... """
	print("Processando ...")
	print(" -> Funcao: {}".format(funcaoMascara))
	print(" -> Inicio do intervalo: {}".format(comeco))
	print(" -> Fim do intervalo: {}".format(fim))
	print(" -> Precisao: {}".format(precisao))
	print(" -> Max. Iteracoes: {}".format(maxIt))



	""" Verifica se existe uma raiz no intervalo fornecido """
	try: 
		if fx(x[0])*fx(x[1])<0:

			print(" ------------------------------------------ ")

			""" Realiza itB iterações pelo método da Bisecção no intervalo dado """
			x = biseccao(x, itB)

			""" Calcula fx para os valores obtidos """
			f=[fx(x[0]), fx(x[1])]

			""" Calcula pelo método das secantes. """
			secante(x, f, itSMax+1, eps, plotRange, funcaoMascara)	

			print(" ------------------------------------------ \n\n")

			""" Desliga modo iterativo para manter o gráfico gerado na tela, caso contrário ele desaparece muito rápido """
			plt.ioff() # Desliga modo iterativo
			plt.show() # Mostra o que foi plotado até agora, ou seja, tudo

		else:
			print("Existem mais de uma ou nenhuma raiz no intervalo dado")

	except TypeError:
		print("ERRO #06: TypeError")

	except ZeroDivisionError:
		print("ERRO #07: ZeroDivisionError")

# janela de dados, repara que ela executa a main e depois
# a main para ela com o entradas.destroy()
entradas = tk.Tk()

entradas.title('Entradas')

tk.Label(entradas, text = "Inicio do intervalo").grid(row = 0, column = 0)
entradaA = tk.Entry(entradas)
entradaA.grid(row = 1, column = 0)

tk.Label(entradas, text = "Fim do intervalo").grid(row = 0, column = 1)
entradaB = tk.Entry(entradas)
entradaB.grid(row = 1, column = 1)

tk.Label(entradas, text = "Inicio do intervalo").grid

tk.Label(entradas, text = "\nMetodo das Secantes").grid(row = 2, columnspan= 2)

tk.Label(entradas, text = "Precisao").grid(row = 3, column = 0)
entradaEpslon = tk.Entry(entradas)
entradaEpslon.grid(row = 4, column = 0)

tk.Label(entradas, text = "Maxixmo de\niteracoes").grid(row = 3, column = 1)
entradaMaxIt = tk.Entry(entradas)
entradaMaxIt.grid(row = 4, column = 1)

#espaçamento
tk.Label(entradas, text = "").grid(row = 5, column = 0)

tk.Label(entradas, text = "Area de plotagem").grid(row = 6, column = 0)
entradaPlotArea = tk.Entry(entradas)
entradaPlotArea.grid(row = 6, column = 1)

#espaçamento
tk.Label(entradas, text = "").grid(row = 7, column = 0)

my_button0 = tk.Button(entradas, text = "Enviar", command = main)
my_button0.grid(row = 8, columnspan = 2)

entradas.mainloop()
