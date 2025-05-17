'''
this is used as multi-comment
'''
# this is single comment

#this sep is used for seprator and the end is used for write something in the end
print("hello",6,7,sep="@",end="endofthisline")
print("hiii")

# Data Types
a=112
print(a)
print(type(a))

b=complex(8,3)
print(b)
print(type(b))

c="rohit"
print(c)
print(type(c))

d=None
print(d)
print(type(d))

e=True
print(e)
print(type(e))

list2 =[8,4.6,[-9,8],["apple","mango"]]
print(list2)
print(type(list2))

tuple=[["Ram,Sham"],["mohan,sohan"]]
print(tuple)
print(type(tuple))

dictonary1={"name":"rohit","age":32}
print(dictonary1)
print(type(dictonary1))

#arthematic Operators

print(5+6)
print(15-6)
print(15*6)
print(15/6)
#floor operator not giving in the decimals
print(15//6)
# modulas
print(5%3)
# exponintials
print(5**3)



# type casting
#explicit type casting
aa="1"
bb="2"
cc=int(aa)+ int(bb)
print(cc)

#implicit type casting = lower casting can be converted in higher cast exmpl below output is float

v=1
h=1.6
print(v+h)

