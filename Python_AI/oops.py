#class and object
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)
del p1
# It is showing error because it is deleted = print(p1.x)


#pass statement in class
class MyClass:
    pass


#__init__() function

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 28)

print(p1.name)
print(p1.age)

#or set manually

class Person:
  pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age)

# self parameter is just a reference to the current instance of the class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

    #class method
  def myfunc(self):
    print("Hello my name is " + self.name)

instance = Person("John", 36)
instance.myfunc()

#Class Properties vs Object Properties

class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

Person.species="rohit"

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

#__str__() function

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    #with the help of str function we can return a string when we print the object else showing the memory location
  def __str__(self):
    return f"{self.name} ({self.age})"    

p1 = Person("Tobias", 36)

print(p1)


#inheritance

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname() 
