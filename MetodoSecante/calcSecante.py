import matplotlib.pyplot as plt

def secant(x, f, it, TAM):	
	xAxis = []
	yAxis = []
	for i in range(int(round(x[0]))-TAM, int(round(x[0]))+TAM):
		xAxis.append(i)
		yAxis.append(fx(i))
	plt.plot(xAxis, yAxis, )

	try:
		for i in range(2,it):
			xValue = x[i-1]-((f[i-1]*(x[i-1]-x[i-2]))/(f[i-1]-f[i-2]))
			x.append(xValue)
			fValue = fx(xValue)
			f.append(fValue)

		for i in range (1, len(f)):
			fSec(i, x[i-1], x[i], f[i-1], f[i], TAM)
		
		
	except ZeroDivisionError:
		print("ERRO #01: Divisao por zero")
	except TypeError:
		print("TypeError")

	plt.grid(True)
	funcao = "x^2"
	plt.title("{}, raiz = ".format(funcao) + str(x[len(x)-1]))
	plt.ylabel("f(x)")
	plt.xlabel("x")
	plt.legend()
	plt.show()

def fSec(i, x0, x1, f0, f1, TAM):
	if x1-x0==0:
		return 
	m = (f1-f0)/(x1-x0)
	xAxis = [x1]
	yAxis = [f1]
	for x in range(int(round(x1))-TAM, int(round(x1))+TAM):
		y = m*(x-xAxis[0])+yAxis[0]
		xAxis.append(x)
		yAxis.append(y)
	lbl = str(i)+" iteração"
	plt.plot(xAxis, yAxis, label = lbl)

def fx(x):
	try:
		return -9*(x**2)-27*x+5
	except ZeroDivisionError:
		print("ERRO #01: Divisao por zero")

def main():
	x=[0, 1]
	f=[fx(x[0]), fx(x[1])]
	it = 7
	TAM = 100
	secant(x, f, it+1, TAM)


if __name__ == "__main__":
    main()
