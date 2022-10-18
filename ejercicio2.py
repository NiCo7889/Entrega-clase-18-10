def ejercicio2():
    lista = [1, 4, 2, 5, 4, 3, 4, 7, 5, 8, 9]
    lista.remove(4)
    lista.remove(4)
    lista.remove(5)
    lista.remove(7)
    lista.remove(8)
    lista.remove(9)
    # TODO
    assert lista == list(range(1, 6))

#Comprobación para ver si funciona
#lista = [1, 4, 2, 5, 4, 3, 4, 7, 5, 8, 9] 
#lista.remove(4)
#lista.remove(4)
#lista.remove(5)
#lista.remove(7)
#lista.remove(8)
#lista.remove(9)
#print(lista)
