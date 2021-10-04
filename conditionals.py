
nameVar1 = "Brian"
listOfAnimals = ['sheep', 'cat', 'dog', 'squirrel', 'badger', 'elephant', 'mouse']
varForDictionary = { 'name':'Mohab' , 'size':'big' , 'age':'24' }

#if listOfAnimals[1] == 'cat':
#    print ('i found the cat')

#if 'sheep' in listOfAnimals:
#    print('Sheep is in the list of values')
#print('This line will always print')

#if 'Mohab' in varForDictionary.values():
#    print('Mohab is in the list')


if nameVar1 != 'Brian' or 'Mohab' in varForDictionary.values():
    print('Mohab is in the list of values')


varForDictionary = { 'name':'Mohab' , 'size':'big' , 'age':'24' }
listOfAnimals = ['sheep', 'cat', 'dog', 'squirrel', 'badger', 'elephant', 'mouse']

if 'cat' in listOfAnimals or 'dog' in listOfAnimals:
    print('Found a cat or dog')

if 'cat' in listOfAnimals:
    print('Found a cat')
elif 'dog' in listOfAnimals:
    print('Found a dog')
else: print ('cats and dogs not found')



#devs_money = 100
#dev_can_play_smash = False

#if devs_money > 10 and dev_can_play_smash:
#    print("Dev enters a smash tournament!")
#elif devs_money < 10 and dev_can_play_smash:
#    print("Dev is too poor to enter")
#else:
#    print("Dev just can't play smash")


#SOLUTION with elif statement:
mark = int(input('insert mark here: '))

if mark > 85 :
    print("Distinction")
elif 85 >= mark > 65 :
    print("Pass")
else:
    print("Fail")

#SOLUTION without elif statement:
mark = int(input('insert mark here again: '))

if mark > 85 :
    print("Distinction")
if 85 >= mark > 65 :
    print("Pass")
if mark <= 65 :
    print("Fail")

#SOLUTION 'nested' if statement:
mark = int(input('insert mark here one more time: '))

if mark >= 65:
    if mark > 85:
        print("Distinction")
    else:
         print("Pass") 
else:
    print("Fail")