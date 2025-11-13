# slicing
"""
el slacing es obteer pedasos de una lista 

"""
players= ["CR7","messi","travis","chicha","Corona" ]
print(players[0:3])

#  slice es trabajaar con un grupo especifico de una lista 

print(players[1:4])

# slicing en un for

players1= ["CR7","messi","travis","chicha","Corona" ]
first_three_player=(players1 [0:3])

print("fisrt three player", first_three_player)

print ("aqui viene los 3 mejores jugasdores de futbol del año")

for player in players [0:3]:
    print (player.upper)


# como copiamos una lista 


my_food=("pizza","gorditas de jaumave","machacado")
#copy_of_food= my_food # manera errone a de copiar una lista 


copy_of_food_1= my_food[:] # esta es la menara correcta de copiar una lista 
copy_of_food_1= my_food.copy()
copy_of_food_1= list(my_food)

# modificando elementos
cars=["bwm","porch","masda","totoya","ford"]

cars[0]="bmw"
cars[1]="porsche"
cars[2]="mazda"
cars[3]="toyota"


# esto ya seria una lista corregida

"""
cuando se pone un for es para poder poner los nombres de las listas 
en forma vertical. 
caundo esta en forma horizontal es por que esta en metodo de lista.

cuando se hace una lista python aparta espacio por que las listas son mutables 

las tuplas son listas inmutbles es decir que si tienen 5 elementos 
se van a quedar en 5 elementos para siempre por que son no mutables 
"""
