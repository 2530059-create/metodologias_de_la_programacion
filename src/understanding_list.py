# LISTAS
# una lista es una coleccion de elementos ordenados y mutables
# se definen con corchetes [] y los elementos se separan por comas
fruits=["manzana", "banana", "cereza"]
print(fruits) # salida: ['manzana', 'banana', 'cereza']

# acceder a elementos de una lista

print(fruits[0].upper()) # salida: MANZANA
print(fruits[1].title()) # salida: Banana
print(fruits[2].title()) # salida: Cereza

#print(fruits[3])  index error porque no existe


"""

Una lista es mutable porque podemos cambiar sus elementos despues de haberla creado
si en los corchetes es una lista
cuando tiene corchetes es un elemento de la lista
y ahi se pueden utilizar todos los metodos de las listas
y se vuelve un string 


cuando se pone el -1 dentro de los corchetes
se esta indicando que se quiere acceder al ultimo elemento de la lista

la 0 seria igual a la -3 cuando te vienes de derecha a izquierda

"""
print(fruits[-1].title()) # salida: Cereza
print(fruits[-2].title()) # salida: Banana
print(fruits[-3].title()) # salida: Manzana

#print(fruits[-4]) # IndexError porque no existe



"""
la f es para convinar las variables y los strings
se pone la f antes de las comillas iniciales


"""
message=f"Mi fruta favorita es la {fruits[0].title()}"
print(message) # salida: Mi fruta favorita es la Manzana

"""
agregar elementos a la lista con append()
el metodo append() agrega un elemento al final de la lista


"""
print("\n Agregar elementos a la lista con append() \n")

motorcycles=['honda', 'yamaha', 'suzuki']
print(motorcycles) # salida: ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles) # salida: ['honda', 'yamaha', 'suzuki', 'ducati']


"""
agrega elementos a la lista con insert()
el metodo insert() agrega un elemento en la posicion escifica de la lista
se debe indicar la posicion y el elemento a agregar
"""

print("\n Agregar elementos a la lista con insert() \n")

motorcycles=['honda', 'yamaha', 'suzuki']
print(motorcycles) # salida: ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles) # salida: ['ducati', 'honda', 'yamaha', 'suzuki']
print(motorcycles[0]) # salida: ducati



"""
insert es para insertar un elemento en una posicion especifica
append es para agregar un elemento al final de la lista

el metodo upper es para string
el metodo append e insert son para listas{}

el metodo insert requiere dos argumentos
y el metodo append toma solo un elemento
"""






# Eleiminar elementos de una lista
print("\n Eliminar elementos de una lista \n")

"""
Eliminar elementos de una lista
 del- para eliminar un elemento de una lista elimina un 
 elemento en una posicion especifica
""" 
print("\n Eliminar elementos de una lista utiliando el metodo del \n")
motorcycles=['honda', 'yamaha', 'suzuki']
print(motorcycles) # salida: ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles) # salida: ['yamaha', 'suzuki']




"""
eliminar elemntos de una lista utulizando el metodo pop
este si es un metodo de las listas

"""
print("\n Eliminar elementos de una lista  utilizando el metodo popped\n")
motorcycles=['honda', 'yamaha', 'suzuki']
print(motorcycles) # salida: ['honda', 'yamaha', 'suzuki']
popped_motorcycle=motorcycles.pop(0)
print(motorcycles) # salida: ['yamaha', 'suzuki']
print(f"La moto que fue sacada de la lista es la {popped_motorcycle.title()}")


print("\n Eliminar elementos de una lista  utilizando el metodo remove\n")

""""
ekiminar elementos de una lista utilizando el metodo 
remove
el metodo remove elimina un elemento por su valor   
 estas son listas con strings
input es igual a leer y a escribir como si fuera pseudocodigo
"""


motorcycles=['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles) # salida: ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles) # salida: ['honda', 'yamaha', 'suzuki']


# ejemplo paractico de remove

print("\n Ejemplo practico de remove \n")

names=['juan', 'maria', 'pedro', 'ana']
print(names) # salida: ['juan', 'maria', 'pedro', 'ana
nombre_eliminado= input("ingresa el nombre que deseas eliminar de la lista: ")
names.remove(nombre_eliminado.strip().lower())
print(names) # salida: ['juan', 'maria', 'ana'] si se ingresa pedro 

