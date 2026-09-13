import cargar_codigo
import ordenar
import buscar


def main():
    codigos = []
    valor_usuario = 9

    while valor_usuario != 0:
        print("Que accion desea realizar?\n"
              "1. Cargar codigo\n"
              "2. Mostrar codigos ordenados\n"
              "3. Buscar codigo\n"
              "0. Salir")

        valor_usuario = int(input(""))

        if valor_usuario == 1:
            cargar_codigo.codigos(codigos)
            print(codigos)
            valor_usuario = 9

        elif valor_usuario == 2:
            ordenar.mostrar_codigos_ordenados(codigos)
            valor_usuario = 9

        elif valor_usuario == 3:
            buscar.buscar_codigo(codigos)
            valor_usuario = 9

    print("Adios")


main()