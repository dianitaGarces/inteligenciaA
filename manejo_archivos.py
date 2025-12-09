#open 
# R lectura
# W write escritura
# x crear archivo

try:
    f = open ("archivo.txt","r")
    print (f.readline())
    f.close()
except FileNotFoundError:
    print("archivo no existe")
    open ("archivo.txt","x")

#abir y cerrar el archivo sin tener que hacerlo manualmente es con with

print("------------------- Leyendo de otra forma -------------------")
try:
    with open("archivo.txt","a", encoding="utf-8") as f:
        f.write("\n")
        f.write("Hola mundo, estamos escribiendo desde codigo")
    with open("archivo.txt","r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("archivo no existe, creando")
    