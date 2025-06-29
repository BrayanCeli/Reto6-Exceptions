def elementos_con_mismos_caracteres(lista_palabras):
    try:
     
        if not isinstance(lista_palabras, list):
            raise TypeError("El argumento debe ser una lista")# Validar que el argumento sea una lista
        
        
        if not lista_palabras:
            print("Advertencia: La lista está vacía")# Validar que la lista no esté vacía
            return []
        
        
        if not all(isinstance(palabra, str) for palabra in lista_palabras):
            raise ValueError("Todos los elementos deben ser cadenas de texto")# Validar que todos los elementos sean strings
        
        grupos = {}
        
        for palabra in lista_palabras:
            try:
                palabra = palabra.lower()# Convertir a minúsculas para evitar distinción entre mayúsculas y minúsculas
                clave = ''.join(sorted(palabra))
                if clave not in grupos:
                    grupos[clave] = []
                grupos[clave].append(palabra)
            except TypeError as e:
                print(f"Advertencia: '{palabra}' no es ordenable - {str(e)}")
                continue
        
        resultado = []
        for grupo in grupos.values():
            if len(grupo) >= 2:
                resultado.extend(grupo)
        
        return resultado
    
    except TypeError as te:
        print(f"Error de tipo: {te}")
        return []
    except ValueError as ve:
        print(f"Error de valor: {ve}")
        return []
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        return []