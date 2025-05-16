x= int(input("Enter the number: "))

match x:
    case 0:
        print("the number is 0")
    case 4:
        print("the number is 4")
    case _ if x!=90:
        print("the number is not 90")
    case _ if x!=80:
        print("the number is not 80")