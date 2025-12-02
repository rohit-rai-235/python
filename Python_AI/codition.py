# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

a = 33
b = 200
if b > a:
  print("b is greater than a")


a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


a = 5
b = 2
if a > b: print("a is greater than b")


a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")



#The pass statement is a null operation - nothing happens when it executes. It serves as a placeholder.
a = 33
b = 200

if b > a:
  pass