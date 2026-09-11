import cargar_codigo
import ordenar

def main():
    codigos = []
    valor_usuario = 9

    while valor_usuario != 0:
        print("Que accion desea realizar?\n1. Cargar codigo\n2. Mostrar codigos ordenados\n0. Salir")
        valor_usuario = int(input(""))
        if valor_usuario == 1:
            cargar_codigo.codigos(codigos)
            print(codigos)
            valor_usuario = 9       
                            
        elif valor_usuario == 2:
            ordenar.mostrar_codigos_ordenados(codigos)
            valor_usuario = 9

        

    print("Adios")


main()
              