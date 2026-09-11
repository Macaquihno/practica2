import cargar_codigo
import ordenar

def main():
    codigos = []
    print("Que accion desea realizar?\n1. Cargar codigo\n2. Mostrar codigos ordenados\n0. Salir")
    valor_usuario = int(input(""))

    while valor_usuario != 0:
        if valor_usuario == 1:
            cargar_codigo.codigos(codigos)
            print(codigos)
            
            print("Que accion desea realizar?\n1. Cargar codigo\n2. Mostrar codigos ordenados\n0. Salir")
            valor_usuario = int(input(""))
            
                

        elif valor_usuario == 2:
            ordenar.mostrar_codigos_ordenados(codigos)

        

    print("Adios")


main()
              