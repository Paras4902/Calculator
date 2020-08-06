from tkinter import Tk, END, Entry, Button, mainloop, messagebox as msgbx
import math


class Calc:

    def sqrt(self):
        expression = self.var.get()
        replacedtxt5 = expression.replace(self.newdiv, '/')
        replacedtxt = replacedtxt5.replace('x', '*')

        try:
            nval = int(eval(replacedtxt))

        except SyntaxError or NameError:
            self.var.delete(0, END)
            msgbx.showerror("Error", "Invalid input")

        else:
            sqval = math.sqrt(nval)
            self.var.delete(0, END)
            self.var.insert(0, sqval)

    def sq(self):
        expression = self.var.get()
        replacedtxt2 = expression.replace(self.newdiv, '/')
        replacedtxt = replacedtxt2.replace('x', '*')

        try:
            newval = int(eval(replacedtxt))

        except SyntaxError or NameError:
            self.var.delete(0, END)
            msgbx.showerror("Error", "Invalid input")

        else:
            sqval = math.pow(newval, 2)
            self.var.delete(0, END)
            self.var.insert(0, sqval)

    def clear(self):
        newtxt1 = self.var.get()
        newtxt = newtxt1[0:-1]
        self.var.delete(0, END)
        self.var.insert(0, newtxt)

    def equal(self):
        expression = self.var.get()
        replacedtxt = expression.replace(self.newdiv, '/')
        replacedtxt1 = replacedtxt.replace('x', '*')

        try:
            solved = str(eval(replacedtxt1))

        except SyntaxError or NameError:
            self.var.delete(0, END)
            msgbx.showerror("Error", "Invalid input")

        except ZeroDivisionError:
            self.var.delete(0, END)
            msgbx.showerror("ZeroDivisionError", "Cannot divide by zero")

        else:
            self.var.delete(0, END)
            self.var.insert(0, solved)

    def clearall(self):
        self.var.delete(0, END)

    def action(self, arg):
        self.var.insert(END, arg)

    def __init__(self, root):
        self.font = "times", 35, "bold"
        self.var = Entry(root, font=self.font, bd=10, bg="black", fg="white")
        self.var.place(x=10, y=10, height=90, width=530)
        self.var.focus_get()
        self.div = '÷'
        self.ndiv = self.div.encode('utf-8', self.div)
        self.newdiv = self.ndiv.decode('utf-8')
        root.geometry("550x650")
        root.resizable(0, 0)
        root.title("Calculator by Paras4902")
        root.config(bg="black")
        Button(root, text=self.newdiv, font=self.font, bd=10, bg="black", fg="white", command=lambda: self.action(self.newdiv)).place(x=450, y=110, height=95, width=95)
        Button(root, text="9", font=self.font, bd=10, bg="black", fg="white", command=lambda: self.action('9')).place(x=10, y=110, height=100, width=100)
        Button(root, text="8", font=self.font, bd=10, bg="black", fg="white", command=lambda: self.action('8')).place(x=120, y=110, height=100, width=100)
        Button(root, text="7", font=self.font, bd=10, bg="black", fg="white", command=lambda: self.action('7')).place(x=230, y=110, height=100, width=100)
        Button(root, text="6", font=self.font, bd=10, bg="black", fg="white", command=lambda: self.action('6')).place(x=10, y=220, height=100, width=100)
        Button(root, text="5", font=self.font, bd=10, bg="black", fg="white", command=lambda: self.action('5')).place(x=120, y=220, height=100, width=100)
        Button(root, text="4", font=self.font, bd=10, bg="black", fg="white", command=lambda: self.action('4')).place(x=230, y=220, height=100, width=100)
        Button(root, text="2", font=self.font, bd=10, bg="black", fg="white", command=lambda: self.action('2')).place(x=120, y=330, height=100, width=100)
        Button(root, text="1", font=self.font, bd=10, bg="black", fg="white", command=lambda: self.action('1')).place(x=230, y=330, height=100, width=100)
        Button(root, text="3", font=self.font, bd=10, bg="black", fg="white", command=lambda: self.action('3')).place(x=10, y=330, height=100, width=100)
        Button(root, text=".", font=self.font, bd=10, bg="black", fg="white", command=lambda: self.action('.')).place(x=120, y=440, height=100, width=100)
        Button(root, text="0", font=self.font, bd=10, bg="black", fg="white", command=lambda: self.action('0')).place(x=10, y=440, height=100, width=100)
        Button(root, text="-", font=self.font, bd=10, bg="black", fg="white", command=lambda: self.action('-')).place(x=340, y=220, height=100, width=100)
        Button(root, text="*", font=self.font, bd=10, bg="black", fg="white", command=lambda: self.action('x')).place(x=340, y=330, height=100, width=100)
        Button(root, text="+", font=self.font, bd=10, bg="black", fg="white", command=lambda: self.action('+')).place(x=340, y=110, height=100, width=100)
        Button(root, text=")", font=self.font, bd=10, bg="black", fg="white", command=lambda: self.action(')')).place(x=450, y=440, height=95, width=95)
        Button(root, text="(", font=self.font, bd=10, bg="black", fg="white", command=lambda: self.action('(')).place(x=340, y=440, height=100, width=100)
        Button(root, text="AC", font=self.font, bd=10, bg="black", fg="white", command=lambda: self.clearall()).place(x=450, y=550, height=90, width=95)
        Button(root, text="=", font=self.font, bd=10, bg="black", fg="white", command=lambda: self.equal()).place(x=10, y=550, height=90, width=430)
        Button(root, text="sq", font=self.font, bd=10, bg="black", fg="white", command=lambda: self.sq()).place(x=450, y=220, height=95, width=95)
        Button(root, text="C", font=self.font, bd=10, bg="black", fg="white", command=lambda: self.clear()).place(x=230, y=440, height=100, width=100)
        Button(root, text="√", font=self.font, bd=10, bg="black", fg="white", command=lambda: self.sqrt()).place(x=450, y=330, height=95, width=95)


if __name__ == '__main__':
    rooted = Tk()
    newcal = Calc(rooted)

    mainloop()
