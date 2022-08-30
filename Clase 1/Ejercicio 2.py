#Ejercicio Integrador 02

#La división de alimentos está trabajando en un pequeño software para cargar las compras de ingredientes para la cocina de Industrias Wayne. 
#Realizar el algoritmo permita ingresar los datos de una compra de ingredientes para
#preparar comida al por mayor, HASTA QUE EL CLIENTE QUIERA.
#PESO: (entre 10 y 100 kilos)
#PRECIO POR KILO: (mayor a 0 [cero]).
#TIPO VALIDAD: ("v", "a", "m");(vegetal, animal, mezcla).
#Además tener en cuenta que si compro más de 100 kilos en total tenes 15% de descuento sobre el precio bruto. o si compro más de 300 kilos en total, tenes 25% de descuento sobre el precio bruto.
#El importe total a pagar, BRUTO sin descuento.
#El importe total a pagar con descuento (Solo si corresponde).
#Informar el tipo de alimento más caro.
#El promedio de precio por kilo en total.
# Sobrino Sebastian comision_01


    
importe_sin_descuento = 0
peso_total = 0
acumulador_v = 0
acumulador_a = 0
acumulador_m = 0
contador = 0
suma_precio = 0

while(True):
    peso = input("Ingrese el peso del producto")
    peso = float (peso)

    while (not(peso > 10 and peso < 100)):
        peso = input("Ingrese el peso del producto")
        peso = float (peso)

    precio = input("Ingrese el precio del producto")
    precio = float (precio)

    while (not(precio > 0)):
        precio = input("Ingrese el precio del producto")
        precio = float (precio)

    tipo = input ("Ingrese el tipo de ingrediente")

    while (tipo != "v" and tipo != "a" and tipo != "m" ):
        tipo = input ("Error. Ingrese el tipo de ingrediente")
    
    total = precio * peso
    importe_sin_descuento += total
    peso_total += peso
    suma_precio += precio  

    if (tipo == "a"):
        acumulador_a += total
    elif (tipo == "v"):
        acumulador_v += total
    else:
        acumulador_m += total

    contador += 1

    respuesta = input ("Desea continuar?")
    respuesta.lower()

    if (respuesta == "si"):
        continue
    elif (respuesta == "no"):
        break

mensaje_uno = f"El importe bruto es {importe_sin_descuento}"

if (peso_total > 100):
    descuento = 0.15
elif (peso_total > 300):
    descuento = 0.25
else:
    descuento = 0

importe_total = importe_sin_descuento - (importe_sin_descuento * descuento)

mensaje_dos = f"El importe con descuento es {importe_total}"

if (acumulador_a > acumulador_m and acumulador_a > acumulador_v):
    mensaje_tres = "El tipo de alimento mas caro es: a"
elif (acumulador_m > acumulador_a and acumulador_m > acumulador_v):
    mensaje_tres =  "El tipo de alimento mas caro es: m"
elif (acumulador_v > acumulador_m and acumulador_v > acumulador_a):
    mensaje_tres =  "El tipo de alimento mas caro es: v"
else:
    mensaje_tres = "No hubo diferencias"

promedio_precio = suma_precio / contador

mensaje_cuatro = f"El promedio de precio por kilo es: ${promedio_precio}"

print(mensaje_uno + "\n" + mensaje_dos + "\n" + mensaje_tres + "\n" + mensaje_cuatro)



    



          