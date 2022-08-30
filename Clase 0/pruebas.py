

while(True):
    respuesta = input("numero?")
    respuesta = int(respuesta)

    print(type(respuesta))
    if (respuesta == 10):
        print("Es 10")
    elif (respuesta == 11):
        print("Es 11")
    else:
        print("No es 10")

    if (respuesta != 1):
        continue
    else:
        break

# range

lista = list(range(100))

for numero in lista:
    print(lista)

# otra forma con for

for numero in range(100):
    print(numero)

# Ejemplo para agregar mail

lista_nombres = []

while True:
    nombre = input("Nombre?")
    lista_nombres.append(nombre)

    rta = input("Pulse S para salir")
    if(rta == "S"):
        break

for nombre in lista_nombres:
    print(nombre)
