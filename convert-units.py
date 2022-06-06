def convertTempeture():
    temp = input("1- Celcius to Fahrenheit\n2- Fahrenheit to Celcius\n3- Celcius to Kelvin\n4- Fahrenheit to Kelvin\nPlease Enter:")
    if temp =='1':
        celcius = float(input("Celcius: "))
        fahrenheit = (celcius * 1.8) + 32
        print(f"{celcius} Celcius = {fahrenheit} Fahrenheit")
    elif temp == '2':
        fahrenheit = float(input("Fahrenheit: "))
        celcius = round(((fahrenheit-32) * 0.5556),2)
        print(f"{fahrenheit} Fahrenheit = {celcius} Celcius")
    elif temp == '3':
        celcius = float(input("Celcius: "))
        kelvin = celcius + 273.15
        print(f"{celcius} Celcius = {kelvin} Kelvin")
    elif temp == '4':
        fahrenheit = float(input("Fahrenheit: "))
        kelvin = round((((fahrenheit -32)*5)/9 + 273.15),2)
        print(f"{fahrenheit} Fahrenheit = {kelvin} Kelvin")
    else:
        print("Please enter again.")
        convertTempeture()

def convertWeight():
    wei = input("1- Ton to Kilogram\n2- Kilogram to Ton\n3- Kilogram to Hectogram\n4- Kilogram to Gram\n5- Kilogram to Miligram\n6- Kilogram to Pound\n7- Pound to Kilogram\n8- Gram to Kilogram\nPlease Enter:  ")
    if wei == '1':
        ton = float(input("Ton: "))
        kilogram = ton * 1000
        print(f"{ton} Ton = {kilogram} Kilogram")
    elif wei == '2':
        kilogram = float(input("Kilogram: "))
        ton = kilogram/1000
        print(f"{kilogram} Kilogram = {ton} Ton")
    elif wei == '3':
        kilogram = float(input("Kilogram: "))
        hectogram = kilogram * 10
        print(f"{kilogram} Kilogram = {hectogram} Hectogram")
    elif wei == '4':
        kilogram = float(input("Kilogram: "))
        gram = kilogram * 1000
        print(f"{kilogram} Kilogram = {gram} Gram")
    elif wei == '5':
        kilogram = float(input("Kilogram: "))
        miligram = kilogram * 1000000
        print(f"{kilogram} Kilogram = {miligram} Miligram")
    elif wei == '6':
        kilogram = float(input("Kilogram: "))
        pound = round(kilogram * 2.2046, 2)
        print(f"{kilogram} Kilogram = {pound} Pound")
    elif wei == '7':
        pound = float(input("Pound: "))
        kilogram = round(pound / 2.2046,2)
        print(f"{pound} Pound = {kilogram} Kilogram")
    elif wei =='8':
        gram = float(input("Gram: "))
        kilogram = gram / 1000
        print(f"{gram} Gram = {kilogram} Kilogram")
    else:
        print("Please enter again.")
        convertWeight()
def convertLenght():
    length = input("1- Kilometer to Meter\n2- Meter to Kilometer\n3- Kilometer to Mile\n4- Mile to Kilometer\n5- Kilometer to Yards\n6- Yards to Kilometer")
    if length == '1':
        kilometer = float(input("Kilometer: "))
        meter = kilometer * 1000
        print(f"{kilometer} Kilometer = {meter} Meter")
    elif length == '2':
        meter = float(input("Meter: "))
        kilometer = meter / 1000
        print(f"{meter} Meter = {kilometer} Kilometer")
    elif length == '3':
        kilometer = float(input("Kilometer"))
        mile = round(kilometer / 1.60934,2)
        print(f"{kilometer} Kilometer = {mile} Mile")
    elif length == '4':
        mile = float(input("Mile: "))
        kilometer = round(mile * 1.60934,2)
        print(f"{mile} Mile = {kilometer} Kilometer")
    elif length == '5':
        kilometer = float(input("Kilometer: "))
        yards = (kilometer * 1093.613298,2)
        print(f"{kilometer} Kilometer = {yards} Yards")
    elif length == '6':
        yards = float(input("Yards: "))
        kilometer = round(yards / 1093.613298,2)
        print(f"{yards} Yards = {kilometer} Kilometer")
    else:
        print("Please enter again.")
        convertLenght()
def convertTime():
    length = input("1- Kilometer to Meter\n2- Meter to Kilometer\n3-Kilometer to Mile\n4- Kilometer to Yards")
    if length == '1':
        pass
    elif length == '2':
        pass
    elif length == '3':
        pass
    elif length == '4':
        pass
    else:
        print("Please enter again.")
        convertLenght()


choice = input("Which conversion would you like to do?\n1- Tempeture\n2- Weight\n3- Lenght\n4- Time(not active)\n Please Enter: ")
if choice == '1':
    convertTempeture()
elif choice == '2':
    convertWeight()
elif choice == '3':
    convertLenght()
elif choice == '4':
    convertTime()
else:
    print("Please enter again.")