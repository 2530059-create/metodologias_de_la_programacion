"""
un script es una manera sencilla una serie de caracteres.

en python todo loq ue se encuentre dentro de comillas simples 

'' o dobles comillas"" es un string

  ""esto es un string""
  'esto tambirn lo es'
  
  'le dije a un amigo,"python es mi lenguje favorito"
  "el lenguaje 'python' lleva el nombre por monty python, no por la serpiente"

 metoddos de las variables de tipo string
 'title: sirve para poner la ´primera letra en mayuscula'
 
"""
name="clase de programacion"
print(name)
print (name.title() )
print (name)

"""
un metodo es una accioon que python puede realizar en un fragmento de datos o sobre la variable.


El punto . despues de una variable seguida des metodo title() dice que se tiene que ejecutar 
El metodo title () de la variable name.

todos los metodos van seguidos de parentesis 
porque en ocaciones necesitan informacion adicional
para funcionar lo cual iria dentro de los parentesis.
en esta ocasion el metodo .title() no requiere
informacion adicional para ejecutarse


"""

print(name.upper())
print(name. lower())

# cincatenacion de strings 
print("CONCATENACION DE STRINGS")
first_name="JULIAN"
last_name="CARMONA"
full_name= first_name + " " + last_name
print(full_name)

print("Hola, " + full_name.title() + "!")