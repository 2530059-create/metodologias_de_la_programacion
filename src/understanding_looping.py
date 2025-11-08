"""
for sirve para repetir un bloque de codigo varias veces
y la variable que se le pone a for puede ser cualquier nombre
ejemplo de for panchito in magicians:
magicians es del tipo string y un a variable auxiliar

    magician es una variable auxiliar que toma: tambien es un string porque
    magicians es una lista de strings
     print(f"{magician.title()}, ese fue un gran hechizo!") es para combinar
     la variable magician con el string ese fue un gran hechizo!

los 4 espacios despues que hay y despues del for se llama indentacion
"""
print("\n ordenar las listas con el metodo for \n")

magicians=["ron","harry","snape","hermione","draco"]

for magician in magicians:
    print(magician)
    print(magician.upper())
    print(f"{magician.title()}, ese fue un gran hechizo!")
    print("\n")
print("Gracias a todos por participar en el show de hoy")


"""
  Identacion:
     python utiliza la identacion para determinar 
     cuando una linea de codigo esta conectada 
     a la linea de codigo anterior.

     Basicamente, se  utliza 4 espacios en blanco
     para obligarlos a a escribir codogo ordenado y 
     estructurado.
"""

# No olvidemos identar (lo que se necesita)
print("\n ordenar las listas con el metodo for-Ejemplo 1: \n")

# print (magician) # Error
magicians1=["alice","david","jorge"]

for magician in magicians1:
    print(magician)
    print ("\n")
print("fin del primer ejemplo")



print("\n ordenar las listas con el metodo for-Ejemplo 2: \n")

# identificacion Error
magicians2=["alice","david","jorge","candelario"]
for magician in magicians2:
    print(magician)
    print (f"great{magician}, I can't wait to see your next trick")
    print ("\n")
#print (f"great{magician}, I can't wait to see your next trick")

# identacion inecesaria

message= ("hola charly")
 # print(message) identacion inecesaria


# logical error 
magicians3=["alice", "david", "jorge", "candelario"]

for magician in magicians3:
    for magician in magicians:
     print(magician)
     print(magician.upper())
     print(f"{magician.title()}, ese fue un gran hechizo!")
     print("\n")
    print("Gracias a todos por participar en el show de hoy")
print("Gracias a todos por participar en el show de hoy")# se soluciona solo poniendolo a la izquierda 




















































print ("\n EJEMPLO HECHO PPOR MI \n")

friends=["nombre1", "nombre2", "nombre3", "nombre4", "nombre5", "nombre6", "nombre7"]

for friend in friends:
   print (friend)
   print (friend.upper())
   print ("\n")
print ("sinceramte creo que sw me esta haciendo faciel este metodo de aprendizaje")