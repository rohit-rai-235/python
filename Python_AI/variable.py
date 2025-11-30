x=5 # x is of type int
y="John" # y is of type str
print(x)
print(y)


x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

#Get the Type
x = 5
y = "John"
print(type(x))
print(type(y))


#Case-Sensitive
a = 4
A = "Sally"
print(a)
print(A)

#multivariables
x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Global Variable
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#end

#global
x = "awesome"

def myfunc():
  #local varaible
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#end


#global keyword:If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = "global varibale"

myfunc()

print("Python is " + x)