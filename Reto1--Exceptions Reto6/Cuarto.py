def mayor_suma_consecutiva(lista):
    try:
        if not isinstance(lista, list):
            raise TypeError("El argumento debe ser una lista")# Validar que el argumento sea una lista
        
        if len(lista) < 2:
            print("Advertencia: La lista debe contener al menos 2 elementos")# Validar que la lista tenga al menos 2 elementos
            return None
        
        if not all(isinstance(x, (int, float)) for x in lista):
            raise ValueError("Todos los elementos de la lista deben ser números")#Validar que todos los elementos de la lista sean números
        
        mayor_suma = lista[0] + lista[1]
        
        for i in range(len(lista) - 1):
            suma = lista[i] + lista[i + 1]
            if suma > mayor_suma:
                mayor_suma = suma
                
        return mayor_suma
    
    except TypeError as te:
        print(f"Error de tipo: {te}")
        return None
    except ValueError as ve:
        print(f"Error de valor: {ve}")
        return None
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        return None