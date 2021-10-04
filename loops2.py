
# for i in range(10):
#     num = i+1
#     print(num*2)

# for letter in 'apples & oranges':
#     print(letter)

# my_list = ['cat', 'dog','mouse']

# for i in my_list:
#     print(i)

# if True: 
#     print("hello there")

# lenVar = len(my_list)
# print(lenVar)

#---------------


# my_fruit = ["Apple", "Banana", "Orange"]

# for fruit in my_fruit[0:3]:
#     print(fruit.upper())


my_list = []
for i in range(1500,2701):
    if (i%5==0) and (i%7==0):
        my_list.append(i)

for x in my_list:
    if (x%8==0):
        print(x)