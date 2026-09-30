import cargar_codigo
import ordenar
import buscar
import longitud
import salir

def main():
    codigos = []
    valor_usuario = None
    try:
        while valor_usuario != 0:
            print("----------------------------------------------------")
            print("¿Que accion desea realizar?\n"
                "1. Cargar codigo\n"
                "2. Mostrar codigos ordenados\n"
                "3. Buscar codigo\n"
                "4. Analizar longitudes\n"
                "0. Salir")
            print("----------------------------------------------------")
            valor_usuario = int(input(""))

            if valor_usuario == 1:
                cargar_codigo.codigos(codigos)
                print(codigos)
                valor_usuario = None

            elif valor_usuario == 2:
                ordenar.mostrar_codigos_ordenados(codigos)
                valor_usuario = None

            elif valor_usuario == 3:
                buscar.buscar_codigo(codigos)
                valor_usuario = None

            elif  valor_usuario == 4:
                longitud.analizar_longitudes(codigos)
                valor_usuario = None

            elif valor_usuario == 0:
                salir.salir()  

            else:
                print("Opcion no valida")
                valor_usuario = None 

    except ValueError:
        print("----------------------------------------------------")
        print("Opcion no valida")   
        print("Cerrando el programa...")

main()