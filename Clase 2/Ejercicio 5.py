

#mi_dic = {"nombre" : "Karen", "Apellido" : "jurgens", "edad" : "35", "Ocupacion" : "Periodista"}

#mi_dic ["edad"] = "36"
#mi_dic ["Ocupacion"] = "Editora"

#print(mi_dic)

#lista = [1,2,3,"raul"]
#lista_dos = []

#for i in lista:
#    if (isinstance(i, int)):
#        print(i)
#    else:
#        lista_dos = [i]
#        print(lista_dos)

lista = []
while (True):
    clientes = input("Ingrese cliente")

    lista.append(clientes)

    respuesta = input("Desea continuar")
    respuesta = respuesta.lower()
    
    if(respuesta == "si"):
        continue
    else:
        break

print(lista)