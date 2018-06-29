# Calculator made using pythons tkinter module
# Author - Mohamed Akil

from tkinter import *
import math
import os

class Application(Frame):
    """ Main class for calculator"""

    def __init__(self, master):
        """ Initialise the Frame. """
        super(Application, self).__init__(master)
        self.real_task = ""
        self.task = ""
        self.UserIn = StringVar()
        self.Real = StringVar()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create all the buttons for calculator. """
        # User input stored as an Entry widget.

        self.user_input = Entry(self, bg = "#A9A9A9", bd = 0, 
        insertwidth = 4, width = 17,
        font = ("TkTextFont", 40), textvariable = self.UserIn, justify = RIGHT)
        self.user_input.grid(columnspan = 5)

        self.user_input.insert(0, "0")

        # Button for value 7
        self.button1 = Button(self, bg = "#A9A9A9", bd = 0,
        text = "7", padx = 33, pady = 25, font = ("Helvetica", 20, "bold"), 
        command = lambda : self.buttonClick(7, "7"))
        self.button1.grid(row = 3, column = 0, sticky = W)

        # Button for value 8
        self.button2 = Button(self, bg = "#A9A9A9", bd = 0, 
        text = "8",  padx = 35, pady = 25, 
        command = lambda : self.buttonClick(8, "8"), font = ("Helvetica", 20, "bold"))
        self.button2.grid(row = 3, column = 1, sticky = W)

        # Button for value 9
        self.button3 = Button(self, bg = "#A9A9A9", bd = 0, 
        text = "9",  padx = 33, pady = 25,
        command = lambda : self.buttonClick(9, "9"), font = ("Helvetica", 20, "bold"))
        self.button3.grid(row = 3, column = 2, sticky = W)

        # Button for value 4
        self.button4 = Button(self, bg = "#A9A9A9", bd = 0,
        text = "4",  padx = 33, pady = 25,
        command = lambda : self.buttonClick(4, "4"), font = ("Helvetica", 20, "bold"))
        self.button4.grid(row = 4, column = 0, sticky = W)

        # Button for value 5
        self.button5 = Button(self, bg = "#A9A9A9", bd = 0, 
        text = "5",  padx = 35, pady = 25,
        command = lambda : self.buttonClick(5, "5"), font = ("Helvetica", 20, "bold"))
        self.button5.grid(row = 4, column = 1, sticky = W)

        # Button for value 6
        self.button6 = Button(self, bg = "#A9A9A9", bd = 0, 
        text = "6",  padx = 33, pady = 25,
        command = lambda : self.buttonClick(6, "6"), font = ("Helvetica", 20, "bold"))
        self.button6.grid(row = 4, column = 2, sticky = W)

        # Button for value 1
        self.button7 = Button(self, bg = "#A9A9A9", bd = 0, 
        text = "1",  padx = 33, pady = 25, 
        command = lambda : self.buttonClick(1, "1"), font = ("Helvetica", 20, "bold"))
        self.button7.grid(row = 5, column = 0, sticky = W)

        # Button for value 2
        self.button8 = Button(self, bg = "#A9A9A9", bd = 0, 
        text = "2",  padx = 35, pady = 25,
        command = lambda : self.buttonClick(2, "2"), font = ("Helvetica", 20, "bold"))
        self.button8.grid(row = 5, column = 1, sticky = W)

        # Button for value 3
        self.button9 = Button(self, bg = "#A9A9A9", bd = 0, 
        text = "3",  padx = 33, pady = 25,
        command = lambda : self.buttonClick(3, "3"), font = ("Helvetica", 20, "bold"))
        self.button9.grid(row = 5, column = 2, sticky = W)

        # Button for value 0
        self.button9 = Button(self, bg = "#A9A9A9", bd = 0, 
        text = "0",  padx = 33, pady = 25,
        command = lambda : self.buttonClick(0, "0"), font = ("Helvetica", 20, "bold"))
        self.button9.grid(row = 6, column = 0, sticky = W)

        # Operator buttons
        # Addition button
        self.Addbutton = Button(self, bg = "#A9A9A9", bd = 0, 
        text = "+",  padx = 36, pady = 25,
        command = lambda : self.buttonClick("+", "+"), font = ("Helvetica", 20, "bold"))
        self.Addbutton.grid(row = 3, column = 3, sticky = W)

        # Subtraction button
        self.Subbutton = Button(self, bg = "#A9A9A9", bd = 0, 
        text = "-",  padx = 39, pady = 25,
        command = lambda : self.buttonClick("-", "-"), font = ("Helvetica", 20, "bold"))
        self.Subbutton.grid(row = 4, column = 3, sticky = W)

        # Multiplication button
        self.Multbutton = Button(self, bg = "#A9A9A9", bd = 0, 
        text = "*",  padx = 38, pady = 25,
        command = lambda : self.buttonClick("*", "*"), font = ("Helvetica", 20, "bold"))
        self.Multbutton.grid(row = 5, column = 3, sticky = W)

        # Division button
        self.Divbutton = Button(self, bg = "#A9A9A9", bd = 0, 
        text = "/",  padx = 39, pady = 25,
        command = lambda : self.buttonClick("/", "/"), font = ("Helvetica", 20, "bold"))
        self.Divbutton.grid(row = 6, column = 3, sticky = W)

        # Tan button
        self.Tanbutton = Button(self, bg = "#A9A9A9", bd = 0, 
        text = "Tan",  padx = 23, pady = 22,
        command = lambda : self.buttonClick("math.tan(", "Tan("), font = ("Helvetica", 15, "bold"))
        self.Tanbutton.grid(row = 2, column = 0, sticky = W)

        # Cos button
        self.Cosbutton = Button(self, bg = "#A9A9A9", bd = 0, 
        text = "Cos",  padx = 24, pady = 22,
        command = lambda : self.buttonClick("math.cos(", "Cos("), font = ("Helvetica", 15, "bold"))
        self.Cosbutton.grid(row = 2, column = 1, sticky = W)


        # Seno button
        self.Senobutton = Button(self, bg = "#A9A9A9", bd = 0, 
        text = "Sen",  padx = 23, pady = 22,
        command = lambda : self.buttonClick("math.sin(", "Sen("), font = ("Helvetica", 15, "bold"))
        self.Senobutton.grid(row = 2, column = 2, sticky = W)

        # Pi button
        self.Pibutton = Button(self, bg = "#A9A9A9", bd = 0, 
        text = "\u03C0",  padx = 34, pady = 24,
        command = lambda : self.buttonClick("math.acos(-1)", "\u03C0"), font = ("Sans-serif", 15, "bold"))
        self.Pibutton.grid(row = 2, column = 3, sticky = W)

        # OpenPar button
        self.OpenParbutton = Button(self, bg = "#A9A9A9", bd = 0, 
        text = "(",  padx = 40, pady = 25,
        command = lambda : self.buttonClick("(", "("), font = ("Helvetica", 20, "bold"))
        self.OpenParbutton.grid(row = 3, column = 4, sticky = W)

        # ClosePar button
        self.CloseParbutton = Button(self, bg = "#A9A9A9", bd = 0, 
        text = ")",  padx = 40, pady = 25,
        command = lambda : self.buttonClick(")", ")"), font = ("Helvetica", 20, "bold"))
        self.CloseParbutton.grid(row = 4, column = 4, sticky = W)

        # X button
        self.Xbutton = Button(self, bg = "#A9A9A9", bd = 0, 
        text = "x",  padx = 37, pady = 25,
        command = lambda : self.buttonClick("x", "x"), font = ("Helvetica", 20, "bold"))
        self.Xbutton.grid(row = 5, column = 4, sticky = W)


        # Sqrt button
        self.Sqrtbutton = Button(self, bg = "#A9A9A9", bd = 0, 
        text = "\u221A",  padx = 30, pady = 25,
        command = lambda : self.buttonClick("math.sqrt(", "\u221A("), font = ("Sans-serif", 20, "bold"))
        self.Sqrtbutton.grid(row = 6, column = 4, sticky = W)


        # Elevate button
        self.Elebutton = Button(self, bg = "#A9A9A9", bd = 0, 
        text = "^",  padx = 37, pady = 18,
        command = lambda : self.buttonClick("**", "^"), font = ("Helvetica", 20, "bold"))
        self.Elebutton.grid(row = 2, column = 4, sticky = W)


        # Plot button
        self.Equalbutton = Button(self, bg = "#BDB76B", bd = 0, 
        text = "Plot",  padx = 63, pady = 25,
        command = self.CalculateTask, font = ("Helvetica", 18, "bold"))
        self.Equalbutton.grid(row = 6, column = 1, sticky = W, columnspan = 2)

        # Clear Button
        self.Clearbutton = Button(self, bg = "#BDB76B", bd = 0,
        text = "AC", font = ("Helvetica", 19, "bold"), width = 31, padx = 8, command = self.ClearDisplay)
        self.Clearbutton.grid(row = 1, columnspan = 5, sticky = W)

    def buttonClick(self, number, symbol):

        self.real_task = self.real_task + str(number)          
        
        self.task = str(self.task) + str(symbol)
        self.UserIn.set(self.task)
        self.Real.set(self.real_task)

    def CalculateTask(self):
        self.data = self.Real.get()
        try:
            #print(self.data)
            arquivo = open('input.txt', 'w')
            arquivo2 = open('title.txt', 'w')
            arquivo.write(self.real_task)
            arquivo2.write(self.task)
            arquivo.close()
            arquivo2.close()

            # TO DO executar o calc com o os
            cwd = os.path.join(os.getcwd(), "calc.py")
            os.system('{} {}' .format('python', cwd))
            self.ClearDisplay()
            #self.answer = eval(self.data)
            #self.displayText(self.answer)
            #self.task = self.answer

        except SyntaxError as e:
            self.displayText("Invalid Syntax!")
            self.task = ""

    def displayText(self, value):
        self.user_input.delete(0, END)
        self.user_input.insert(0, value)

    def ClearDisplay(self):
        self.task = ""
        self.real_task = ""
        self.user_input.delete(0, END)
        self.user_input.insert(0, "0")


calculator = Tk()

calculator.title("Calculator")
app = Application(calculator)
# Make window fixed (cannot be resized)
calculator.resizable(width = False, height = False)

calculator.mainloop()
