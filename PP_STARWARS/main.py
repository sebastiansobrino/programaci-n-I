'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''
import funciones

def starwars_app():
    lista_personajes = funciones.cargar_json(r"C:\Users\Seba\Desktop\Primer cuatrimestre\Programacion_l\parcial\PP_STARWARS\data.json")
    while(True):
        print("1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input()
        if(respuesta=="1"):
            funciones.ordenar(lista_personajes,"height")
        elif(respuesta=="2"):
            funciones.mostrar_personaje_mas_alto_segun_genero(lista_personajes)
        elif(respuesta=="3"):
            funciones.ordenar(lista_personajes,"mass")
        elif(respuesta=="4"):
            funciones.buscador(lista_personajes)
        elif(respuesta=="5"):
            funciones.exportar_csv(r"C:\Users\Seba\Desktop\Primer cuatrimestre\Programacion_l\parcial\PP_STARWARS\prueba.csv",lista_personajes)
        elif(respuesta=="6"):
            break


starwars_app()

