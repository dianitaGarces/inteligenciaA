from menu import mostrar_menu
from pedidos import pedir_cafe
from historial import ver_historial

def main():

    while True:
        mostrar_menu()
        opcion = input("seleccione una opcion")

        if opcion =="1":
            pedir_cafe()
        elif opcion =="2":
            ver_historial()
        elif opcion =="3":
            print("Fin programa")
            break
        else:
            print("Opción invalida")

#asi se asegura que esto es lo que se correo asi se se tenga muchos archivos
if __name__ == "__main__":
    main()