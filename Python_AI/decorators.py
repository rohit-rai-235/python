#this function changes the return value of another function to uppercase using a decorator
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

#example usage of the decorator
@changecase
def myfunction():
  return "Hello Rohit"

print(myfunction())


#Arguments in the Decorated Function

def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))