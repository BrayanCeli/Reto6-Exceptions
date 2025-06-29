def palabra_palindroma():
    try:
        palabra = input("Escriba una palabra: ").strip().lower()
        
        if not palabra:
            raise ValueError("No se ingresó ninguna palabra") # Verificar que se ingresó algo
        
        if not palabra.isalpha():
            raise ValueError("Solo se permiten letras (sin espacios ni números)")# Verificar que solo contiene letras (opcional, según requisitos)
        
        es_palindroma = True
        for i in range(len(palabra) // 2):
            if palabra[i] != palabra[-(i + 1)]:
                es_palindroma = False
                break
        
        if es_palindroma:
            print(f"'{palabra}' es palíndroma")
        else:
            print(f"'{palabra}' no es palíndroma")
            
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {str(e)}")#Captura cualquier otro error inesperado

palabra_palindroma()