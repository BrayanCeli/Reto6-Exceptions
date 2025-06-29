def lista_de_primos(limite=100):
    try:
        
        if not isinstance(limite, int) or limite < 1:
            raise ValueError("El límite debe ser un entero positivo mayor que 0")#Validar que el límite sea un número positivo
        
        primos = []
        
        for i in range(2, limite + 1):  #Empezamos desde 2 (1 no es primo)
            es_primo = True
            
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    es_primo = False
                    break
            
            if es_primo:
                primos.append(i)
        
        return primos
    
    except ValueError as ve:
        print(f"Error de valor: {ve}")#Captura errores si el límite no es un entero positivo
        return []
    except TypeError:
        print("Error: El límite debe ser un número entero")#Captura errores si se tipifica un tipo de incorrecto de dato
        return []
    except Exception as e:
        print(f"Error inesperado: {str(e)}")#Errores genericos no esperados
        return []