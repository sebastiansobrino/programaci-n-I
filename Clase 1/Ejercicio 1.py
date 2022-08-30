#La división de higiene está trabajando en un control de stock para productos sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos:
#El tipo (validar "barbijo", "jabón" o "alcohol")
#El precio: (validar entre 100 y 300)
#La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
#La marca y el Fabricante.

# Se debe informar lo siguiente:
#Del más caro de los barbijos, la cantidad de unidades y el fabricante.
#Del ítem con más unidades, el fabricante.
#Cuántas unidades de jabones hay en total.

from xml.dom.expatbuilder import FragmentBuilder


unidades_de_jabones = 0
unidades_de_barbijos = 0
unidades_de_alcohol = 0
cantidad_de_jabones = 0
maximo_precio = 0



for i in range(5):

    tipo = input("Ingrese el tipo de producto: Barbijo, Jabon o Alcohol")
   
    while (tipo != "Barbijo" and tipo != "Jabon" and tipo != "Alcohol"):
        tipo = input("Error. Ingrese Barbijo, Jabon o Alcohol")
    
    precio = input("Ingrese precio del producto")
    precio = int(precio)

    while (not(precio > 100 and precio < 300)):
        precio = input("Error. Ingrese un valor entre 100 y 300")
        precio = int(precio)
    
    cantidad_de_unidades = input("Ingrese cantidad de unidades (entre 0 y 1000)")
    cantidad_de_unidades = int(cantidad_de_unidades)

    while(not(cantidad_de_unidades > 0 and cantidad_de_unidades < 1000)):
        cantidad_de_unidades = input("Error. Ingrese valores entre 0 y 1000")
        cantidad_de_unidades = int(cantidad_de_unidades)

    fabricante = input("Ingrese el fabricante")
   
    if (tipo == "Jabon"):
        cantidad_de_jabones += 1
        unidades_de_jabones += cantidad_de_unidades
        fabricante_jabon = fabricante
    elif (tipo == "Barbijo"):
        
        unidades_de_barbijos += cantidad_de_unidades
        fabricante_barbijo = fabricante
            
        if (i == 0):
            maximo_precio = precio
            cantidad_maxima = cantidad_de_unidades
            fabricante_maximo = fabricante
        elif (maximo_precio < precio):
            maximo_precio = precio
            cantidad_maxima = cantidad_de_unidades
            fabricante_maximo = fabricante      
    else:
        unidades_de_alcohol += cantidad_de_unidades
        fabricante_alcohol = fabricante

if (unidades_de_barbijos == 0):
    mensaje_uno = "No se ingresaron barbijos"
else:
    mensaje_uno = f"La cantidad de unidades vendidas es {cantidad_maxima} y su fabricante es  {fabricante_maximo}"

if (unidades_de_jabones > unidades_de_barbijos and unidades_de_jabones > unidades_de_alcohol):
    mensaje_dos = "El fabricante de jabones, la unidad mas vendida, es " + fabricante_jabon
elif (unidades_de_barbijos > unidades_de_jabones and unidades_de_barbijos > unidades_de_alcohol):
    mensaje_dos = "El fabricante de barbijos, la unidad mas vendida, es " + fabricante_barbijo
elif (unidades_de_alcohol > unidades_de_barbijos and unidades_de_alcohol > unidades_de_jabones):
    mensaje_dos = "El fabricante de alcoholes, la unidad mas vendida, es " + fabricante_alcohol
else:
    mensaje_dos = "No hubo diferencias"

mensaje_tres = f"La cantidad de jabones es {cantidad_de_jabones}" 

print(mensaje_uno + "\n" + mensaje_dos + "\n" + mensaje_tres)



        

     
        
    