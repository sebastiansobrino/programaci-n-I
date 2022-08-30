
contador = 0
suma_magia_fuerza = 0
suma_edad_heroinas = 0
suma_edad_heroes = 0


while(True):
    
    heroe = input ("Ingrese el heroe o heorina")
    heroe = heroe.lower()

    while (heroe.isnumeric()):
        heroe = input ("Error. Ingrese el heroe o heroina")
        heroe = heroe.lower()

    
    edad = input("Ingrese la edad")
    edad = int (edad)
    while (not(edad > 10 and edad < 100)):
        edad = input("Ingrese la edad")
        edad = int (edad)

    sexo = input ("Ingrese el sexo")
    sexo = sexo.lower()

    while (sexo != "m" and sexo != "f" and sexo != "nb" ):
        sexo = input ("Error. Ingrese el sexo")
        sexo = sexo.lower()


    habilidad = input ("Ingrese su habilidad")
    habilidad = habilidad.lower()

    while (habilidad != "fuerza" and habilidad != "magia" and habilidad != "inteligencia" ):
        habilidad = input ("Error. Ingrese su habilidad")
        habilidad = habilidad.lower()



    if (habilidad == "fuerza"):
        if (contador == 0):
            edad_mas_joven = edad
            heroe_mas_joven = heroe
        elif (edad_mas_joven > edad):
            edad_mas_joven = edad
            heroe_mas_joven = heroe
    
    if (sexo == "f"):
        suma_edad_heroinas += edad
        if (habilidad == "fuerza" or habilidad == "magia"):
            suma_magia_fuerza += 1
    elif (sexo == "m"):
        if (habilidad == "fuerza"):
            suma_edad_heroes += edad

        
    if (contador == 0):
        edad_mas_grande = edad
        heroe_mas_viejo = heroe
        sexo_del_viejo = sexo
    elif (edad_mas_grande < edad):
        edad_mas_grande = edad
        heroe_mas_viejo = heroe
        sexo_del_viejo = sexo

    contador += 1

    respuesta = input ("Desea ingresar otro heroe?")
    respuesta.lower()

    if (respuesta == "si"):
        continue
    elif (respuesta == "no"):
        break

promedio_edad_heroinas = suma_edad_heroinas / contador
promedio_edad_heroes = suma_edad_heroes / contador

mensaje_uno = "El heroe/heroina mas joven es " + heroe_mas_joven
mensaje_dos = f"El sexo y nombre del heroe/heroina mas grande es {sexo_del_viejo} {heroe_mas_viejo}"
mensaje_tres = f"La cantida de heroinas que tiene habilidad de fuerza o magia es {suma_magia_fuerza}"
mensaje_cuatro = f"El promedio de edad entre heronias es: {promedio_edad_heroinas} años"
mensaje_cinco = f"El promedio de edad entre heroes de fuerza es {promedio_edad_heroes} años"

print(mensaje_uno + "\n" + mensaje_dos + "\n" + mensaje_tres + "\n" + mensaje_cuatro + "\n" + mensaje_cinco)