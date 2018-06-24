import matplotlib.pyplot as plt
cordx = []
cordy = []
for x in range(-100, 100):
	y = 3*x**2
	cordx.append(x)
	cordy.append(y)
	print(y)
plt.plot(cordx,cordy)
plt.show()