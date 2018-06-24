def secant(x, f, it):
	for i in range(2,it):
		xValue = x[i-1]-((f[i-1]*(x[i-1]-x[i-2]))/(f[i-1]-f[i-2]))
		x.append(xValue)
		fValue = function(xValue)
		f.append(fValue)
	
	for i in range(0,it):
		print("{} - x = {}| f = {}".format(i, x[i],f[i]))

def main():
	x=[0.5, 1.0]
	f=[0.625, -3.0]
	it = 8
	secant(x, f, it)

def function(x):
	return (x**3)-(9*x)+5

if __name__ == "__main__":
    main()
