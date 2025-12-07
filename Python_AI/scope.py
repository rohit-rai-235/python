#############Local Scope############
def myfunc():
  x = 300
  print(x)

myfunc()

#############Function Inside Function############

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#############Global Scope############
x = 254
def myfunc():
    print(x)
myfunc()

print(x)

##############Nonlocal Keyword############
def myfunc1():
  x = "Jane"
  def myfunc2():
   nonlocal x
   x = "hello"
   
  myfunc2()
  return x

print(myfunc1())

################The LEGB Rule############
# Local - Inside the current function
# Enclosing - Inside enclosing functions (from inner to outer)
# Global - At the top level of the module
# Built-in - In Python's built-in namespace

x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)

