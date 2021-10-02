print ("I can python")

print (5-3)
print (9/4)
print (9//4)
print (20-5*(2+1))

variableForAString ="this is a string"
variableForAFloat = 15.2
variableForAnInteger = 121
variableForABoolean = True

print (variableForAString)
print (variableForAFloat) 
print (variableForAnInteger)
print (variableForABoolean)

variableForAnotherString = ("this is another string")
print (variableForAString + variableForAnotherString)
print (variableForAFloat + variableForAnInteger)

#python can only combine two data types that are the same e.g. 
#string + string or integer + float

print (variableForAString + str(variableForAnInteger))
#str() means it can change an integer into a string


print (f"some text: {variableForAString} {variableForAFloat}")
#F-strings combines strings with other data types

variableForAnInput = input("Enter a value to be put in the variable: ")
#print (variableForAnInput)
#




number1 = input("Enter whole number: ")
number2 = input("Enter decimal number: ")

integer_number = int(number1)
float_number = float(number2)
round_number = int(round(float_number))

print(number1)
print(number2)
print(round_number)
