import os
func = input('Enter the function: ')
arquivo = open('secante.py', 'w')
arquivo.write('for x in range(-100, 100):\n\ty = ' + func + '\n\tprint(y)')
arquivo.close()
cwd = os.path.join(os.getcwd(), "secante.py")
os.system('{} {}'.format('python', cwd))
