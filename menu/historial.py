archivo_name="archivo_pedidos.txt"

def ver_historial():
    
    try:
        print("Historial de pedidos:\n")
        with open (archivo_name,"r",encoding="utf-8") as archivo:
                pedidos=archivo.readlines()
                if pedidos:
                     for i, pedidos in enumerate(pedidos):
                        print(str(i)+ "-"+pedidos.strip()+"\n")
                else:
                     print("no existen pedidos aun")
    except FileNotFoundError:
         print("no existe el archivo de historial de pedidos")

    