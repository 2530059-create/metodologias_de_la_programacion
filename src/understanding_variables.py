import traceback


message="this is a variable"
another_message = "this is another variable"
print(message)
print(another_message)

print (message, another_message)


"""
Yo tampoco lo tengo
"""

Julian_massage="Hola, soy Julian"
print(Julian_massage)



"""
traceback es un registro en donde el interprete tubo problemas para ejecutar el codigo.

Traceback (most recent call last):
  File "c:/Users/julia/projects/metodologias_de_la_programacion/src/understanding_variables.py", line 17, in <module>
    print(Julian_masage)
          ^^^^^^^^^^^^^
NameError: name 'Julian_masage' is not defined. Did you mean: 'Julian_massage'?

name error: significa que olvidamos establecer el valor de una variable antes de usarla, o cometimos un error al ingresar el nombre de la variable.
"""

