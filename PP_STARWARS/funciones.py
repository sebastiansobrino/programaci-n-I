import json
import re

def pasar_elementos_int(valor:str):
    '''
    Recibe un valor como tipo de dato str
    Pasa un tipo de dato str a int
    Retorna el valor en int
    '''
    return int(valor)


def cargar_json(archivo:str):
    '''
    Recibe un str
    Permite abrir un archivo Json en modo lectura
    Retorna una lista con diccionarios dentro
    '''
    with open(archivo,"r") as file:
        bibioteca = json.load(file)
        return bibioteca["results"]

def hallar_max(lista:list,keys:str):
    '''
    Recibe una lista y una keys
    Permite hallar el maximo valor
    Retorta el indice de ese valor
    '''
    if(len(lista) > 0):
        minimo_maximo = 0
        for elementos in lista:
            elementos[keys] = pasar_elementos_int(elementos[keys])
        for i in range(1,len(lista)):
            if(lista[i][keys] < lista[minimo_maximo][keys]):
                minimo_maximo = i
        return minimo_maximo
    else:
        print(-1)

def ordenar (lista:list,keys:str):
    if(len(lista) > 0):
        lista_auxiliar = lista [:]
        lista_ordenada = []
        while(len(lista_auxiliar) > 0):
            lista_ordenada.append(lista_auxiliar.pop(hallar_max(lista_auxiliar,keys)))
        return lista_ordenada
    else:
        print(-1)

def mostrar_personaje_mas_alto_segun_genero(lista:list):
    '''
    Recibe una lista.
    Permite hallar el personaje mas alto de cada genero
    No retorna nada. Imprime los personajes mas altos de cada genero
    '''
    if(len(lista) > 0): 
        valor_min_hombres = 0
        valor_min_mujeres = 0
        valor_min_n_a = 0
        for elementos in lista:
            elementos["height"] = pasar_elementos_int(elementos["height"])
            if(elementos["gender"] == "male"):
                if(elementos["height"] > valor_min_hombres):
                    valor_min_hombres = elementos["height"]
                    nombre_hombre_alto = elementos
            elif(elementos["gender"] == "female"):
                if(elementos["height"] > valor_min_mujeres):
                    valor_min_mujeres = elementos["height"]
                    mujer_mas_alta = elementos
            else:
                if(elementos["height"] > valor_min_n_a):
                    valor_min_n_a = elementos["height"]
                    n_mas_alta = elementos
        print("El hombre mas alto es: {0} - La mujer mas alta es: {1} - El n/a mas alto es: {2}".format
                (nombre_hombre_alto["name"],mujer_mas_alta["name"],n_mas_alta["name"]))       
    else:
        print(-1)

def buscador(lista:list):
    '''
    Recibe una lista.
    Permite al usuario ingresar una palabra y buscarla en la lista.
    Imprime al personaje buscado con sus caracteristicas
    '''
    if(len(lista) > 0):
        palabra_buscada = input("Que palabra desea buscar")
        for elementos in lista:
            if(re.search(palabra_buscada,elementos["name"],re.IGNORECASE)):
                print("name: {0} | height: {1} | mass: {2} | gender: {3}".format
                    (elementos["name"],elementos["height"],elementos["mass"],elementos["gender"]))
    else:
        print(-1)

def exportar_csv(archivo:str,lista:list):
    '''
    Recibe una lista y un archivo en tipo de dato str.
    Permite exportar un archivo a formato CSV
    No retorna nada. Crea un archivo CSV
    '''
    if(len(lista) > 0):
        with open(archivo,"w") as file:
            for elementos in lista:
                file.write("name: {0} | height: {1} | mass: {2} | gender: {3}\n".format
                    (elementos["name"],elementos["height"],elementos["mass"],elementos["gender"]))
    else:
        print(-1)