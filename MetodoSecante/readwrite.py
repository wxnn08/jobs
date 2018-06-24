import os
func = input('Enter the function: ')
arquivo = open('secante.py', 'w')
arquivo.write('import matplotlib.pyplot as plt\ncordx = []\ncordy = []\nfor x in range(-100, 100):\n\ty = ' + func + '\n\tcordx.append(x)\n\tcordy.append(y)\n\tprint(y)\nplt.plot(cordx,cordy)\nplt.show()')
arquivo.close()
cwd = os.path.join(os.getcwd(), "secante.py")
os.system('{} {}'.format('python', cwd))
