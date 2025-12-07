"""
vamos a relizar un progrma que sume pesos mexicanos
hasta que el usuario escriba la apalabra salir 

el programa tambien debe decirme cuantos numeros
ingreso el usuario, cual fue el minimo y cual fue  el 
maximo
"""


sum_numbers= 0.0 # este es flotante
counter=0 #es entero 
minimum= None # esta variable se le asigna el none para qur no se le de un valor porque genera problemas
maximum= None

while True:
    print ("inggrsa la palabra 'salir' para terminar")
    user_input= input ("ingresa una cantidad (MXN)")
    # centinel
    if user_input == "salir":
        break
    try:
        quantity= float (user_input)
    except ValueError:
     print ("cantidad no valida ingrese un numero entero")
     continue
    except KeyboardInterrupt:
     print ("programa cerrado por el usuario")
    break

counter = counter +1
sum_numbers+= quantity
if minimum is None or quantity <minimum:
   minimum = quantity
if maximum is None or quantity < maximum:
   maximum = quantity


print(sum_numbers)
print (counter)