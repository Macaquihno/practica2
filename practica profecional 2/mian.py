import cargar_codigo
import ordenar

def main():

    valor_usuario = int(input("Ingrese el código: "))

    while valor_usuario != 0:   
        if valor_usuario == 1:
            cargar_codigo.codigos()
        elif valor_usuario == 2:
            print("Adios")
        elif valor_usuario == 0:
            print("Adios")
           


main()
print("Adios")
              