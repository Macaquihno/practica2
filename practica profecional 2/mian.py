import cargar_codigo
import ordenar

def main():

    codigos = []

    valor_usuario = int(input("Ingrese el código: "))

    while valor_usuario != 0:

        if valor_usuario == 1:
            cargar_codigo.codigos(codigos)

        elif valor_usuario == 2:
            ordenar.mostrar_codigos_ordenados(codigos)

        valor_usuario = int(input("Ingrese el código: "))

    print("Adios")


main()
              