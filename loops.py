# while and for 

# for loop
#books = ['War & Peace', '1984', 'Harry Potter', 'Art of War', 'Of Mice & Men', 'The Humans']

#for bookItem in books:
#    print ("I have read " + bookItem)

#for bookItem in books:
#    if bookItem == '1984':
#        print (bookItem + " is the only book in the list that can be cast to an int")
#    else:
#        print(bookItem)

# strVar = '011010101001'
# for charVar in strVar:
#     if int(charVar):
#         print("This was false")
#     else:
#         print("The Truth!")

#for numVar in range(0,100):
#    print(numVar)

#----
#varForDictionary = { 'name':'Mohab' , 'size':'big' , 'age':'24' }

#for thingsVar in varForDictionary:
#    print(varForDictionary[thingsVar])

#----



#While

#inputNumVar = int(input('Put in a whole number: '))
#resultVar = 1
#while inputNumVar > 0:
#    resultVar = resultVar * inputNumVar
#    inputNumVar = inputNumVar - 1

#print(resultVar)


#inputNumVar = int(input('Put in a whole number: '))
#resultVar = 1

#while True:
#    resultVar = resultVar * inputNumVar
#    inputNumVar = inputNumVar - 1
#    print(resultVar)
#    if resultVar > 150:
#        break



#for i in range(10):
#    print(i)

#    if i == 5:
#        break


#for i in range(10, 21, 2):
#    print(i)


#inputNamesList = []
#numVar = 5
#while numVar > 0:
#    inputNameVar = input('Type IN: ')
#    inputNamesList.append(inputNameVar)
#    numVar = numVar - 1
#print(inputNamesList)



# names = 0
# while names < 5:
#     name = input("Please enter a name: ")
#     print(name + " Is awesome!")
#     names = names + 1


#inputString = 'rotor'
#outputString = 'rotor'
#inputString == outputString

#------------------
varName = input("Please enter a name to check if it's a palindrome: ").lower()
varCheck = ''
for i in range(len(varName)-1,-1,-1):
    varCheck = varCheck + varName[i]
if varCheck == varName:
    print("Congrats your name is a palindrome: " + varName)
else:
    print("Sorry: " + varName + " Is not a palindrome")




#---------------
#Alternative Palindrome

#word=input('Enter word that will be checked: ')
#reversed_word= word[::-1]
#count = len(word)
#wordlist=[]
#starting_word=list(word.lower())

#print(starting)

    

#for i in range(0,count):
    #converting the string to lower case and appending to a list
#    if word[i].lower() == reversed_word[i].lower():
#        wordlist.append(word[i].lower())
        #print(wordlist)
    #Comparing the lower case version of the input(starting word)
    #and the wordlist
#    if wordlist == starting_word:
#        print('Its a palindrome')
#----------------

#Another palindrome example

# palinVar = input('Type in: ')

# numChar = len(palinVar) - 1
# raVnilap = ''

# while numChar >= 0:
#     raVnilap = raVnilap + palinVar[numChar]
#     numChar -= 1

# if raVnilap == palinVar:
#     print('PALINDROME')
# else:
#     print('NO')

