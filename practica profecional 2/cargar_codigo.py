
def codigos():
    cadena_ingreso = str(input("Ingrese el código: "))
    longitud = len(cadena_ingreso)
    if cadena_ingreso == "" or longitud<4:
        print("El código ingresado es inválido.")
    else:
        print("El código ingresado es válido.")
        return cadena_ingreso