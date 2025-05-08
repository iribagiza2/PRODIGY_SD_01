# Temperature conversion program

# User prompts

temperature = float(input("Enter the temperature: "))
print("------------------------------")
print("Temperature scales: ")
print("1. C for Celsius")
print("2. F for Fahrenheit")
print("3. K for Kelvin")
unit = int(input("Unit(choose from 1 to 3): "))
while unit < 1 or unit > 3: 
    unit = int(input("Unit(choose from 1 to 3): "))

if unit == 1:
    print("The original Temperature is", temperature, "degrees Celsius")

elif unit == 2:
    print("The original Temperature is", temperature, "degrees Fahrenheit")

else:
    print("The original Temperature is", temperature, "Kelvin")

# Temperature conversions

# Conversion from Degrees Celsius(C)  
# F = (C * 9/5) + 32
# K = C + 273.15

if unit == 1:
    F = (temperature * 9/5) + 32
    K = temperature + 273.15
    print("Temperature in Fahrenheit is ", F)
    print("Temperature in Kelvin is ", K)

# Conversion from Degrees Fahrenheit(F)  
# C = (F * 9/5) + 32
# K = C + 273.15

elif unit == 2:
    C = (temperature - 32) * 5/9
    K = C + 273.15
    print("Temperature in Fahrenheit is ", C)
    print("Temperature in Kelvin is ", K)

# Conversion from Kelvin(K)  
# C = K - 273.15
# F = (K - 273.15) * 9/5 + 32
else:
    C = temperature - 273.15
    F = (temperature - 273.15) * 9/5 + 32
    print("Temperature in Celsius is ", C)
    print("Temperature in Fahrenheit is ", F)