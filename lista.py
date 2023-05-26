print("Hola Mundo!")
lista = [1,"Hola", 3.67, [1, 2, 3]]
print(lista)
print(lista[2])
print(lista [1])
a = [90, "Python", 3.87]
print(a[-1])
print(a[-2])
print(a[-3])
lista = [1,2]
lista.append (3)
lista.append (4)
print(lista) #[1,2,3,4]
lista =[1,2]
lista.extend ([3,4,5,6,7]) # el extend sirve para añadir mas valores a la lista
print(lista)
lista =[1,3]
lista.insert (1,"Casa")
print(lista) #[1,"Casa", 3]
lista = [1,2,3]
lista.remove (2)# el remove sirve para quitar un valor de la lista
print(lista)
lista =[1,2,3] #  el popo elimina el ultimo valor de la  lista
lista.pop(1)
print(lista)
lista= [1,2,3]
lista.reverse () # el reverse sirve para dar vuelta las lista de mayor a menor
print(lista)#[3,2,1]
lista_numerica =[11,3,7,2,8]
lista_numerica.sort() # el sort sirve para ordenar los numeros de menor a mayor y textos
print(lista_numerica) 
lista_texto =["HolaB","HolaC","holaA","c","b","c","A","a"]
lista_texto.sort()
print(lista_texto)