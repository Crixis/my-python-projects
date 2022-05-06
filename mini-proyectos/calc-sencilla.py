"""
 hacer una calculadora: 
 tener dos campor de texto
 tener 4 botones para las operaciones
 mostrar el resultado por alerta
"""
from tkinter import *
from tkinter import messagebox
from turtle import left

ventana=Tk()
ventana.title("Calculadora en tkinter")
ventana.geometry("500x300")

def sumar():
    try:
        res.set(float(num1.get())+float(num2.get()))
        mostraresultado()
    except:
        messagebox.showerror("Error", "Introduce bien los datos!!")

def restar():
    try:
        res.set(float(num1.get())-float(num2.get()))
        mostraresultado()
    except:
        messagebox.showerror("Error", "Introduce bien los datos!!")

def multiplicar():
    try:
        res.set(float(num1.get())*float(num2.get()))
        mostraresultado()
    except:
        messagebox.showerror("Error", "Introduce bien los datos!!")

def dividir():
    try:
        res.set(float(num1.get())/float(num2.get()))
        mostraresultado()
    except:
        messagebox.showerror("Error", "Introduce bien los datos!!")

def mostraresultado():
    messagebox.showinfo("Resultado", f"el resultado de la operacion es: {res.get()}")
    num1.set("")
    num2.set("")

num1=StringVar()
num2=StringVar()
res= StringVar()

marco=Frame(ventana, width=280, height=170)
marco.config(bd=5, relief=SOLID, padx=15, pady=15)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Introdude un numero: ").pack()
Entry(marco, textvariable=num1, justify=CENTER).pack()

Label(marco, text="Introduce otro numero: ").pack()
Entry(marco, textvariable=num2, justify=CENTER).pack()

Label(marco, text=" ")

Button(marco, text="Sumar", command=sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=dividir).pack(side="left", fill=X, expand=YES)

ventana.mainloop()