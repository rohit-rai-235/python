# The string are immutables- they never change
name='Rohit'
print(name)

na='''
this is multiline string

we can also add spaces and other symbols and charaters
'''
print(na)

#this string is like the array of the character
print(name[0])
print(name[1])

#lets play for each loop for string

for char in name:
    print(char)

#string slicing and operations
#find lenth of the string
print("the length of the string:",len(name))

#slice the character from the string
print("the slice from 0 to 3 of the string:",name[0:3])
print("the slice from 1 to 3 of the string:",name[1:3])
print("the slice from :3 of the string:",name[:3])
print("the slice from : of the string:",name[:])
print("the slice from 0:-3 of the string:",name[0:-3])
# OR
print("the slice from 0:len(name)-3 of the string:",name[0:len(name)-3])
print("the slice from 0:-3 of the string:",name[-3:-1])

# String Operations
names="!!Viraj!!!!!!!!!"
print(names.upper())
print(names.lower())
print(names.rstrip("!"))
print(names.lstrip("!"))
print(names.replace("!","@"))
print(names.split("j"))

blog="introduction of the fOrest"
print(blog.capitalize())
print(len(blog))
print(len(blog.center(50)))
print(blog.center(50))
print(blog.count("o"))
print(blog.endswith("rest"))
print(blog.endswith("ti",4,10))
print(blog.find("ti")) # if string is not find it will give the -1
print(blog.index("ti")) #if we are not sure about the string is available dont use index method

trt="rohit00f"
print(trt.isalnum()) # is alfanumeric no space only alf or numb
print(trt.isalpha()) # is alfa only alfa no numb
print(blog.islower())

str1="We will rock you \n buddy"
print(str1)
print(str1.isprintable()) # giver false because it contain \n which is not a printable string

str2=" "
print(str2.isspace())

str3="This is Title"
print(str3.istitle())
print(str3.startswith("This"))
print(str3.swapcase())
print(str3.title())