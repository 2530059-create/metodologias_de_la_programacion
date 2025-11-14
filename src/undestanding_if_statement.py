cars= ("audi","bmw", "subaru", "toyota")


for car in cars:
    if car=="bmw":
        print (car.upper())
    else:
        print (car)


# El condicional es el corazon de un if 

car= "bmw "
print (car== "bmw") # esto te regresa un true o false 

# condicinal false

car= "Audi"
print (car== "audi") # esto da false porque aunque sea igual tiene una letra diferente
# posible solucion a entradas de usuario

car="Audi"
print (car.lower()=="audi") # esto debe de dar true

# operador relaconal != para determinar la desigualdad

requested_topping= "mushroom" 



answer=17
if answer != 42: 
    print ("es diferente")



# es para saber que hay un nombe en una lista 

banned_students= ["jorge","calos","moyra","gus","host"]
user= "mauro"
print (user not in banned_students) # true
print ("jorge"  in banned_students) # true




game_active= True 
can_edit= False 



age= int (input ("\ndime cual es tu edad: "))
print (age)

if age>= 18:
    print ("\n eres mauyor de edad")
else:
    print ("eres putito")
