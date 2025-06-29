def calculadora():
    try:
        a = int(input("Ingrese un numero a:"))
        b = int(input("Ingrese un numero b:"))
        operacion = input("Ingrese la operacion a realizar(+, -, *, /):")
        
        if operacion == "+":
            print(f"Resultado de la suma: {a + b}")
        elif operacion == "-":
            print(f"Resultado de la resta: {a - b}")
        elif operacion == "*":
            print(f"Resultado del producto: {a * b}")
        elif operacion == "/":
            try:
                print(f"Resultado de la division: {a / b}")
            except ZeroDivisionError:
                print("No es posible division entre cero") #Error de división por cero
        else:
            print("Syntax error: Operación no válida")
            
    except ValueError:
        print("Error: Debes ingresar números enteros válidos") #Solo se permiten números enteros 
    except Exception as e:
        print(f"Ocurrió un error inesperado: {str(e)}") #Esta línea captura cualquier otro error inesperado

calculadora()