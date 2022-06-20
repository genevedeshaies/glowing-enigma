#Program to estimate your young horse's mature height

values = {"Current Height" : "", 
"Measurement Unit" : "",
"Current Age" : "",
"Horse Type" : "",
}


# values["Current Height"] = input("What is your horse's current height at the withers? Please use cm, in or hh. ")

# if len(currentHeight) > 1:
#     usedMeasurement = currentHeight[1]
# else:
#     usedMeasurement = input("Is this measurement in cm, in or hh? ")

def getValues():
    height = input("What is your horse's current height at the withers? Please use cm, in or hh. ")
    height = list(height)
    type(height)
    values["Current Height"] = int(height[0])
    if len(height) > 1:
        unit = height[1]
    else:
        unit = input("Is this measurement in cm, in or hh? ")
    values["Measurement Unit"] = unit
    age = input("How old is your horse? Please enter age in months (mo). ")
    values["Current Age"] = age[0]
    type = input("What type of horse is this? Pony, stock, sport or draft? ")
    values["Horse Type"] = type[0].casefold()
    return values

print(getValues())
# def calculate(height, unit, type, age):

