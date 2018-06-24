import matplotlib.pyplot as plt

def secant(x, f, it, TAM):	
	xAxis = []
	yAxis = []
	for i in range(int(round(x[0]))-TAM, int(round(x[0]))+TAM):
		xAxis.append(i)
		yAxis.append(fx(i))
	plt.plot(xAxis, yAxis, )

	for i in range(2,it):
		if f[i-1]-f[i-2] == 0:
			break
		else:
			if x[i-1]-x[i-2] == 0:
				break

			else:
				xValue = x[i-1]-((f[i-1]*(x[i-1]-x[i-2]))/(f[i-1]-f[i-2]))
			x.append(xValue)
			fValue = fx(xValue)
			f.append(fValue)
	
	for i in range (1, len(f)):
		fSec(i, x[i-1], x[i], f[i-1], f[i], TAM)
	
	plt.grid(True)
	funcao = "x^2"
	plt.title("{}, raiz = ".format(funcao) + str(x[len(x)-1]))
	plt.ylabel("f(x)")
	plt.xlabel("x")
	plt.legend()
	plt.show()

def main():
	# Pré valores passados pelo usuario
	x=[0.5, 1.0]		# x0, x1
	f=[0.625, -3.0]		# f0, f1
	it = 7				#numero de iteracoes
	TAM = 100			#Tamanho para plotar o gráfico, é necessario encontrar um valor melhor

	# Chama função secant() para calcular e plotar o gráfico #
	secant(x, f, it+1, TAM)

def fSec(i, x0, x1, f0, f1, TAM):
	m = (f1-f0)/(x1-x0)
	#y = m(x-x0)+y0
	xAxis = [x1]
	yAxis = [f1]
	for x in range(int(round(x1))-TAM, int(round(x1))+TAM):
		y = m*(x-xAxis[0])+yAxis[0]
		xAxis.append(x)
		yAxis.append(y)
	lbl = str(i)+" iteração"
	plt.plot(xAxis, yAxis, label = lbl)

def fx(x):
	return x**2

if __name__ == "__main__":
    main()
