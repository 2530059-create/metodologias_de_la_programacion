"""
functions 

las funcuines son bloques de codigo para realizar 
una tarea especifica 

cuando queremos realizar la tarea que se a definido
en una funcion, tenemos que llenar el nombre de 
la funcion resposable.

defimicion de un a funcion (sintax)
def

con la palabra reservada def: defini un a funcion 
"""


def greeting_mauro ():
    print ("HOLA MAURO")


greeting_mauro()
greeting_mauro()

username= input ("Escribe tu nombre")

def greet(username):
    print ( f"hola {username} como estas", )

greet(username )

"""
vamos a relizar un programa que genere
el nombre completo de una persona

vamos a pasarla por primer nombre, el segundo 
es el apellido 

la funcion debe genrear el nombre completo y regresarlo

"""

def create_full_name (first_name, midle_name, last_name):
    full_name = f"{first_name}{midle_name}{last_name}"
    return full_name.title

user_firts_name= input ("Escribe tu primer nombre: ").strip().lower
user_middle_name= input ("Escribe tu segundo nombre: ").strip().lower
user_last_name= input ("Escribe tus apellidos: ").strip().lower

print (create_full_name(
    user_firts_name,
    user_middle_name,
    user_last_name,
    ))


# argumentos clave keyword arguments

"""
los positional tiene que ser siempre en orden 
y el keyword no importa siempre y cuando le des las especificaciones 
que te lo pide

"""


# parametros opcionales

"""
cuando un argumento es opcionale se le tiene que
 poner un string vacio 

"""

## temas para estudiar a futuro 

#funciones: args, kgargs
# manejo de datos: cvs, yeison, etc
# argumentos por linea de comandos 
# cli : comand line interface
# generadores, interadores, yield
# tesiting 