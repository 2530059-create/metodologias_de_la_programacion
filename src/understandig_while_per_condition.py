"""
vamos a relixae un prograna con contaraseña
defina el pin como contraseña 

despues vamos a darle 3 intentos al usuario
para escribir el pin

si el usuario escribe correctamente le pin 
el programa debe mostrar un mensaje  de acceso permitido 

si el usuario se equivoca se le debe de decir
cuantos intentos le quedan 

"""
MAX_ATTEMPTS = 3
intents= 0
CORRECT_PIN= "190407"
user_pin = input ("ESCRIBE EL PIN: ")
while intents < MAX_ATTEMPTS:
    if user_pin == CORRECT_PIN:
        print ("acceso permitido")
        break
