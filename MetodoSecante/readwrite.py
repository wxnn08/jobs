import os
func = input('Escreva a funcao: ')
X0 = input('X0: ')
X1 = input('X1: ')
IT = input('Iteracoes: ')
TAM = input('Tamanho: ')
arquivo = open('secante.py', 'w')
arquivo.write("""import matplotlib.pyplot as plt\n\ndef secant(x, f, it, TAM):\t\n\txAxis = []\n\tyAxis = []\n\tfor i in range(int(round(x[0]))-TAM, int(round(x[0]))+TAM):\n\t\txAxis.append(i)\n\t\tyAxis.append(fx(i))\n\tplt.plot(xAxis, yAxis, label = "f")\n\t\n\tfor i in range(2,it):\n\t\tif f[i-1]-f[i-2] == 0: \n\t\t\tbreak\n\t\telse:\n\t\t\tif x[i-1]-x[i-2] == 0:\n\t\t\t\tbreak\n\t\t\telse:\n\t\t\t\txValue = x[i-1]-((f[i-1]*(x[i-1]-x[i-2]))/(f[i-1]-f[i-2]))\n\t\t\tx.append(xValue)\n\t\t\tfValue = fx(xValue)\n\t\t\tf.append(fValue)\n\t\n\tfor i in range (1, len(f)):\n\t\tfSec(i, x[i-1], x[i], f[i-1], f[i], TAM)\n\t\n\tplt.grid(True)\n\tfuncao = " """ + func + """ " \n\tplt.title("{}, raiz = ".format(funcao) + str(x[len(x)-1]))\n\tplt.ylabel("f(x)")\n\tplt.xlabel("x")\n\tplt.legend()\n\tplt.show()\n\ndef fSec(i, x0, x1, f0, f1, TAM):\n\tm = (f1-f0)/(x1-x0)\n\txAxis = [x1]\n\tyAxis = [f1]\n\tfor x in range(int(round(x1))-TAM, int(round(x1))+TAM):\n\t\ty = m*(x-xAxis[0])+yAxis[0]\n\t\txAxis.append(x)\n\t\tyAxis.append(y)\n\tlbl = str(i)+" iteração"\n\tplt.plot(xAxis, yAxis, label = lbl)\n\ndef fx(x):\n\treturn """+func+""" \n\ndef main():\n\tx=["""+X0+""", """+X1+"""]\n\tf=[fx("""+X0+"""), fx("""+X1+""")]\n\tit = """+IT+"""\n\tTAM = """+TAM+"""\n\tsecant(x, f, it+1, TAM)\n\nif __name__ == "__main__":\n    main()\n""")
 
arquivo.close()
cwd = os.path.join(os.getcwd(), "secante.py")
os.system('{} {}'.format('python', cwd))
