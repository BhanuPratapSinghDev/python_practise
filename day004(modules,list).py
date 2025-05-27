# Module

import day4_my_module                           # making own module to learn
#print(day4_my_module.my_DOB())                 TypeError: 'int' object is not callable
print(day4_my_module.my_DOB)

#print(day4_my_module.my_country())             TypeError: 'str' object is not callable
print(day4_my_module.my_country)

# Randomisation : by using random module
import random
print(random.randint(1,10))               # start = a and end = b both must be integers and both inclusive values

print(random.randrange(1,10,1))  # just like range() including 1 excluding 10
                                                #step value by default 1
print(random.uniform(1.1,10.1))           # returns random float  [1.1 , 10.1 ]

print(random.random())                          # returns random float [0,1)
print(random.random()*10)

colours=["red","blue","green","pink"]

print(random.choice(colours))                   # needs a sequence

print(random.sample(colours,2))              # needs an integer to get sample of 2 unique elements  in list form ,
                                                # from a list

print(random.shuffle(colours))                  # mutable sequence ,just shuffles in place not returns itself
print(colours)

# List : ordered elements data structure
fruits=["Mango", "Watermelon","Apple","Pear"]   # don't forget "  " as elements are strings here
print(fruits[0])

fruits[-1]="Guava"
print(fruits)                                   #['Mango', 'Watermelon', 'Apple', 'Guava']

fruits.append("Apricot")                        # to add one element at last
print(fruits)

# fruits.extend("kiwi")                        #['Mango', 'Watermelon', 'Apple', 'Guava', 'Apricot', 'k', 'i', 'w', 'i']
# print(fruits)
fruits.extend(["Kiwi","Banana"])                #iterable needed
print(fruits)                                   #['Mango', 'Watermelon', 'Apple', 'Guava', 'Apricot', 'Kiwi', 'Banana']

fruits.insert(2,"Raspberry")
print(fruits)                                  #['Mango', 'Watermelon', 'Raspberry', 'Apple', 'Guava', 'Apricot', 'Kiwi'
                                               # , 'Banana']
#fruits.pop()                                  by default the last one
#print(fruits)                                 ['Mango', 'Watermelon', 'Raspberry', 'Apple', 'Guava', 'Apricot', 'Kiwi']

fruits.pop(4)
print(fruits)                                #['Mango', 'Watermelon', 'Raspberry', 'Apple', 'Apricot', 'Kiwi', 'Banana']

fruits.remove("Mango")                       # removes first value equal to Mango
print(fruits)                                #['Watermelon', 'Raspberry', 'Apple', 'Apricot', 'Kiwi', 'Banana']

fruits_new=['Watermelon', 'Raspberry', 'Apple', 'Apricot', 'Kiwi', 'Banana']
#print(fruits_new[10])                        IndexError: list index out of range
#to get last element
number_of_fruits = len(fruits_new)
#print(fruits_new[number_of_fruits])          IndexError: list index out of range
print(fruits_new[number_of_fruits-1])         # Banana

# Nested List
fruits=["Apple","Mango"]
vegetables=["Spinach","Brocolli"]
food=[fruits,vegetables]                      #[['Apple', 'Mango'], ['Spinach', 'Brocolli']]
print(food)
