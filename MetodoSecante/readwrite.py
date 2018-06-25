import os
func = input('Escreva a funcao: ')
X0 = input('X0: ')
X1 = input('X1: ')
it = input('Iteracoes: ')
arquivo = open('secante.py', 'w')
arquivo.write("""import matplotlib.pyplot as plt\n\ndef secant(x, f, it, TAM):\t\n\txAxis = []\n\tyAxis = []\n\traiz = 0\n\tfor i in range(int(round(x[0]))-TAM, int(round(x[0]))+TAM):\n\t\tyValue = fx(i)\n\t\tif yValue!="?":\n\t\t\txAxis.append(i)\n\t\t\tyAxis.append(yValue)\n\n\tfuncao = " """+func+""" "\n\tplt.plot(xAxis, yAxis, label=funcao)\n\n\ttry:\n\t\tfor i in range(2,it):\n\t\t\txValue = x[i-1]-((f[i-1]*(x[i-1]-x[i-2]))/(f[i-1]-f[i-2]))\n\t\t\tx.append(xValue)\n\t\t\tfValue = fx(xValue)\n\t\t\tf.append(fValue)\n\n\t\tfor i in range (1, len(f)):\n\t\t\tfSec(i, x[i-1], x[i], f[i-1], f[i], TAM)\n\t\t\n\texcept ZeroDivisionError:\n\t\tprint("ERRO #01: Divisao por zero")\n\texcept TypeError:\n\t\tprint("ERRO #02: TypeError")\n\t\traiz = "?"\n\n\tif raiz!="?":\n\t\traiz = str(x[len(x)-1])\n\n\tplt.title("{}, raiz = ".format(funcao) + raiz)\n\tplt.ylabel("f(x)")\n\tplt.xlabel("x")\n\tplt.legend()\n\tplt.grid(True)\n\tplt.show()\n\ndef fSec(i, x0, x1, f0, f1, TAM):\n\ttry:\n\t\tm = (f1-f0)/(x1-x0)\n\t\txAxis = [x1]\n\t\tyAxis = [f1]\n\t\tfor x in range(int(round(x1))-TAM, int(round(x1))+TAM):\n\t\t\ty = m*(x-xAxis[0])+yAxis[0]\n\t\t\txAxis.append(x)\n\t\t\tyAxis.append(y)\n\t\tlbl = str(i)+" iteração"\n\t\tplt.plot(xAxis, yAxis,"--", label = lbl)\n\n\texcept ZeroDivisionError:\n\t\tprint("ERRO #03: Divisao por zero")\n\ndef fx(x):\n\ttry:\n\t\treturn """+func+"""\n\texcept ZeroDivisionError:\n\t\tprint("ERRO #04: Divisao por zero")\n\t\treturn "?"\n\ndef main():\n\tx=["""+X0+""", """+X1+"""]\n\tf=[fx(x[0]), fx(x[1])]\n\tit = """+it+"""\n\tTAM = 1000\n\tsecant(x, f, it+1, TAM)\n\n\nif __name__ == "__main__":\n    main()\n""")
arquivo.close()
cwd = os.path.join(os.getcwd(), "secante.py")
os.system('{} {}'.format('python', cwd))
