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

print ("Hola, " + full_name.title() + "!")


# syntax error en strings 
message="una fortaleza de python es su comunidad"
print (message)


message_two= "una fortaleza de 'python' es su comunidad"
print(message_two)
"""
un error de sintaxis ocurre cuando python no puede interpretar nuestro codigo
te aviisa en la terminal con un mensaje de error y la ubicacion del error en el codigo.

apararece interpretado de esta manera:


    File "c:/Users/julia/projects/metodologias_de_la_programacion/src/understanding_strings.py", line 42
        message_two= "una fortaleza de 'python' es su comunidad
                                                                    ^


"""

# concatenacion con f-strings
famous_person="albert einstein"
quote="python is love"

# concatenacion convencional
message= famous_person + "una vex dijo " + quote
print(message)

# concatenacion con f-strings

message_f_strings= f"{famous_person}  una vez dijo  {quote}"
print(message_f_strings)


# ACTIVIDAD
"""
1) elije un pesonaje famoso e igualao a una variable del tipo strings
2)elije una frase famosa que haya dicho e igualao a una variable del tipo string
3)usa f-strings para crear un mensaje que combine el nombre del personaje y la cita
4)imprime el mensaje
"""

famous_person="Socrates"
quote="solo se que no se nada"       
message_f_strings= f"{famous_person}  una vez dijo  {quote}"
print(message_f_strings)

