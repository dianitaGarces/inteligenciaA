# Asi se hacen los comentarios en este lenguaje
"""Estos son 
comentarios multilineas
"""
from asyncio import print_call_graph
import random


if 5> 3:
    print("si es mayor")

#variables multiples
a = b =c = "Frutas"
print (a)
x,y,z="Manzana", "Pera","Durazno"
print(x,y,z)

#variable numero imaginario 
imaginario=1j

# texto
comillas_simples='hola '
comillas_dobles="mundo "
comillas_triples= '''variable'''
print(comillas_simples+ comillas_dobles + comillas_triples)
#Listas

lista=[0,1,2,3,4]

#Tuplas, no pueden modificarse

tupla=["a","b","c"]

#diccionario colleccion clave valor
print("------ diccionario ------")
diccionario = {
    "nombre":"juan",
    "edad":30,
    "ciudad":"Bogota"
}
print(diccionario)
print (diccionario.get("nombre"))
print(diccionario.keys())
print(diccionario.values())
diccionario["edad"]=32
print(diccionario.values())

diccionario["profesion"]="Ingeniero"
print(diccionario.values())

diccionario.update({"edad":33,"sexo":"masculino"})#sirve para actualizar o agregar un valor
print(diccionario.values())
print ("---------------->imprimiendo diccionario con buckle ------------------->")
for key in diccionario:
    print(key)

print("Imprimiendo valores ")
for valor in diccionario.values():
    print(valor)

print("Imprimiendo clave y  valores ")
for k,v in diccionario.items():
    print(k,v)

diccionario.pop("sexo")#elimina item especifico segun llave
print("eliminando clave ",diccionario.values())

diccionario.popitem() #elimina el ultimo item
print("eliminando item", diccionario.values())

diccionario.clear()#vacia el diccionario
print("clear ", diccionario.values())


print("------ diccionario anidado ------")
diccionarioFamilia = {
    "hijo1":{ "nombre":"juan",
    "edad":30,
    "ciudad":"Bogota"
    },
     "hijo2":{ "nombre":"pedro",
    "edad":15,
    "ciudad":"Bogota"
    },
     "hijo3":{ "nombre":"laura",
    "edad":20,
    "ciudad":"Bogota"
    }
}

print("imprimiendo diccionario anidado ",diccionarioFamilia["hijo1"]["nombre"])



#conjuntos, se llama SET colecciòn desordenada con elementos mutables

print("------------------Conjuntos ------------------")
frutas={"Manza","Naranjas","Mandarinas","Naranjas"}
print("cojuntos")
print(frutas)
print("Manza" in frutas)
frutas.add("Pera")
print(frutas)

frutas_tropicales={"Pinna","Mango"}
frutas.update(frutas_tropicales) #sirve para añadir listas, conjuntos y tuplas
print("frutas anadida ",frutas)

frutas.remove("Mango")
print (frutas)

frutas.discard("Banana") #si el elemento no existe con este no sale error con remove si
print(frutas)

frutas.pop()#elimina elemento aleatorio ya que no tiene posicion
print(frutas)

frutas.clear()#vacia el conjunto
print(frutas)

print("--- operacion de conjuntos ------")
a = {"a","b","c"}
b ={"c","d","e"}
c = a.union(b)
print ("Union entre dos conjuntos ",c)
inter= a.intersection(b)
print("interecciond e conjunto solo elementos repetidos ",inter)

diferencia= a.difference(b)
print ("Diferencia de conjuntos ",diferencia)
conjunto = {1,1,2,2,3}
print ("conjuntos ignora los repetidos ")
print(conjunto)

#converitr numero
print(type(imaginario))

xf = float (2.8)
num_int = int(xf)
print (xf)
print (num_int)

# numeros random
print ("numero aleatorios del 1 al 10")
print (random.randrange(1,10))

# opciones de texto
texto = "Hola mundo Colombia"
print(len(texto))

estaIncluida= "Java" in texto
print(estaIncluida)

print(texto.upper())

print(texto.lower())

espacios = "    Hola mundo de espacios    "
espacios = espacios.split(" ")
print(espacios)

texto = "este es un texto"
print(texto[4:])
print(texto[0:3])
print(texto[:3])
print(texto.replace("este","esto"))
print(texto)

#booleanos

print(bool("Hola mundo"))
print(bool(["Hola mundo","dos"]))
print(bool(0))

#None la ausencia de valor
xNone= None
print (xNone)


#operador aritmetico
x=3
y=4
print("suma ",x+y)

#potencia
print("potencia ", x**y)

#division entera
print("potencia ", x//y)

#operador de asignacion abreviado
x = 5
x += 3
x -= 3
x //=3
x %=3
print (x)

#operador Walrus (Morza)

print(z := 3)
print ("Walrus",z)

#matcha para control de flujo
dia = 10
match dia:
    case 1:
        print("lunes")
    case 2:
        print("martes")
    case _:
        print("no es un dia")

# while 
print("While")
i=1 
while i <= 3:
    print(i)
    i +=1

# for
print("for")

palabra = "Python"
for letra in palabra:
    print(letra)

for i in range(0,10,2):
    if i == 4:
        pass
    print("rango ",i)

#listas
vehiculos =["Auto","Moto","Bus"]
vehiculos.append("Barco")#agrega un elementoo al final
print(vehiculos)

#insert en una posicion y mueve los otros
vehiculos.insert(1,"Bicicleta")
print(vehiculos)

#remove elimina
vehiculos.remove ("Moto")

print(vehiculos)

#pop elimina un elemento segun la posicion
vehiculos.pop(1)
print(vehiculos)

#ordenar sort
vehiculos.sort()
print(vehiculos)

#reverse ordenar al rever
vehiculos.reverse()
print(vehiculos)

vehiculos2= ["Camion","TM"]
vehiculos_final= vehiculos + vehiculos2

print(vehiculos_final)

#tuplas, no se pueden modificar
tecnologias = ("Java","Python","C++")
print(tecnologias)
print(type(tecnologias))

tecnologia = ("Java",) #asi se declar auna tupla de un elemento con la ,

tecnologias_diversa = ("Java","Python",3,True)
print (tecnologias_diversa)

tecnologias_total = tecnologias + tecnologias_diversa
print (tecnologias_total)#duplica valores no valida que sean diferentes como Java

# lambda
xx = lambda aa: aa+10

print(xx(5))

xx = lambda aa, bb: aa+bb
print(xx(5,20))

def miFuncion(n):
        return lambda a: a*n

duplicador= miFuncion(2)
triplicador = miFuncion(3)
print ("llama la lamda le pasa el 5 y a la funcion el 2 = ", duplicador(5))
print ("llama la lamda le pasa el 5 y a la funcion el 3 = " ,triplicador(5))

#modulos llama a otros archivos
#import operaciones
#print(operaciones.sumar(2,3))

#excepciones
print("-------------- excepciones -----------")

try:
    numero = 10/0
    print("Manejo excpeciones try")
except ZeroDivisionError:
    print("error no se puede divir por cero")

tupla_a = (1, 2) 
tupla_b = (1, 3) 
tupla_c =  tupla_a * 2 + tupla_b
print(tupla_c)


x, y, z = "manzana", "naranja", "banana"
print (y)