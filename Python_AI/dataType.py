# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType


##########################Numeric Types: int, float, complex###############################
# Text Type:	str
a="String"
print(type(a))
 
b = 5
print(type(b))

c=1.2
print(type(c))

d=2+6j
print(type(d))
##########################End Numeric  Type###############################

##########################Sequence Type: list, tuple, range###############################

#lists are mutable (changeable), while tuples are immutable (unchangeable)
#List
e=["apple", "banana", "cherry"]
print(type(e))

e[1]="fox"
print(e)

#Tupple
f=("apple", "banana", "cherry")
# f[1]="fox"
# print(f[1])

#range (start,end, difference/steps)
g = range(3, 10, 2)
#convert to list to display the content of x:
print(list(g))

##########################End Sequence Type###########################

##########################Mapping Type: dict##########################
h = {"name" : "John", "age" : 36}

print(h['name'])

##########################End Mapping Type###########################


##########################Set Type: set, frozenset##########################
set = {"apple","apple", "banana", "cherry",1,True,2}
set.add("Ram")
print(set)
#in sets/frozenset duplicate is not allowed and true and 1 has same value in the set/ mutable type
#set is mutable but forzenset is immutalble
j = frozenset(set)
print(j)

##########################End Set Type##########################

##########################Boolean Type: bool##########################
k = bool(0)
print(k)
##########################End Boolean Type##########################

##########################Binary Types: bytes, bytearray, memoryview####################
#bytes() returns an object that cannot be modified, and bytearray() returns an object that can be modified.

# bytes → “I will read it only.”

# bytearray → “I want to edit it.”

# memoryview → “I want to look inside without making a copy.”



l = "rohit"
 # UTF-8 encoding is used
b = bytes(l, 'utf-8',errors='strict') 
print(b)


# Create a bytearray from a string
ba = bytearray("Geeks for geeks!", "utf-8")
print(ba)  # Output: bytearray(b'geeks for geeks!')

# Modify the bytearray 
ba[1] = 105  # 'i' in ASCII is 105
print(ba)

##########################End Binary Type##########################

##########################None Types: NoneType####################
x = None
if x == None:
    print("x is None")
else:
    print("x is not None")

##########################End None Type##########################