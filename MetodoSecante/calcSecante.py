def function(x):
	return x**2

def secant():
	x=[0.5, 1.0]
	f=[0.625, -3]
	for i in range(2,8):
		xValue = x[i-1]-((f[i-1]*(x[i-1]-x[i-2]))/(f[i-1]-f[i-2]))
		x.append(xValue)
		fValue = function(xValue)
		f.append(fValue)
	
	for i in range(0,8):
		print("x = {}| f = {}".format(x[i],f[i]))

def main():
	secant()

if __name__ == "__main__":
    main()
