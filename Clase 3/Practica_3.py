from data_stark import lista_personajes


'''
[
  {
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
  }
] 

1. Heroe mas alto.
2. Heroe mas bajo.
3. Altura promedio
4. Heroe mas pesado.
5. Heroe menos pesado.
6. Salir
'''



def heroe_mas_alto():
    #Heroe mas alto
    altura_maxima = float(lista_personajes[1]["altura"])
    for heroe in lista_personajes:
        altura = float(heroe["altura"])
        if (altura > altura_maxima):
            altura_maxima = altura
            Heroe_alto = heroe

    print(Heroe_alto)

def heroe_mas_bajo():

    altura_minima = float(lista_personajes[1]["altura"])
    for heroe in lista_personajes:
        altura = float(heroe["altura"])
        if (altura < altura_minima):
            altura_minima = altura
            heroe_bajo = heroe

    print(heroe_bajo)

def altura_promedio():
    acumulador_de_altura = 0

    for heroe in lista_personajes:
        altura = float(heroe["altura"])
        acumulador_de_altura += altura

    print(acumulador_de_altura/len(heroe))

def heroe_mas_pesado():
    peso_maxima = float(lista_personajes[1]["peso"])
    for heroe in lista_personajes:
        peso = float(heroe["peso"])
        if (peso > peso_maxima):
            peso_maxima = peso
            heroe_pesado = heroe

    print(heroe_pesado)

def heroe_menos_pesado():
    peso_minima = float(lista_personajes[1]["peso"])
    for heroe in lista_personajes:
        peso = float(heroe["peso"])
        if (peso < peso_minima):
            peso_minima = peso
            heroe_menos_pesado = heroe

    print(heroe_menos_pesado)



while(True):
    respuesta = input("Seleccione la opcion que desee saber: \n 1. Heroe mas alto. \n 2. Heroe mas bajo. \n 3. Altura promedio \n 4. Heroe mas pesado. \n 5. Heroe menos pesado. \n 6. Salir\n >")
    if (respuesta == "1"):
        heroe_mas_alto()
    elif (respuesta == "2"):
        heroe_mas_bajo()
    elif (respuesta == "3"):
        altura_promedio()
    elif (respuesta == "4"):
        heroe_mas_pesado()
    elif (respuesta == "5"):
        heroe_menos_pesado()
    elif (respuesta == "6"):
        break
    


