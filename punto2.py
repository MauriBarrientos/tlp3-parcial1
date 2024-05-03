#Función para eliminar elementos duplicados
def eliminar_duplicados(lista):
    lista_nueva= []
    for elemento in lista: #Iteración que recorrera cada elemento de la lista
        if elemento not in lista_nueva:#Si el elemento no esta en la lista se agregará a la lista nueva
            lista_nueva.append(elemento) 
    return lista_nueva


print(eliminar_duplicados([1,2,3,4,4,5,6,6,7]))