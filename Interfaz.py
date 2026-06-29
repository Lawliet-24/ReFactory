import tkinter as tk
from tkinter import messagebox
from prompt_toolkit import prompt
import sympy
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application



Ventana = tk.Tk()
Ventana.title('Refactory')
Ventana.geometry('500x300')

def Factorizar():
    Transformaciones = standard_transformations + (implicit_multiplication_application,)
    Expresion = Expression.get()
    Expresion = Expresion.replace('^', '**')
    
    try:
        Expresion = parse_expr(Expresion, transformations=Transformaciones)
        
        if Expresion.has(sympy.Symbol('x'), sympy.Symbol('y'), sympy.Symbol('z')):
            Resultado = sympy.factor(Expresion)
            Resultado = str(Resultado).replace('**', '^').replace('*', '')
            messagebox.showinfo("Resultado", f"El resultado es: {Resultado}")
        else:
            messagebox.showerror("Error", "La expresión debe contener al menos una variable (x, y o z).")
    
    except Exception as e:
        messagebox.showerror("Error", f"La expresión ingresada no es válida.\nDetalles: {str(e)}")

Expression = tk.StringVar()

Titulo = tk.Label(Ventana, 
  text="======================================================")
Titulo.pack(pady=10)

Subtitulo = tk.Label(Ventana, 
  text="················BIENVENIDO A REFACTORY················")
Subtitulo.pack(pady=10)

Descripcion = tk.Label(Ventana, 
  text="(Programa de factorización de expresiones algebraicas)")
Descripcion.pack(pady=10)

Instruccion = tk.Label(Ventana, 
  text="Ingrese la expresión algebraica que desea factorizar: ")

Instruccion.pack(pady=10)

Titulo2 = tk.Label(Ventana, 
  text='=======================================================')
Titulo2.pack(pady=10)

Entrada = tk.Entry(Ventana, width=30, 
    font=('Arial', 14),
    textvariable=Expression
).pack(pady=5) 

Boton = tk.Button(Ventana,
    text='Factorizar',
    font=('Arial', 14),
    background='lightgreen',
    foreground='black',
    command=Factorizar
).pack(pady=10)



Ventana.mainloop()