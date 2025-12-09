archivo_name="archivo_pedidos.txt"
def pedir_cafe():
    print("Elige un cafe")
    print("\n 1. Late")
    print("\n 2. Americano")

    opcion = input("opcion")

    cafes = {
        "1":"Late",
        "2":"Americano" 
            }
    
    if opcion in cafes:
        cafe_elegido=cafes[opcion]
        print("Escogiste un " + cafe_elegido +" Preparando tu café ")
        with open (archivo_name,"a",encoding="utf-8") as archivo:
            archivo.write(cafe_elegido+"\n")
    else:
        print("Opcion incorrecta ")