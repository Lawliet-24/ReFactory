import sympy 
import os
import time
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

Historial = InMemoryHistory()
x ,y ,z = sympy.Symbol('x'), sympy.Symbol('y'), sympy.Symbol('z')

Transformaciones = standard_transformations + (implicit_multiplication_application,)

while True:
    os.system("clear")
    print("======================================================")
    print("················BIENVENIDO A REFACTORY················")
    print("(Programa de factorización de expresiones algebraicas)")
    print("======================================================")
    print("Ingrese la expresión algebraica que desea factorizar: ")
    print("↓--------↓--------↓")
    print(" ")
    
    try:
        time.sleep(0.2)
        Expression = prompt("Ingrese la expresión: ", history=Historial)
        
        Expression = Expression.replace('^', '**')
        Expression = parse_expr(Expression, transformations=Transformaciones)
        
        if Expression.has(x, y, z):
            pass

        else:
            for i in range(5, 0, -1):
                os.system("clear")
                print("La expresión debe contener al menos una variable (x, y o z).")
                print(' ')
                print(f'Volviendo al menú en ({i}) segundos...')
                time.sleep(1)
            continue
        
    except:
        os.system("clear")
        print("==================================================")
        print("[Error]: La expresión ingresada no es válida.")
        print('Recuerde que usas los simbolos:')
        print('|* para multiplicar, + para sumar, - para restar, / para dividir y ** para elevar a una potencia.|')
        print('===================================================')
        print(' ')
        input("Presione Enter para continuar...")
        continue
    else:
        print('==================================================')
        print('Su resultado es:')
        Result = sympy.factor(Expression)
        
        Result = str(Result).replace('**', '^')
        Result = Result.replace('*', '')
        
        print(f'_______________({Result})__________________')
        print('==================================================')
        input("Presione Enter para continuar...")