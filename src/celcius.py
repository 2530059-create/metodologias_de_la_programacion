

temperature=float(input("SET YOUR TEMPERATURE IN CELCIUS: "))

farenheit= temperature * 9 / 5 + 32
print (f"it is your temperature in farenheit: {farenheit}" )

kelvin= temperature + 273.15

print (f"it is your temperature in kelvin: {kelvin} ")

if temperature <30:
     print ("FALSE: 'is low temperature'")
elif temperature >=30:
    print("TRUE: 'ias high temperature'")
            
