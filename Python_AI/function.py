#In Python, a function is defined using the def keyword, followed by a function name and parentheses:

def my_function():
  print("Hello from a function")

#calling function
my_function()


##############################################################


def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

##############################################################

#default parameter

def my_function(name = "friend"):
  print("Hello", name)

my_function()


###############################################################

# keyword Arguments
#You can send arguments with the key = value syntax.

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

################################################################

# Mixing Positional and Keyword Arguments

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

################################################################

# Passing Different Data Types
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

################################################################

# Sending a dictionary as an argument:

def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)

################################################################

# Returning Different Data Types

def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

#####################################################################
# Combining Positional-Only and Keyword-Only

def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)